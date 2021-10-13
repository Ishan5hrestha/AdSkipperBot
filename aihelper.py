import pyautogui
import keyboard
import time
from win32gui import GetCursorInfo

while True:
	time.sleep(0.8)
	points = []
	x = 0
	y = 0
	color = []
	string = []
	click = [0,0]
	rough = 1
	while True:
		if keyboard.is_pressed("shift"):
			x,y = pyautogui.position()
			try:
				color = pyautogui.pixel(x,y)
				string.append([x,y,color[0],color[1],color[2]])
				time.sleep(0.8)
			except:
				pass
		if keyboard.is_pressed("ctrl"):
			x,y = pyautogui.position()
			click[0] = x
			click[1] = y
			time.sleep(0.8)
		if keyboard.is_pressed("space"):
			print("if ",end="")
			for i in string:
				if rough!=1:
					print(" and ",end="")
				else: rough = 0
				print("checkPixel(",i[0],",",i[1],",",i[2],",",i[3],",",i[4],")",end="")
			print(": click(",click[0],",",click[1],")")
			break

		
