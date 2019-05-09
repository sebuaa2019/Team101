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
import time,sys,json

# Import the ArmRobot.py file (must be in the same directory as this file!).
import RPi.GPIO as GPIO  
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.escape

servoMin = 150  # Min pulse length out of 4096  #150
servoMax = 600  # Max pulse length out of 4096 #600

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24


def t_up(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)   # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)   # BIN1
    time.sleep(t_time)


def t_stop(t_time):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_down(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)   # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)   # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_left(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)   # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)   # BIN1
    time.sleep(t_time)


def t_right(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)   # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)   # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


c = 0
# Initialize TOrnado to use 'GET' and load index.html


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())


# Code for handling the data sent from the webpage
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'connection opened...'

    def on_message(self, message):      # receives the data from the webpage and is stored in the variable message
        global c
        print 'received:', message        # prints the revived from the webpage
        decodejson = json.loads(message)
        c=decodejson['eventType']
        v=decodejson['eventValue']
        print 'eventType:',c
        if c == 6 :
            print "Running Forward"
            t_up(100,0)
        elif c == 4 :
            print "Running Reverse"
            t_down(100,0)
        elif c == 8 :
            print "Turning Right"
            t_right(80,0)
        elif c == 2 :
            print "Turning Left"
            t_left(80,0)
        elif c == 5 :
            print "Stopped"
            t_stop(0)    # Stop the robot from moving.
        print "Values Updated"

    def on_close(self):
        # robot.stop()      # Stop the robot from moving.
        print 'connection closed...'


application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Ready"
        while running:
            time.sleep(.2)              # sleep for 200 ms


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)

    L_Motor= GPIO.PWM(PWMA, 100)
    L_Motor.start(0)
    R_Motor = GPIO.PWM(PWMB, 100)
    R_Motor.start(0)

    # pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
    running = True
    thread1 = myThread(1, "Thread-1", 1)
    thread1.setDaemon(True)
    thread1.start()
    application.listen(9093)          	# starts the websockets connection
    tornado.ioloop.IOLoop.instance().start()
  

