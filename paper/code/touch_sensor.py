# Source: https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# Source2: https://stackoverflow.com/questions/16143842/raspberry-pi-gpio-events-in-python

import RPi.GPIO as GPIO
import time


class touch_sensor(object):
	"""docstring for touch_sensor"""
	def __init__(self, pin=7, pin_setup='BOARD'):
		self.pin = pin
		if pin_setup == 'BCM':
			GPIO.setmode(GPIO.BCM)
		else:
			GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.pin,GPIO.IN)
		GPIO.remove_event_detect(self.pin)
		GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.touch_callback)
		self.display_num = 1
		
	def touch_callback(self, channel):
		if self.display_num == 1:
			if GPIO.input(self.pin) == 1:
				self.display_num = 0
			else:
				self.display_num = 1
		else:
			if GPIO.input(self.pin) == 1:
				self.display_num = 1
			else:
				self.display_num = 0
		
	def return_state(self):
		return self.display_num

while True:
	time.sleep(1)
	print(touch_sensor(pin=13).return_state())