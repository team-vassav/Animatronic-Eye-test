# Animatronic-Eye 👀
This Repository provides the work done by team VASSAV as an Undergraduate 👨‍🎓 mini project.

Animatronics is a blended word which is formed by the combination of Animate and Electronics. We (VASSAV) as a team are interested in multi disciplinary fields such as Computer Science 💻, Robotics 🤖 and Electronics. With the keen interest on this we created this project with the inspiration of Walt Disney's facinated puppets in his cartoon shows. 

This Project presents simulation of human eyes and their movements in different situations. The Mechanical parts (which acts as muscles 💪 in human eye structure 👁️) are designed in Fusion 360  and movement of those eye balls is controlled through servo motors (which acts as Cyliary muscles 💪). The Electronics setup (which plays role of Nerves) feeds the info to Brain 🧠 of this Project. The Brain which controls these entire animatronic eyes is Rasperry Pi 4B, where a pre-programmed mechanism drives these movements. 

We used two Raspberry pi cameras 📷 (which acts as perceivers of image 🖼️) for gathering live video 📹 then the video was sent to Raspberry pi for processing. The Object detection program in Raspberry pi understands the live feed from camera 📷 and based on the object's central co-ordinates (with some math calucaltion behind the program) we determine the point co-ordinates to where these eye balls must move. Raspberry pi program calculates this and sends instructions to servo motors, based on these servo motors move in specified direction ➡️. 

This project can serve as an attachment to the robots where animatronics plays major role (in comic shows). 
