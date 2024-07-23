nn=["0","1","2","3","4","5"]
msg="ILLEGAL CARD ACCESS"
no=""
import cv2
import numpy as np
import RPi.GPIO as gpio
from datetime import datetime
from cam import VideoCapture
import time
now = datetime.now()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
val=0
ix=1
#cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_BUFFERSIZE, 1);
#cam.set(cv2.CAP_PROP_FPS, 2);
import time
import serial
from sm.apisend import send
import re
import urllib
import thingspeak
from Adafruit_CharLCD import Adafruit_CharLCD
#pyrebase
import pyrebase

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=12,
                       cols=20, lines=4)
api="NGC3TP4AJ6F9VCY5"
id="1567358"
sap="O9QjuSYbPIwEM3fVJnNrZsdD1XtygkvLRaCle84WmTGp6BcoxiChUB42u98IqiSQjvREz1Lfp5bt0VZX"
#import maskchk
import time
import threading
exp = re.compile(r'b')          
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")      
data = serial.Serial(
                    port='/dev/ttyS0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print (" ")
a=0
lcd.clear()
lcd.message('  IOT ATTENDANCE \n       SYSTEM')
time.sleep(3)  

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')

bw_threshold = 80

font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = (0, 255, 0)
not_weared_mask_font_color = (0, 0, 255)
noface = (255, 255, 255)
thickness = 2
font_scale = 1
weared_mask = "wearing MASK"
not_weared_mask = "NO MASK"
Id=""

cap = VideoCapture(0)

def face():
   a=""
   ix=1
   while (ix==1):

    im =cap.read()
    
    laststate=0

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # For each face in faces
    for(x,y,w,h) in faces:


        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)


        Id,n = recognizer.predict(gray[y:y+h,x:x+w])
        

        if(Id <= 5 and n<190):
            Id=nn[Id]
            ix=0
            val=Id
 
        else:
            Id="unknown"
            #print("unknown")

	    
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)


    cv2.imshow('im',im) 
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

   lcd.clear()
   lcd.message('  FACE VERIFICATION \n        OK \n\n   PUT YOUR MASK')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          10')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          9')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          8')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          7')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          6')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          5')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          4')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          3')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          2')
   time.sleep(1)
   lcd.clear()
   lcd.message('PUT YOUR MASK \n \n  TAKING IMAGE IN  \n          1')
   time.sleep(1)
   lcd.clear()
   lcd.message('\n \n   TAKING IMAGE  \n          ')
   ix=1
   img =cap.read()
   img = cv2.flip(img,1)
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)
   faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 4)
   print("checking for mask")
   if(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, "No face found...", org, font, font_scale, noface, thickness, cv2.LINE_AA)
        a="UNMASKED"
   elif(len(faces) == 0 and len(faces_bw) == 1):
        cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        a="MASKED"
   else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)
        if(len(mouth_rects) == 0):
            cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
            a="MASKED"
            print("MASK VERIFICATION OK")
            lcd.clear()
            lcd.message('MASK VERIFICATION \n \n      SUCCESS')
            time.sleep(3)


        else:
            for (mx, my, mw, mh) in mouth_rects:
               if(y < my < y + h):
                 print("UNMASKED PERSON")
                 a="UNMASKED"
                 cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
                 lcd.clear()
                 lcd.message('MASK VERIFICATION \n \n      FAILED')
                 time.sleep(3)        
                 break

   lcd.clear()
   lcd.message('  \n   ATTENDANCE MARKED ')
   return(Id,a)

try:     
   while 1:
         lcd.clear()
         lcd.message('       PLEASE\n   PLACE YOUR CARD  ')        
         print ("Place the card")
         x=data.read(12)#print upto 10 data at once and the 
                        #remaining on the second line
         if str(x)=="3B0037D2A37D":
             a=1
             usr="user1"
             print ("Card No - ",x)
             print ("WELCOME USER 1")
             lcd.clear()
             lcd.message(' \n   WELCOME USER 1 ')
             time.sleep(3)
             print (" ")
         
         elif str(x)=="3B00381F7D61":
             a=1
             usr="user2"
             print ("Card No - ",x)
             print ("WELCOME USER 2")
             lcd.clear()
             lcd.message(' \n   WELCOME USER 2 ')
             time.sleep(3)
             print (" ")

         elif str(x)=="3B00382DBB95":
             a=1
             usr="user3"
             print ("Card No - ",x)
             print ("WELCOME USER 3")
             lcd.clear()
             lcd.message(' \n   WELCOME USER 3')
             time.sleep(3)
             print (" ")
         
         else:
             a=0
             print ("WRONG CARD.....")
             print (" ") 
             lcd.clear()
             lcd.message(' \n       WRONG CARD  ')
             send(no,msg,sap)
             time.sleep(3)
             continue

         print("Taking Image...")
         f,m=face()  
            
         print("\n")
         time.sleep(2)
         print("Sending data...")
         n=open("out.txt","a+")
         thingspeak.send(api,str(x),usr,str(f),str(m))
         #pyrebase
         firebaseConfig = {
            'apiKey': "AIzaSyBVxy4oK6LzUREKBSgik39cxkxUl_Ea64M",
            'authDomain': "batch7-project-a09d0.firebaseapp.com",
            'databaseURL': "https://batch7-project-a09d0-default-rtdb.firebaseio.com",
            'projectId': "batch7-project-a09d0",
            'storageBucket': "batch7-project-a09d0.appspot.com",
            'messagingSenderId': "976184391607",
            'appId': "1:976184391607:web:d1b45ebef488e440981a32"
            }
         firebase = pyrebase.initialize_app(firebaseConfig)
         db = firebase.database()
         dt = {'card_id': x, 'name': usr, 'face_id': f, 'mask_status': m}
         db.child('Attendance').push(dt)
         time.sleep(3)

except KeyboardInterrupt:
       data.close()