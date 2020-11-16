import speech_recognition as sr
import subprocess as sp
import pyttsx3
import os
print("\t\t\t\tHi, Iam your assistant")
pyttsx3.speak("Hi, Iam your assistant,tell me what you want to do")
while True :
	r=sr.Recognizer()
	with sr.Microphone() as source:
		pyttsx3.speak("please say something")
		print("\t\t\t\tstart say")
		audio = r.listen(source)
		print("\t\t\t\tspeech done")
		pyttsx3.speak("Ok working on it")
		data = r.recognize_google(audio)
		print(data)
		if "hadoop" in data or "Hadoop" in data or "big data" in data:
			os.system("python hadoopmenu.py")
		elif "AWS" in data or "aws" in data or "cloud" in data:
			os.system("python awsmenu.py")
		elif "docker" in data or "container" in data:
			os.system("python dr.py")
		#elif "logical" in data and "volume" in data:
			#os.system("python lvm.py")
		elif "extend" in data or "increase" in data and "logical" in data and "volume" in data:
			os.system("python lvmextend.py")
		else:
			print("can't understand")
		input("Click Enter to continue")