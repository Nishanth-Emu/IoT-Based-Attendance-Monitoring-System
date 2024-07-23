# Import OpenCV2 for image processing
import cv2
import os
# Import numpy for matrices calculations
import numpy as np
from datetime import datetime
now = datetime.now()
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()
os.system("sudo rm -r /home/pi/Desktop/out.txt")
# Load the trained mode
recognizer.read('trainer/trainer.yml')
nm=['','VISHNU','BALA','NISHANTH']
# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX
laststate=0
# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id,n = recognizer.predict(gray[y:y+h,x:x+w])
        if(n<80):
            Id=Id
            id2=Id
        else:
            Id="UNKNOWN"
            id2=0
        
        if(laststate!=Id ):
            n=open("/home/pi/Desktop/out.txt","a+")
            n.write("\n")
            n.write(dt_string+"   "+str(Id) )

        laststate=Id        
        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, nm[id2], (x,y-40), font, 1, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
