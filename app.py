from pyPS4Controller.controller import Controller
from gpiozero import LED
from time import sleep

led = LED(4)
brightnessValue = 1
maxValue = 32767

class MyController(Controller):
	def __init__(self, ** kwargs):
		Controller.__init__(self, ** kwargs)

def on_x_press(self):
	led.value = brightnessValue

def on_circle_press(self):
	brightnessValue = 0
	led.value = brightnessValue

def on_L3_up(self, value):
	brightnessValue = abs(value) / maxValue
	led.value = brightnessValue

controller = MyController(interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen()
