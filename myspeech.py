import speech_recognition as sr

  #This is my python speech to text
  #Ali Perpetual
  #2019364028

r = sr.Recognizer()
print("Recognising my speech...")

let = sr.AudioFile('ali.wav')
with let as source:
    audio = r.record(source)
    
    type(audio)
    
    r.recognize_google(audio)
    
    print("Ending my speech Recognition..")
    
    #ECE 331 Assignment
 
    
    