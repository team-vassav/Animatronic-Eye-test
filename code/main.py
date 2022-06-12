import cv2
import numpy as np
from time import sleep
import pigpio
pi = pigpio.pi()

servoPinVer = 32
servoPinHor = 33

frameWidth = 480
frameHeight = 320
cap = cv2.VideoCapture(0)

posX = 0
posY = 1700

hsvVal = [93,114,117,255,0,255]


def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",15,255,empty)
cv2.createTrackbar("Threshold2","Parameters",30,255,empty)
cv2.createTrackbar("Area","Parameters",300,2000,empty)


def getContours(img,imgContour):
    cx,cy = 0,0
    contours, hierarchy = 
        cv2.findContours(img, cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x , y ), 
                (x + w , y + h ), (0, 255, 0), 2)

            cx = int(x + (w / 2))
            cy = int(y + (h / 2))

            cv2.line(imgContour, (int(frameWidth/2), 
                int(frameHeight/2)), (cx,cy),
                     (0, 0, 255), 2)
    return cx,cy

def conRange(oldMin,oldMax,newMin,newMax,oldValue):
    return (((oldValue -oldMin)*(newMax-newMin))/
        (oldMax-oldMin))+ newMin


while True:

    #Image processing 
    _, img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    imgContour = img.copy()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower = np.array([hsvVal[0],hsvVal[2],hsvVal[4]])
    upper = np.array([hsvVal[1],hsvVal[3],hsvVal[5]])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    imgBlur = cv2.GaussianBlur(mask, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    cx,cy = getContours(imgDil, imgContour)
    print(cx,cy)

   
    # Moving motors
    #vertical
    if cy!=0:
        centerY = frameHeight//2
        if cy>centerY+20:
            posY = int(np.clip(posY+10,1400,2500))
        elif cy<centerY-20:
            posY =  int(np.clip(posY-10,1400,2500))
        pi.set_servo_pulsewidth(17,posY)

     #### Horizontal
    if cx!=0:
       posX = int(conRange(frameWidth,0,2000,2500,cx))
       pi.set_servo_pulsewidth(18,posX)

    cv2.imshow('Result', imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
