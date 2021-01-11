from pyPS4Controller.controller import Controller
from gpiozero import PWMLED
from picamera import PiCamera
from time import sleep, time
import signal
import sys

led = PWMLED(4)
brightnessValue = 1
components = ["LED", "Camera"]
index = 0
camera = PiCamera()
camera.resolution = (2560,1936)
getMilliSeconds = lambda: int(round(time() * 1000))

class MyController(Controller):
	def __init__(self, ** kwargs):
		Controller.__init__(self, ** kwargs)

	def on_x_press(self):
		if index == 0:
			led.value = brightnessValue
		elif index == 1:
			camera.capture(f"{getMilliSeconds()}.jpg")

	def on_circle_press(self):
		if index == 0:
			led.value = 0
		else:
			print(f"Plese Change to LED by using R1 or L1. {components[index]} is selected now.")

	def on_up_arrow_press(self):
		if index == 0:
			global brightnessValue 
			brightnessValue = min((brightnessValue + 0.1), 1)
			led.value = brightnessValue
		else:
			camera.vflip = True

	def on_down_arrow_press(self):
		if index == 0:
			global brightnessValue
			brightnessValue = max((brightnessValue - 0.1), 0)
			led.value = brightnessValue
		else:
			camera.vflip = True

	def on_right_arrow_press(self):
		if index == 0:
			print(f"Plese Change to CAMERA by using R1 or L1. {components[index]} is selected now.")
		else:
			camera.hflip = True

	def on_left_arrow_press(self):
		if index == 0:
			print(f"Plese Change to CAMERA by using R1 or L1. {components[index]} is selected now.")
		else:
			camera.hflip = True

	def on_R1_press(self):
		global index
		if index == (len(components) - 1):
			index = 0
		else:
			index += 1
		print(f"{components[index]} is selected.")

	def on_L1_press(self):
		global index
		if index == 0:
			index = len(components) - 1
		else:
			index -= 1	
		print(f"{components[index]} is selected.")

def signal_handler(sig, frame):
	camera.close()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
controller = MyController(interface = "/dev/input/js0", connecting_using_ds4drv = False)
controller.listen()
