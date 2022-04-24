# Animatronic-Eye
This repository provides the work done by team VassaV as an undergraduate mini project

Animatronics is a blended word which is formed by the combination of Animate and Electronics. We (VassaV) as a team are interested in multi disciplinary fields such as Computer Science, Robotics and Electronics. With the keen interest on this we created this project with the inspiration of Walt Disney's facinated puppets in his cartoon shows. 

This project presents simulation of human eyes and their movements in different situations. The mechanical parts (which acts as muscles in human eye structure) are designed in Fusion360 and movement of those eye balls is controlled through servo motors (which acts as Cyliary muscles). The electronics setup (which plays role of Nerves) feeds the info to Brain of this Project. The Brain which controls these entire anematronic eyes is Rasperry pi4. Where a pre-programmed mechanism drives these movements. 

We used two Raspberry pi cameras (which acts as perceivers of image) for gathering live video then the video was sent to Rasperry pi for processing. The Object detection program in Raspberry pi understands the live feed from camera and based on the object's central co-ordinates (with some math calucaltion behind the program) we determine the point co-ordinates to where these eya balls must move. Raspberry pi program calculates this and sends instructions to servo motors, based on these servo motors move in specified direction. 

This project can serve as an attachment to the robots where anematronics plays major role (in comic shows). 
