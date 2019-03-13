import random
import time
import json
import requests
from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
	
response = requests.get("https://randomuser.me/api/?results=10").content

data = json.loads(response)

x = 3
y = 3

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right


#while(1):
for y in range(0,10):
	
	temp = data['results'][y]['name']['first']
	sense.show_message(temp, text_colour=[255,0,0])
	event = sense.stick.wait_for_event()
	#LIKE
	if event.direction == sense.stick.direction_left:
		sense.set_pixel(0, 0, 0, 255, 0)
		sleep(1)
		sense.clear()
	#DISLIKE
	if event.direction == sense.stick.direction_right:
		sense.set_pixel(0, 0, 255, 0, 0)
		sleep(1)
		sense.clear()

	





