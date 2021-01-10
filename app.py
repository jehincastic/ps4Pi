from pyPS4Controller.controller import Controller
from gpiozero import PWMLED
from time import sleep

led = PWMLED(4)
brightnessValue = 1

class MyController(Controller):
	def __init__(self, ** kwargs):
		Controller.__init__(self, ** kwargs)

	def on_x_press(self):
		led.value = brightnessValue

	def on_circle_press(self):
		led.value = 0

	def on_up_arrow_press(self):
		global brightnessValue 
		brightnessValue = min((brightnessValue + 0.1), 1)
		led.value = brightnessValue

	def on_down_arrow_press(self):
		global brightnessValue
		brightnessValue = max((brightnessValue - 0.1), 0)
		led.value = brightnessValue

controller = MyController(interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen()
