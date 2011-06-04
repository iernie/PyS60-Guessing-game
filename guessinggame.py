# Made by Ernie (ernsgamerzone.com), 2008
# This software is licensed under the CC-GNU GPL: http://creativecommons.org/licenses/GPL/2.0/
# Version 0.1.2 (build 2)

import appuifw
import e32
import random

running = 1

a = 0
b = 10

def quit():
    appuifw.app.set_exit()

while running == 1:

	appuifw.app.title = u"Guessing Game"

	appuifw.app.screen='normal'

	L = [u"Start", u"Settings", u"About", u"Exit"]

	index = appuifw.selection_list(choices=L , search_field=0)

	if index == 0:

		number = random.randint(a, b)
		tries = 1
		thetry = -1

		while thetry != number:

			thetry = appuifw.query(u"Guess the number:", "number")

			if thetry > number:
				appuifw.note(u"Too high, try again", "error")
				tries = tries + 1
	
			if thetry < number:
				appuifw.note(u"Too low, try again", "error")
				tries = tries + 1

			if thetry == number:
				break

		appuifw.note(u"Victory!", "conf")
		appuifw.note(u"Right number was: " + number, "info")
		appuifw.note(u"Number of tries are " + tries, "info")
		appuifw.note(u"Thanks for playing!", "info")

	elif index == 1:
		data1,data2 = appuifw.multi_query(u"From",u"To")
		a = int(data1)
		b = int(data2)

	elif index == 2:
		appuifw.note(u"This game is made by Ernie using Python!", "info")

	elif index == 3:
		app.exit_key_handler=quit
