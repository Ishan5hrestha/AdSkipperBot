from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api, win32con
from win32gui import GetWindowText, GetForegroundWindow,GetCursorInfo

#560,500 Go button location 760,500 color: 244,149,23
#Right top button >> 829,55 => 27,51,90 then 34,43,58
#95,47,8 error at menu

def press(key):
	keyboard.press_and_release(key)

def write(text):
	keyboard.write(text);time.sleep(0.2)

def instant_write(text):
	keyboard.write(text);time.sleep(0.2)
	keyboard.press_and_release('enter')

def active_window():
	fullname = GetWindowText(GetForegroundWindow())
	fullname = fullname.split("-")
	name = fullname[len(fullname)-1]
	name.replace(" ","")
	return name.lower()

def alttab(num):
	pyautogui.keyDown('alt')
	for i in range(num):
		pyautogui.press('tab')
	pyautogui.keyUp('alt')

def contains(sentence, words):
	found = False
	word_array = words.split(",")
	for word in word_array:
		if word.find("&")!=-1:
			wo = word.split("&")
			for rd in wo:
				if sentence.find(rd)!=-1:
					found=True
				else:
					found=False
					break
			if found == True: return 1;
		else:
			if sentence.find(word)!=-1: return 1
			else: return 0

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.001) #This pauses the script for 0.01 seconds
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def drag(x1,y1,x2,y2):
	win32api.SetCursorPos((x1,y1))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.2) #This pauses the script for 0.01 seconds
	win32api.SetCursorPos((x2,y2))
	time.sleep(.5)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def checkPixel(x,y,a,b,c):
	try:
		color = pyautogui.pixel(x,y)
		if (color[0] == a and color[1] == b and color[2] == c):
			return True
		return False
	except:
		return False

def checkPixelOC(x,y,a,b,c):
	try:
		color = pyautogui.pixel(x,y)
		if (color[0] > a and color[1] > b and color[2] > c):
			return True
		return False
	except:
		return False

def checkAlphaLower(x1,y1,x2,y2,r):		#check if the alpha of cntrast is lower to check button
	try:
		color1 = pyautogui.pixel(x1,y1)
		color2 = pyautogui.pixel(x2,y2)
		if (abs(color1[0]-color2[0]) >r and abs(color1[1]-color2[1]) >r and abs(color1[2]-color2[2]) >r):
			return True
		return False
	except:
		return False	

def clearApps():
	click( 1347 , 708 )
	time.sleep(2)
	drag(672, 146, 672, 548)
	time.sleep(2)
	click( 821 , 71 )
	time.sleep(0.5)
	press("escape")
	time.sleep(10)


