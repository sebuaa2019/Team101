################################################################################################################
# PREREQUISITES
# Tornado Web Server for Python
#
# TROUBLESHOOTING:
# Don't use Ctrl+Z to stop the program, use Ctrl+c.
# If you use Ctrl+Z, it will not close the socket and you won't be able to run the program the next time.
# If you get the following error:
# "socket.error: [Errno 98] Address already in use "
# Run this on the terminal:
# "sudo netstat -ap |grep :9093"
# Note down the PID of the process running it
# And kill that process using:
# "kill pid"
# If it does not work use:
# "kill -9 pid"
# If the error does not go away, try changin the port number '9093' both in the client and server code
import time

# Import the ArmRobot.py file (must be in the same directory as this file!).
import RPi.GPIO as GPIO


class MotorDriver:
    def __init__(self):
        self.__PWMA = 18
        self.__AIN1 = 22
        self.__AIN2 = 27

        self.__PWMB = 23
        self.__BIN1 = 25
        self.__BIN2 = 24

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
        GPIO.setup(self.__AIN2, GPIO.OUT)
        GPIO.setup(self.__AIN1, GPIO.OUT)
        GPIO.setup(self.__PWMA, GPIO.OUT)

        GPIO.setup(self.__BIN1, GPIO.OUT)
        GPIO.setup(self.__BIN2, GPIO.OUT)
        GPIO.setup(self.__PWMB, GPIO.OUT)

        self.__L_Motor = GPIO.PWM(self.__PWMA, 100)
        self.__R_Motor = GPIO.PWM(self.__PWMB, 100)
        self.__L_Motor.start(0)
        self.__R_Motor.start(0)

    def t_up(self, speed, t_time):
        self.__L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__AIN2, False)  # AIN2
        GPIO.output(self.__AIN1, True)  # AIN1

        self.__R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__BIN2, True)  # BIN2
        GPIO.output(self.__BIN1, False)  # BIN1
        time.sleep(t_time)

    def t_stop(self, t_time):
        self.__L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.__AIN2, False)  # AIN2
        GPIO.output(self.__AIN1, False)  # AIN1

        self.__R_Motor.ChangeDutyCycle(0)
        GPIO.output(self.__BIN2, False)  # BIN2
        GPIO.output(self.__BIN1, False)  # BIN1
        time.sleep(t_time)

    def t_down(self, speed, t_time):
        self.__L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__AIN2, True)  # AIN2
        GPIO.output(self.__AIN1, False)  # AIN1

        self.__R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__BIN2, False)  # BIN2
        GPIO.output(self.__BIN1, True)  # BIN1
        time.sleep(t_time)

    def t_left(self, speed, t_time):
        self.__L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__AIN2, False)  # AIN2
        GPIO.output(self.__AIN1, True)  # AIN1

        self.__R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__BIN2, False)  # BIN2
        GPIO.output(self.__BIN1, True)  # BIN1
        time.sleep(t_time)

    def t_right(self, speed, t_time):
        self.__L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__AIN2, True)  # AIN2
        GPIO.output(self.__AIN1, False)  # AIN1

        self.__R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.__BIN2, True)  # BIN2
        GPIO.output(self.__BIN1, False)  # BIN1
        time.sleep(t_time)
