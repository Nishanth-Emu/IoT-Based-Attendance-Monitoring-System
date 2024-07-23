# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
import urllib.request
import pyrebase

# thingspeak
x = str(input("enter card id : "))
x = x.replace(' ', "%20")
x = x.replace('\n', "%0A")
usr = str(input("enter your name : "))
usr = usr.replace(' ', "%20")
usr = usr.replace('\n', "%0A")
f = str(input("Enter your Face ID : "))
f = f.replace(' ', "%20")
f = f.replace('\n', "%0A")
m = str(input("Enter your mask : "))
m = m.replace(' ', "%20")
m = m.replace('\n', "%0A")

# msg = str(input('Enter your message : '))
# msg = msg.replace(' ', "%20")
# msg = msg.replace('\n', "%0A")
b = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=RL2RLT93U16LUYS5&field1=0'+x+usr+f+m)
print("\nYour message has successfully been sent!")

# firebase data
# cred = credentials.Certificate("D:\encryption image\serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
# 	'databaseURL': 'https://batch7-project-a09d0-default-rtdb.firebaseio.com/'
# })

# ref = db.reference('/')
# ref.set({
# 	"Attendance":
# 	{
# 		"date": date,
# 		"name": name,
# 		"face_id": face,
# 		"mask": mask,
# 		"status": status
# 	}
# })

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

data = {'card_id': x, 'name': usr, 'face_id': f, 'mask': m}
db.child('Attendance').push(data)








