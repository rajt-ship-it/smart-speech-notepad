import pyttsx3
import speech_recognition as sr
def l():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Speak now...")
        audio = recognizer.listen(source,timeout=10)

    try:
        text1 = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", text1)
        return text1#return karoge tab hi toh jab again use hoga toh defined rahega text1

    except sr.UnknownValueError:
        print("I could not understand.")
        print("try entering it by keyboard")
        a=input("enter here ")
        return a

    except sr.RequestError as e:
        print("Service error:", e)
        print("try entering it by keyboard")
        a=input("enter here ")
        return a
     
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",100)
    engine.say(text)
    engine.runAndWait()
#engine.say("hello") note;- aise agar har jagah yeh engine.say("eekhfhfhfj") likhoge toh bas ek baar bolega ange bhi agar likha hoga toh ahi bolega isliye def karke shruwat se func start kato
#engine.setProperty("rate",150)
#engine.runAndWait()
import os
if not os.path.exists("python all works"):
    os.mkdir("python all works")
file="python all works/notepad.txt"
f=open(file,'a')
k=open(file,'r')
text=k.read()
li=text.splitlines()#yaha list(text) nahi use hoga because yeh list function ek string type ke chithre karke list banata hai jaise raj='r','a','j'.vaise yaha per text=hello\nraj\n etc type mein hoga toh splitline use karke hamne banaya toh splitline("\n") automatic ho gaya jab notdpad se yaha data aaya hoga to next line mein jo hoga vo /n se likha hoga toh ussko alag alag karna padega na taki samajh sake
class notepad:
    def __init__(self):
        self.note=[]
        self.note.extend(li)#note yaha append nahi karsakte because li ek list hai and append functions added anything inside already exiting list means it will get converted to nested list. and this we used because if any data is there in notepad that must be extracted first
    def save_to_file(self):
        with open(file,'w') as f:
            for i in self.note:
                f.write(i +"\n")
                #f.close() yaha yeh likhdoge toh while ke ander hi file band hojayegi fir isske baad ke file wale operations execute honge toh error aayega because file toh band hai na 
    def add(self):
        speak("enter your note here")
        a=input("enter your note here")
        self.note.append(a)
        speak("note has been added")
        self.save_to_file()
        print("note has been added")
    def remove(self):
        speak("enter note to be removed")
        a=input("enter note to be removed")
        if a in self.note:

            self.note.remove(a)
            self.save_to_file()
            speak("note has been removed")
        else:
            speak("note not found")
    def show(self):
        # return (f"added note is {self.note}") yeh yaha return lagadiya toh func call hone per kisi variable ko yeh value assign kardega but but yeh print ya out thodi dega na
        
        message = f"added note is {self.note}"
        print(message)
        speak(message)
r=notepad()
while True:
    speak("enter what you want add/remove/show/exit")
    voiceinput=l()#yeh dekho upper l() def kiya tha because ussmein return dala tha toh usski value store toh karni hogi kahi na
    if voiceinput.lower()=="add":
        r.add()
    elif voiceinput.lower()=="remove":
        r.remove()
    elif voiceinput.lower()=="show":
        r.show()
    elif voiceinput.lower()=="exit":
        break
#NOTE:-file mein kuch bhi update karne wala command jo just niche hai vo jab loop khattam hogi tab chalta tha isliye upper daldiya taaki turant update ho also yaha append tha per isse overight nahi hoga issliye "w" use kiya isse pura data notepadse hatjayega per or jo list mein aab hai vo store hoga and pehle hi list mein ham pura data lachuke the toh loss bhi nahi hoga 
# for i in r.note:
#     f.write(i + "\n")#here if you want to get your added note to be in other line then use this otherwise ""a.notehellorajhowareyouwhat"" something like this will happen ok
    

t=open(file,'r')
print(t.read())
t.close()