class phone:
	
	def __init__(self, name, state):
		self.startTime = time.time()
		self.name = name
		self.state = state
		self.App = 0
		self.sleep = 0
		self.timer = 0.0
		self.breserkTimer = 60
		self.noenergy = 0

	def startApp(self,appNo):
		if appNo == 0:
			# if checkPixel( 676 , 476 , 237 , 117 , 17 ): 
			click( 666 , 464 )	#bfast bfree
		elif appNo == 3:
			click( 783 , 463 )	#efast efree
		elif appNo ==1:
			click( 783 , 369 )	#comrade bfast bfree
			time.sleep(15)
			if checkPixel( 692 , 588 , 255 , 254 , 255 ) and checkPixel( 705 , 588 , 62 , 152 , 255 ): click( 614 , 586 )
			if checkPixel( 492 , 58 , 200 , 200 , 200 ) and not checkPixelOC( 497 , 59 , 50 , 50 , 50 ) and checkPixelOC( 503 , 59 , 200 , 200 , 200 ): click( 497 , 59 )
			click( 573 , 688 )
			time.sleep(5)
			if checkPixel( 703 , 689 , 254 , 112 , 3 ) and checkPixel( 608 , 686 , 255 , 255 , 255 ): click( 601 , 690 )
			click( 664 , 422 )
		elif appNo ==4:
			click( 783 , 369 )	#comrade efast efree
			time.sleep(15)
			if checkPixel( 692 , 588 , 255 , 254 , 255 ) and checkPixel( 705 , 588 , 62 , 152 , 255 ): click( 614 , 586 )
			if checkPixel( 492 , 58 , 200 , 200 , 200 ) and not checkPixelOC( 497 , 59 , 50 , 50 , 50 ) and checkPixelOC( 503 , 59 , 200 , 200 , 200 ): click( 497 , 59 )
			click( 573 , 688 )
			time.sleep(5)
			if checkPixel( 703 , 689 , 254 , 112 , 3 ) and checkPixel( 608 , 686 , 255 , 255 , 255 ): click( 601 , 690 )
			click( 793 , 420 )
		elif appNo ==2:			#vasili bfast bfree
			click( 664 , 367 )
			time.sleep(15)
			if checkPixel( 692 , 588 , 255 , 254 , 255 ) and checkPixel( 705 , 588 , 62 , 152 , 255 ): click( 614 , 586 )
			if checkPixel( 492 , 58 , 200 , 200 , 200 ) and not checkPixelOC( 497 , 59 , 50 , 50 , 50 ) and checkPixelOC( 503 , 59 , 200 , 200 , 200 ): click( 497 , 59 )
			click( 573 , 688 )
			time.sleep(5)
			if checkPixel( 703 , 689 , 254 , 112 , 3 ) and checkPixel( 608 , 686 , 255 , 255 , 255 ): click( 601 , 690 )
			click( 536 , 287 )
		else:					#vasili efast efree
			click( 664 , 367 )
			time.sleep(15)
			if checkPixel( 692 , 588 , 255 , 254 , 255 ) and checkPixel( 705 , 588 , 62 , 152 , 255 ): click( 614 , 586 )
			if checkPixel( 492 , 58 , 200 , 200 , 200 ) and not checkPixelOC( 497 , 59 , 50 , 50 , 50 ) and checkPixelOC( 503 , 59 , 200 , 200 , 200 ): click( 497 , 59 )
			click( 573 , 688 )
			time.sleep(5)
			if checkPixel( 703 , 689 , 254 , 112 , 3 ) and checkPixel( 608 , 686 , 255 , 255 , 255 ): click( 601 , 690 )
			click( 657 , 282 )

	def checkSleep(self):
		if time.time()>self.timer:
			self.sleep = 0
			return False
		return True

	def isSleeping(self):
		if self.sleep>0: return True
		else: return False

	def overlord(self):
		if  self.sleep==0:print(self.timer,"Btimer:",self.breserkTimer,"Time:",time.time(),"appNo:",self.App,"energyno:",self.noenergy)
		breserk = False
		self.checkSleep()

		#you dont have energy
		if checkPixel( 653 , 429 , 255 , 255 , 255 ) and checkPixel( 657 , 346 , 255 , 255 , 255 ) and checkPixel( 668 , 315 , 95 , 47 , 8 ) and checkPixel( 789 , 425 , 2 , 134 , 120 ): 
			click( 789 , 425 )
			time.sleep(10+random.randint(0,9))
			self.noenergy += 1
		#efst
		if checkPixel( 803 , 338 , 255 , 255 , 255 ) and checkPixel( 765 , 306 , 8 , 33 , 95 ) and checkPixel( 814 , 469 , 7 , 29 , 84 ) and checkPixel( 789 , 425 , 2 , 134 , 120 ):
			click( 784 , 425 )
			time.sleep(10+random.randint(0,9))
			self.noenergy += 1

		if checkPixel( 549 , 409 , 255 , 255 , 255 ) and checkPixel( 810 , 405 , 13 , 139 , 126 ) and checkPixel( 723 , 369 , 139 , 139 , 139 ) and checkPixel( 650 , 368 , 68 , 68 , 68 ): 
			click( 808 , 407 )
			time.sleep(10+random.randint(0,9))
			self.noenergy += 1


		#mainmenu and efAst
		if ((checkPixel( 524 , 168 , 21 , 82 , 238 ) and checkPixel( 574 , 490 , 61 , 91 , 242 )) or (checkPixel( 524 , 190 , 238 , 117 , 21 ) and checkPixel( 817 , 192 , 238 , 117 , 21 ) and checkPixel( 617 , 503 , 244 , 149 , 23 ))) and self.sleep==0: 
			click( 664 , 491 )
			self.sleep = 10
			self.timer = time.time() + self.sleep
			self.breserkTimer = time.time() + 120
			# alttab (1)
	
		if time.time()>self.breserkTimer-60 and time.time()<self.breserkTimer-59.9 and self.startTime+60<time.time():
			click( 835 , 56 )


		if time.time()>self.breserkTimer and self.startTime+60<time.time():
			breserk = True
			self.breserkTimer = time.time() + 120

		# #black screen with close button
		# if checkPixel( 638 , 615 , 0 , 0 , 0 ) and checkPixel( 689 , 277 , 0 , 0 , 0 ) and checkPixel( 689 , 87 , 0 , 0 , 0 ) and checkPixel( 842 , 56 , 238 , 238 , 238 ) and checkPixel( 836 , 56 , 226 , 226 , 226 ): breserk = True
		# #Black screen error
		# if checkPixel( 481 , 632 , 34 , 40 , 45 ) and checkPixel( 834 , 454 , 24 , 28 , 31 ) and checkPixel( 496 , 193 , 9 , 11 , 12 ) and checkPixel( 840 , 61 , 2 , 2 , 2 ):
		#breserk = True
		#if checkPixel( 755 , 137 , 6 , 7 , 8 ) and checkPixel( 688 , 278 , 14 , 16 , 18 ) and checkPixel( 554 , 472 , 25 , 29 , 32 ) and checkPixel( 792 , 540 , 29 , 34 , 38 ):
		#	breserk = True



		if breserk:
			im1 = pyautogui.screenshot(region=(0,0,1366,768))
			nme = str(time.time())
			im1.save(nme+".png")
			clearApps()
			self.startApp(self.App)
			breserk = False


		#giveAWAy
		if checkPixel( 641 , 457 , 255 , 255 , 255 ) and checkPixel( 802 , 301 , 255 , 255 , 255 ) and checkPixel( 761 , 264 , 95 , 47 , 8 ) and checkPixel( 803 , 536 , 95 , 47 , 8 ): click( 790 , 467 )
		if checkPixel( 798 , 303 , 255 , 255 , 255 ) and checkPixel( 641 , 471 , 255 , 255 , 255 ) and checkPixel( 645 , 642 , 8 , 33 , 95 ): click( 787 , 462 )

		#redeem
		if checkPixel( 689 , 518 , 238 , 117 , 21 ) and checkPixel( 578 , 95 , 238 , 117 , 21 ) and checkPixel( 506 , 83 , 244 , 149 , 23 ): click( 506 , 93 )
		if checkPixel( 588 , 439 , 21 , 82 , 238 ) and checkPixel( 572 , 115 , 21 , 82 , 238 ) and checkPixel( 513 , 93 , 61 , 91 , 242 ): click( 513 , 93 )

		#Excess end

		if (checkPixel( 706 , 225 , 255 , 255 , 255 ) and checkPixel( 691 , 558 , 255 , 255 , 255 ) and (checkPixel( 679 , 679 , 95 , 47 , 8 )or checkPixel( 786 , 140 , 8 , 33 , 95 ))) or self.noenergy>10:
			click( 787 , 547 )
			self.noenergy = 0
			self.App +=1
			self.App = self.App%6
			clearApps()
			time.sleep(1)
			self.startApp(self.App)
		

	def action(self):
		if self.sleep==0:
			#static ad
			if checkPixel( 533 , 47 , 0 , 0 , 0 ) and checkPixel( 726 , 46 , 0 , 0 , 0 ) and checkPixel( 852 , 43 , 68 , 68 , 68 ): click( 849 , 43 )
			if checkPixel( 845 , 56 , 68 , 68 , 68 ) and checkPixel( 843 , 50 , 242 , 242 , 242 ): click( 843 , 50 )	#****
			if checkPixel( 827 , 50 , 0 , 0 , 0 ) and checkPixel( 844 , 50 , 242 , 242 , 242 ): click( 844 , 50 )
			if checkPixel( 843 , 59 , 112 , 112 , 112 ) and checkPixel( 834 , 60 , 0 , 0 , 0 ) and checkPixel( 826 , 59 , 138 , 132 , 129 ): click( 832 , 59 )

			if checkPixel( 831 , 53 , 28 , 51 , 90 ) and checkPixel( 837 , 56 , 236 , 238 , 240 ): click( 837 , 56 )
			if checkPixel( 700 , 485 , 23 , 126 , 253 ) and checkPixel( 683 , 487 , 255 , 255 , 255 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )

			#clipcl@ps
			if checkPixel( 700 , 645 , 22 , 125 , 251 ) and checkPixel( 836 , 59 , 254 , 253 , 250 ): click( 835 , 58 )

			#snooker
			if checkPixel( 843 , 50 , 27 , 34 , 54 ) and checkPixel( 842 , 56 , 191 , 192 , 198 ): click( 842 , 56 )

			#bb4ll
			if checkPixel( 837 , 57 , 243 , 248 , 249 ): click( 837 , 57 )

			#glob2l
			if checkPixel( 842 , 57 , 242 , 219 , 201 ) and checkPixel( 837 , 57 , 231 , 187 , 154 )and not checkPixel(  845 , 56, 231 , 187 , 154 ): click( 837 , 57 )
			#speciAl
			if checkPixelOC( 842 , 56 , 200 , 200 , 200 ) and not checkPixelOC( 845 , 56 , 206 , 206 , 206 ): click( 838 , 56 )
			if checkPixel( 696 , 505 , 23 , 126 , 253 ) and checkPixelOC( 682 , 498 , 200 , 200 , 200 ) and checkPixelOC( 837 , 56 , 200 , 200 , 200 ): click( 837 , 56 )	#universl get right top closer
			if not checkPixelOC( 842 , 56 , 100 , 100 , 100 ) and checkPixelOC( 837 , 56 , 200 , 200 , 200 ) and not checkPixel( 832 , 56 , 100 , 100 , 100 ): click( 835 , 56 )	#cross
			# if checkPixelOC( 485 , 47 , 200 , 200 , 200 ) and not checkPixelOC( 490 , 48 , 200 , 200 , 200 ): click( 484 , 48 )
			# if checkPixelOC( 74 , 58 , 200 , 200 , 200 ) and not checkPixelOC( 82 , 57 , 200 , 200 , 200 ): click( 74 , 57 )
			if not checkPixelOC( 490 , 47 , 200 , 200 , 200 ) and checkPixelOC( 485 , 46 , 200 , 200 , 200 ) and not checkPixelOC( 479 , 46 , 200 , 200 , 200 ): click( 483 , 46 )
			if checkPixelOC( 832 , 78 , 250 , 250 , 250 ) and checkPixelOC( 835 , 61 , 250 , 250 , 250 ) and not checkPixelOC( 835 , 68 , 250 , 250 , 250 ): click( 834 , 61 )
			if not checkPixelOC( 84 , 58 , 200 , 200 , 200 ) and checkPixelOC( 74 , 57 ,200 , 200 , 200 ) and not checkPixelOC( 64 , 57 , 200 , 200 , 200 ): click( 76 , 59 )

			if not checkPixelOC( 505 , 101 , 200 , 200 , 200 ) and not checkPixelOC( 504 , 80 , 200 , 200 , 200 ) and checkPixelOC( 501 , 92 , 200 , 200 , 200 ) and not checkPixelOC( 517 , 91 , 200 , 200 , 200 ): click( 508 , 91 )
			if checkPixel( 845 , 53 , 5 , 9 , 9 ) and checkPixel( 839 , 53 , 246 , 246 , 246 ) and checkPixel( 831 , 52 , 3 , 9 , 9 ): click( 835 , 52 )

			#App lAuncher
			#multicc
			if checkPixel( 639 , 633 , 41 , 53 , 79 ) and checkPixel( 619 , 426 , 70 , 96 , 142 ) and checkPixel( 675 , 95 , 54 , 78 , 127 ):
				if self.App==1:click( 658 , 424 )
				if self.App==4:click( 798 , 421 )
			#multispce cc
			if checkPixel( 646 , 577 , 229 , 229 , 229 ) and checkPixel( 675 , 439 , 29 , 139 , 122 ) and checkPixel( 688 , 211 , 29 , 139 , 122 ):
				if self.App==2:click( 529 , 288 )
				if self.App==5:click( 660 , 285 )

			if checkPixel( 517 , 599 , 143 , 113 , 251 ) and checkPixel( 586 , 510 , 54 , 17 , 190 ) and checkPixel( 490 , 105 , 142 , 112 , 251 ) and checkPixel( 491 , 47 , 139 , 124 , 194 ): click( 485 , 48 )
			if (checkPixel(828, 136, 13, 59, 25) and checkPixel(572,620, 255, 255, 0) and checkPixel(832, 93, 48, 56, 65)):	#poker wala
				click(820, 91)
			if (checkPixel(828, 136, 13, 59, 25) and checkPixel(572,620, 255, 255, 0) and checkPixel(832, 93, 10, 40, 20)):
				click(820, 91)
			if checkPixel( 487 , 315 , 8 , 128 , 67 ) and checkPixel( 558 , 559 , 243 , 243 , 243 ) and checkPixel( 615 , 233 , 228 , 2 , 7 ) and checkPixel( 832 , 90 , 7 , 82 , 43 ):
				click( 826 , 91 )
			#hello kitty wala ball jharne
			if checkPixel( 488 , 640 , 0 , 14 , 40 ) and checkPixel( 825 , 151 , 102 , 247 , 249 ) and checkPixel( 481 , 46 , 111 , 186 , 190 ):click( 484 , 48 )
			#thulo kitty
			if checkPixel( 188 , 563 , 0 , 14 , 40 ) and checkPixel( 576 , 240 , 247 , 247 , 252 ) and checkPixel( 90 , 152 , 98 , 247 , 251 ) and checkPixel( 73 , 69 , 80 , 155 , 170 ): click( 74 , 58 )
			
			#taas wala play now ra re vako tala		
			if checkPixel( 550 , 535 , 18 , 133 , 29 ) and checkPixel( 802 , 659 , 255 , 255 , 255 ) and checkPixel( 837 , 64 , 10 , 67 , 14 ): 
				click( 838 , 56 )
				time.sleep(3)
				click( 838 , 56 )
			#matchington wala
			if checkPixel( 747 , 549 , 207 , 215 , 214 ) and checkPixel( 849 , 121 , 100 , 64 , 50 ) and checkPixel( 529 , 318 , 131 , 145 , 149 ) and checkPixel( 839 , 57 , 144 , 151 , 146 ): click( 839 , 57 )
			if checkPixel( 533 , 547 , 207 , 215 , 214 ) and checkPixel( 634 , 320 , 86 , 101 , 114 ) and checkPixel( 801 , 132 , 255 , 247 , 235 ) and checkPixel( 836 , 57 , 244 , 244 , 241 ): click( 836 , 57 )
			if checkPixel( 707 , 483 , 23 , 126 , 253 ) and checkPixel( 701 , 397 , 255 , 255 , 255 ) and checkPixel( 678 , 324 , 212 , 222 , 236 ) and checkPixel( 647 , 283 , 221 , 143 , 13 ) and checkPixel( 701 , 296 , 49 , 60 , 73 ) and checkPixel( 836 , 56 , 243 , 243 , 243 ): click( 836 , 56 )

			#thulo wala follower badhaune
			if checkPixel( 91 , 184 , 249 , 149 , 58 ) and checkPixel( 848 , 224 , 249 , 60 , 127 ) and checkPixel( 86 , 62 , 193 , 146 , 94 ): click( 74 , 59 )
			if checkPixel( 780 , 89 , 9 , 126 , 67 ) and checkPixel( 529 , 486 , 243 , 243 , 243 ) and checkPixel( 535 , 662 , 158 , 3 , 10 ) and checkPixel( 837 , 64 , 6 , 87 , 44 ): click( 837 , 55 )
			#second cross click
			if checkPixel( 498 , 388 , 20 , 79 , 49 ) and checkPixel( 537 , 658 , 108 , 67 , 68 ) and checkPixel( 694 , 474 , 23 , 126 , 253 ) and checkPixel( 843 , 55 , 24 , 58 , 40 ): click( 836 , 55 )
			#game wala tree rakhne
			if checkPixel( 483 , 48 , 213 , 243 , 254 ) and checkPixel( 765 , 656 , 238 , 223 , 200 ) and checkPixel( 848 , 116 , 218 , 199 , 185 ) and checkPixel( 839 , 61 , 233 , 238 , 239 ): click( 839 , 56 )
			if checkPixel( 824 , 514 , 175 , 134 , 106 ) and checkPixel( 739 , 426 , 110 , 95 , 54 ) and checkPixel( 857 , 214 , 200 , 172 , 150 ) and checkPixel( 843 , 54 , 191 , 199 , 202 ): click( 836 , 58 )
			if checkPixel( 631 , 484 , 23 , 126 , 253 ) and checkPixel( 648 , 283 , 231 , 163 , 19 ) and checkPixel( 678 , 251 , 9 , 203 , 217 ) and checkPixel( 711 , 308 , 51 , 99 , 140 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )
			if checkPixel( 841 , 349 , 104 , 96 , 84 ) and checkPixel( 706 , 476 , 23 , 126 , 253 ) and checkPixel( 623 , 123 , 113 , 102 , 88 ) and checkPixel( 830 , 56 , 99 , 103 , 105 ): click( 838 , 57 )
			#girl in computer ad
			if checkPixel( 531 , 457 , 99 , 165 , 185 ) and checkPixel( 647 , 420 , 21 , 40 , 70 ) and checkPixel( 634 , 336 , 15 , 30 , 60 ) and checkPixel( 836 , 51 , 68 , 68 , 68 ): click( 841 , 51 )
			#playstore quit garne
			if checkPixel( 496 , 89 , 95 , 99 , 104 ) and checkPixel( 524 , 89 , 255 , 255 , 255 ) and checkPixel( 838 , 84 , 109 , 113 , 117 ): click( 1351 , 644 )
			if checkPixel( 794 , 91 , 116 , 120 , 124 ) and checkPixel( 565 , 89 , 95 , 99 , 104 ) and checkPixel( 496 , 89 , 95 , 99 , 104 ) and checkPixel( 837 , 96 , 95 , 99 , 104 ): click( 1353 , 647 )
			#1945 Air force
			if checkPixel( 701 , 503 , 23 , 126 , 253 ) and checkPixel( 650 , 381 , 255 , 255 , 255 ) and checkPixel( 712 , 285 , 60 , 62 , 85 ) and checkPixel( 666 , 235 , 251 , 227 , 119 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )
			#sudoku wala
			#***
			if checkPixel( 830 , 57 , 204 , 204 , 204 ) and checkPixel( 843 , 57 , 243 , 243 , 243 ): click( 843 , 57 )
			if checkPixel( 636 , 505 , 23 , 126 , 252 ) and checkPixel( 664 , 501 , 255 , 255 , 255 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )
			if checkPixel( 696 , 505 , 23 , 126 , 253 ) and checkPixel( 683 , 499 , 255 , 255 , 255 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )
			#pubg
			if checkPixel( 64 , 60 , 105 , 114 , 126 ) and checkPixel( 74 , 67 , 104 , 113 , 125 ) and checkPixel( 74 , 49 , 105 , 113 , 123 ) and checkPixel( 74 , 58 , 249 , 250 , 250 ): click( 74 , 58 )
			if checkPixel( 84 , 59 , 145 , 148 , 150 ) and checkPixel( 74 , 58 , 251 , 251 , 251 ) and checkPixel( 65 , 57 , 149 , 153 , 154 ): click( 73 , 59 )

			#superhero
			if checkPixel( 832 , 57 , 119 , 179 , 204 ) and checkPixel( 836 , 57 , 240 , 247 , 249 ): click( 836 , 57 )
			if checkPixel( 704 , 492 , 23 , 126 , 253 ) and checkPixel( 682 , 480 , 255 , 255 , 255 ) and checkPixel( 837 , 56 , 255 , 255 , 255 ): click( 837 , 56 )


			if checkPixel( 745 , 167 , 255 , 255 , 255 ) and checkPixel( 767 , 218 , 234 , 238 , 248 ) and checkPixel( 840 , 65 , 204 , 204 , 204 ):
				click( 838 , 56 )
				time.sleep(1.5)
				click( 838 , 56 )
			if checkPixel( 578 , 679 , 236 , 48 , 33 ) and checkPixel( 717 , 59 , 143 , 143 , 143 ) and checkPixel( 766 , 63 , 0 , 0 , 0 ) and checkPixel( 801 , 566 , 52 , 104 , 215 ) and checkPixel( 832 , 54 , 0 , 0 , 0 ): click( 836 , 55 )
			if checkPixel( 636 , 518 , 23 , 126 , 253 ) and checkPixel( 670 , 282 , 48 , 93 , 188 ) and checkPixel( 702 , 248 , 255 , 255 , 255 ) and checkPixel( 841 , 54 , 36 , 36 , 36 ): click( 836 , 55 )
			if checkPixel( 516 , 581 , 143 , 143 , 143 ) and checkPixel( 628 , 522 , 23 , 126 , 253 ) and checkPixel( 665 , 265 , 52 , 72 , 97 ) and checkPixel( 830 , 54 , 105 , 105 , 105 ): click( 838 , 58 )	#same as above but without sleep. ie the second part
			if checkPixel( 675 , 280 , 178 , 223 , 254 ) and checkPixel( 702 , 512 , 23 , 126 , 253 ) and checkPixel( 709 , 639 , 41 , 84 , 134 ) and checkPixel( 831 , 57 , 104 , 104 , 104 ): click( 838 , 56 )
			#comics bob
			if checkPixel( 597 , 690 , 201 , 147 , 114 ) and checkPixel( 665 , 322 , 75 , 124 , 133 ) and checkPixel( 789 , 170 , 118 , 124 , 138 ) and checkPixel( 665 , 161 , 247 , 168 , 74 ) and checkPixel( 832 , 55 , 174 , 118 , 49 ): click( 837 , 55 )
			#machington wala
			if checkPixel( 479 , 522 , 222 , 182 , 145 ) and checkPixel( 784 , 552 , 239 , 62 , 79 ) and checkPixel( 831 , 57 , 129 , 75 , 28 ): click( 837 , 57 )
			if checkPixel( 626 , 492 , 23 , 126 , 253 ) and checkPixel( 523 , 400 , 255 , 255 , 255 ) and checkPixel( 712 , 310 , 61 , 103 , 147 ) and checkPixel( 647 , 285 , 227 , 154 , 16 ) and checkPixel( 632 , 279 , 94 , 126 , 140 ) and checkPixel( 679 , 251 , 8 , 208 , 221 ) and checkPixel( 844 , 56 , 70 , 48 , 32 ): click( 837 , 56 )
			#en4
			if checkPixel( 700 , 490 , 23 , 126 , 253 ) and checkPixel( 588 , 406 , 255 , 255 , 255 ) and checkPixel( 674 , 260 , 0 , 207 , 194 ) and checkPixel( 702 , 325 , 239 , 169 , 149 ) and checkPixel( 628 , 316 , 155 , 47 , 52 ) and checkPixel( 836 , 56 , 244 , 242 , 240 ): click( 836 , 56 )
			#cAr drAW
			if checkPixel( 760 , 599 , 246 , 0 , 0 ) and checkPixel( 566 , 596 , 0 , 97 , 255 ) and checkPixel( 836 , 206 , 137 , 137 , 137 ) and checkPixel( 820 , 52 , 139 , 139 , 139 ) and checkPixel( 834 , 54 , 231 , 231 , 231 ): click( 834 , 54 )
			if checkPixel( 630 , 326 , 46 , 148 , 255 ) and checkPixel( 658 , 398 , 255 , 255 , 255 ) and checkPixel( 626 , 496 , 23 , 126 , 253 ) and checkPixel( 676 , 314 , 255 , 175 , 0 ) and checkPixel( 837 , 56 , 255 , 255 , 255 ):click( 837 , 56 )
			#bll gu4kune
			if checkPixel( 526 , 686 , 255 , 255 , 255 ) and checkPixel( 507 , 103 , 16 , 185 , 250 ) and checkPixel( 509 , 80 , 234 , 20 , 7 ) and checkPixel( 530 , 67 , 237 , 170 , 9 ) and checkPixel( 836 , 57 , 235 , 246 , 249 ): click( 836 , 57 )
			if checkPixel( 692 , 497 , 23 , 126 , 253 ) and checkPixel( 576 , 404 , 255 , 255 , 255 ) and checkPixel( 616 , 299 , 255 , 255 , 255 ) and checkPixel( 629 , 300 , 0 , 0 , 254 ) and checkPixel( 643 , 311 , 254 , 0 , 206 ) and checkPixel( 843 , 56 , 54 , 93 , 105 ): click( 837 , 56 )

			#AlloW youtube in ply store
			if checkPixel( 712 , 89 , 102 , 102 , 102 ) and checkPixel( 612 , 463 , 255 , 255 , 255 ) and checkPixel( 775 , 442 , 1 , 135 , 95 ) and checkPixel( 626 , 82 , 38 , 40 , 42 ):
				click( 1349 , 714 )
				click( 1349 , 714 )
				
			#quick closer
			if not checkPixelOC( 833 , 92 , 100 , 100 , 100 ) and checkPixelOC( 825 , 92 , 250 , 250 , 250 ) and not checkPixelOC( 817 , 92 , 100 , 100 , 100 ): click( 824 , 92 )
			if not checkPixelOC( 832 , 93 , 200 , 200 , 200 ) and checkPixelOC( 825 , 93 , 240 , 240 , 240 ) and not checkPixel( 816 , 93 , 200 , 200 , 200 ): click( 825 , 92 )

			#pubg ll
			if checkPixelOC( 74 , 58 , 200 , 200, 200 ) and not checkPixelOC( 67 , 57 , 100 , 100 , 100 ) and not checkPixel( 79 , 58 , 100 , 100 , 100 ): click( 73 , 57 )

			#crocodile game
			if checkPixel( 716 , 687 , 239 , 105 , 52 ) and checkPixel( 519 , 702 , 116 , 222 , 174 ) and checkPixel( 502 , 706 , 235 , 227 , 198 ) and checkPixel( 831 , 58 , 135 , 129 , 102 ): click( 837 , 58 )
			if checkPixel( 702 , 311 , 117 , 222 , 175 ) and checkPixel( 671 , 328 , 244 , 230 , 205 ) and checkPixel( 661 , 276 , 203 , 154 , 147 ) and checkPixel( 699 , 491 , 23 , 126 , 253 ) and checkPixel( 845 , 55 , 77 , 74 , 63 ): click( 834 , 57 )
			if checkPixel( 553 , 580 , 255 , 96 , 49 ) and checkPixel( 822 , 376 , 223 , 218 , 182 ) and checkPixel( 618 , 262 , 128 , 232 , 55 ) and checkPixel( 811 , 72 , 169 , 161 , 127 ) and checkPixel( 829 , 56 , 135 , 129 , 102 ): click( 836 , 55 )
			#take apart gme
			if checkPixel( 482 , 648 , 56 , 79 , 118 ) and checkPixel( 549 , 518 , 255 , 255 , 255 ) and checkPixel( 606 , 512 , 1 , 135 , 95 ) and checkPixel( 817 , 52 , 235 , 235 , 235 ) and checkPixel( 832 , 54 , 23 , 23 , 23 ): click( 838 , 54 )
			#ECER only	
			if checkPixel( 682 , 274 , 1 , 1 , 255 ) and checkPixel( 744 , 264 , 255 , 255 , 255 ) and checkPixel( 496 , 65 , 68 , 195 , 96 ) and checkPixel( 852 , 49 , 68 , 68 , 68 ): click( 844 , 50 )
			#ecer red girl
			if checkPixel( 588 , 691 , 58 , 120 , 231 ) and checkPixel( 557 , 382 , 241 , 0 , 35 ) and checkPixel( 717 , 181 , 243 , 215 , 201 ) and checkPixel( 843 , 55 , 195 , 195 , 190 ): click( 843 , 51 )
			if checkPixel( 498 , 89 , 60 , 64 , 67 ) and checkPixel( 782 , 88 , 60 , 64 , 67 ) and checkPixel( 836 , 82 , 60 , 64 , 67 ) and checkPixel( 660 , 96 , 255 , 255 , 255 ): click( 1348 , 635 )
			if checkPixel( 692 , 497 , 23 , 126 , 253 ) and checkPixel( 576 , 404 , 255 , 255 , 255 ) and checkPixel( 616 , 299 , 255 , 255 , 255 ) and checkPixel( 629 , 300 , 0 , 0 , 254 ) and checkPixel( 643 , 311 , 254 , 0 , 206 ) and checkPixel( 843 , 56 , 54 , 93 , 105 ): click( 837 , 56 )
			if checkPixel( 603 , 698 , 58 , 120 , 231 ) and checkPixel( 525 , 702 , 238 , 238 , 238 ) and checkPixel( 855 , 72 , 253 , 253 , 243 ) and checkPixel( 844 , 56 , 195 , 195 , 190 ): click( 844 , 52 )
			#solitiare wala
			#BEST
			if checkPixel( 573 , 615 , 255 , 253 , 0 ) and checkPixel( 609 , 607 , 0 , 1 , 1 ) and checkPixel( 837 , 72 , 248 , 249 , 249 ): click( 837 , 72 )
			if checkPixel( 630 , 469 , 23 , 126 , 253 ) and checkPixel( 645 , 469 , 255 , 255 , 255 ) and checkPixel( 838 , 56 , 255 , 255 , 255 ): click( 838 , 56 )
			if checkPixel( 826 , 93 , 255 , 255 , 255 ) and checkPixel( 833 , 93 , 175 , 175 , 175 ): click( 826 , 93 )

			if checkPixel( 832 , 56 , 7 , 92 , 49 ) and checkPixel( 837 , 57 , 229 , 238 , 233 ): click( 839 , 57 )

			if checkPixel( 803 , 658 , 255 , 255 , 255 ) and checkPixel( 836 , 427 , 15 , 123 , 24 ) and checkPixel( 829 , 193 , 219 , 142 , 14 ) and checkPixel( 837 , 65 , 9 , 66 , 13 ): click( 837 , 54 )
			if checkPixel( 703 , 522 , 23 , 126 , 253 ) and checkPixel( 759 , 570 , 23 , 80 , 28 ) and checkPixel( 742 , 110 , 22 , 66 , 26 ) and checkPixel( 842 , 55 , 40 , 58 , 41 ): click( 837 , 55 )
			if checkPixel( 574 , 627 , 254 , 251 , 0 ) and checkPixel( 803 , 415 , 11 , 110 , 56 ) and checkPixel( 792 , 120 , 13 , 71 , 30 ) and checkPixel( 815 , 90 , 10 , 48 , 21 ): click( 824 , 91 )
			if checkPixel( 701 , 69 , 3 , 62 , 32 ) and checkPixel( 603 , 67 , 8 , 118 , 60 ) and checkPixel( 587 , 66 , 3 , 55 , 28 ) and checkPixel( 835 , 93 , 5 , 82 , 42 ): click( 827 , 93 )
			if checkPixel( 626 , 510 , 23 , 126 , 253 ) and checkPixel( 667 , 289 , 203 , 37 , 25 ) and checkPixel( 635 , 253 , 255 , 255 , 255 ) and checkPixel( 661 , 235 , 28 , 165 , 19 ) and checkPixel( 844 , 56 , 38 , 57 , 40 ): click( 839 , 56 )
			#DNA evolution
			if checkPixel( 707 , 484 , 23 , 126 , 253 ) and checkPixel( 688 , 319 , 91 , 251 , 253 ) and checkPixel( 679 , 298 , 219 , 38 , 33 ) and checkPixel( 640 , 268 , 255 , 212 , 0 ) and checkPixel( 838 , 57 , 246 , 246 , 247 ): click( 838 , 57 )
			if checkPixel( 773 , 674 , 154 , 54 , 214 ) and checkPixel( 515 , 678 , 182 , 54 , 255 ) and checkPixel( 507 , 691 , 0 , 215 , 254 ) and checkPixel( 845 , 55 , 139 , 166 , 203 ): click( 838 , 56 )
			if checkPixel( 623 , 234 , 174 , 54 , 255 ) and checkPixel( 724 , 170 , 177 , 48 , 255 ) and checkPixel( 680 , 176 , 0 , 227 , 253 ) and checkPixel( 685 , 196 , 207 , 28 , 23 ) and checkPixel( 831 , 56 , 74 , 102 , 186 ): click( 838 , 57 )
			if checkPixel( 623 , 335 , 173 , 53 , 255 ) and checkPixel( 713 , 290 , 177 , 49 , 255 ) and checkPixel( 701 , 259 , 168 , 42 , 255 ) and checkPixel( 677 , 301 , 199 , 20 , 15 ) and checkPixel( 831 , 55 , 51 , 63 , 97 ): click( 836 , 55 )
			#Mario
			if checkPixel( 123 , 96 , 103 , 217 , 216 ) and checkPixel( 1133 , 375 , 68 , 152 , 152 ) and checkPixel( 1124 , 647 , 194 , 99 , 4 ) and checkPixel( 589 , 682 , 71 , 211 , 201 ) and checkPixel( 395 , 67 , 101 , 254 , 163 ) and checkPixel( 84 , 58 , 85 , 85 , 84 ): click( 74 , 58 )
			#bottle water transfer game
			if checkPixel( 736 , 647 , 254 , 223 , 221 ) and checkPixel( 706 , 431 , 71 , 69 , 72 ) and checkPixel( 628 , 241 , 79 , 79 , 72 ) and checkPixel( 744 , 238 , 254 , 223 , 221 ) and checkPixel( 492 , 47 , 195 , 180 , 179 ): click( 485 , 49 )
			if checkPixel( 491 , 46 , 195 , 180 , 179 ) and checkPixel( 711 , 430 , 77 , 77 , 79 ) and checkPixel( 621 , 239 , 91 , 81 , 81 ): click( 487 , 48 )
			#stAte.io
			if checkPixel( 712 , 538 , 105 , 15 , 0 ) and checkPixel( 763 , 160 , 214 , 65 , 66 ) and checkPixel( 828 , 110 , 89 , 89 , 89 ) and checkPixel( 830 , 54 , 84 , 84 , 84 ): click( 837 , 56 )	
			if checkPixel( 632 , 508 , 23 , 126 , 253 ) and checkPixel( 709 , 309 , 242 , 110 , 110 ) and checkPixel( 666 , 267 , 100 , 174 , 229 ) and checkPixel( 842 , 54 , 56 , 56 , 56 ): click( 836 , 55 )
			if checkPixel( 781 , 673 , 134 , 92 , 99 ) and checkPixel( 517 , 160 , 253 , 157 , 74 ) and checkPixel( 647 , 313 , 208 , 154 , 145 ) and checkPixel( 830 , 55 , 70 , 64 , 73 ): click( 835 , 55 )
			if checkPixel( 707 , 491 , 23 , 126 , 253 ) and checkPixel( 767 , 666 , 83 , 62 , 65 ) and checkPixel( 507 , 191 , 125 , 89 , 54 ) and checkPixel( 794 , 87 , 60 , 56 , 61 ) and checkPixel( 842 , 54 , 50 , 47 , 51 ): click( 836 , 55 )
			#indiAn clling App
			if checkPixel( 711 , 539 , 255 , 235 , 58 ) and checkPixel( 599 , 349 , 0 , 4 , 1 ) and checkPixel( 155 , 68 , 26 , 93 , 30 ) and checkPixel( 73 , 68 , 68 , 68 , 68 ): click( 73 , 68 )

			#close chrome
			if checkPixel( 491 , 95 , 60 , 64 , 67 ) and checkPixel( 547 , 72 , 241 , 243 , 244 ) and checkPixel( 740 , 74 , 241 , 243 , 244 ) and checkPixel( 826 , 85 , 210 , 63 , 49 ): click( 1351 , 646 )
			
			print("..")	
			time.sleep(.2)
			return True
		else:
			print("sleeping")
			return False

def main():
	tabtimer = time.time()+30;

	nowTime1 = 0.0
	# phone1 = phone("1shanko1", "started")
	phone1 = phone("bluestacks 24", "started")	
	while True:
		# if time.time()>tabtimer: alttab(1)
		# if keyboard.is_pressed("alt"): tabtimer = time.time()+20
		while True:#active_window()==phone1.name:
			phone1.overlord()
			phone1.action()
		# while active_window()==phone2.name:
		# 	phone2.overlord()
		# 	phone2.action()

main()
#memory
#813,253 241,0,32 and 740,56 256,173,16 and 848,69 252,253,248 >>>> 845,50
#828,136 13,59,25 and 572,620 255,255,0
