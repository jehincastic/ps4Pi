from pyPS4Controller.controller import Controller
from gpiozero import LED
from time import sleep

led = LED(4)

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        led.on()

    def on_circle_press(self):
        led.off()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

