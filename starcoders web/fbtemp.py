# Imports
#-------------------------------------------------------------------------------
import pyrebase

# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
  'apiKey': "AIzaSyAmHhBKHbU_zxsRQqiWcD1t159ZFq1dUQI",
  'authDomain': "automated-ray-380216.firebaseapp.com",
  'projectId': "automated-ray-380216",
  'storageBucket': "automated-ray-380216.appspot.com",
  'messagingSenderId': "271666645379",
  'appId': "1:271666645379:web:922c2df33cc6c1e774ceb6",
  'measurementId': "G-7BJ7YSPF1Q",
  'databaseURL':'https://automated-ray-380216-default-rtdb.firebaseio.com/'
 };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data = db.child("Users").get()
valn=data.val()
print(valn)
n=len(valn)
addli=[]
emli=[]
nameli=[]
pwli=[]
pnli=[]
print(list(valn[0].values())[0])
for i in range(1,n):

    emli.append(list(valn[i].values())[0])
    nameli.append(list(valn[i].values())[1])    
    pwli.append(list(valn[i].values())[2])

print(emli)
print(nameli)
print(pwli)
