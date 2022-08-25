from time import sleep
import re
import playsound
from tkinter import *
from threading import Thread

def startTimer(query):
	nums = re.findall(r'[0-9]+', query)
	time = 0
	if "minute" in query and "second" in query:
		time = int(nums[0])*60 + int(nums[1])
	elif "minute" in query:
		time = int(nums[0])*60
	elif "second" in query:
		time = int(nums[0])
	else: return

	print("Timer Started")
	sleep(time)
	playsound.playsound("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\audios\\Timer.mp3")



