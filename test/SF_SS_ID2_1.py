import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/src')
from Motor import Controller
import RPi.GPIO as GPIO

if __name__ == '__main__':
    controller = Controller(gyro_address=0x68, gpio_trigger=20, gpio_echo=21)
    try:
        controller.forward(0.5, 100)
    except KeyboardInterrupt:
        controller.stop()
        GPIO.cleanup()
