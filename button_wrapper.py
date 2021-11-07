import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread
from datetime import datetime
import motor
import os

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(target = wrapper, args = (5,action_motor))
    thread_button_2 = Thread(target = wrapper, args = (2,apply_reboot))

    thread_button_1.start()
    thread_button_2.start()
    print("[button_wrapper] Launch Thread function")

def wrapper(gpio_number, function):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            function()

def action_motor():
    motor.steps(-300)
    motor.steps(300)

def apply_reboot():
    print("REBOOT")
    os.system("sudo reboot")
