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
import time,json

# Import the ArmRobot.py file (must be in the same directory as this file!).
import driver
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.escape

servoMin = 150  # Min pulse length out of 4096  #150
servoMax = 600  # Max pulse length out of 4096 #600
motor = driver.MotorDriver()
c = 0


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
        print 'eventType:', c
        if c == 8:
            print "Running Forward"
            motor.t_up(100, 0)
        elif c == 2:
            print "Running Reverse"
            motor.t_down(100, 0)
        elif c == 4:
            print "Turning Right"
            motor.t_right(80, 0)
        elif c == 6:
            print "Turning Left"
            motor.t_left(80, 0)
        elif c == 5:
            print "Stopped"
            motor.t_stop(0)    # Stop the robot from moving.
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


if __name__ == '__main__':
    running = True
    thread1 = myThread(1, "Thread-1", 1)
    thread1.setDaemon(True)
    thread1.start()
    application.listen(9093)          	# starts the websockets connection
    tornado.ioloop.IOLoop.instance().start()
