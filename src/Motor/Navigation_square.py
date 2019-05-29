# coding=utf-8
# import Controller
# import RPi.GPIO as GPIO
import yaml
import logging.config
import os
import time
import random
import math


# 植株绝对位置
# 小车初始应位于0号田垄中，朝向超前
# 小车超声波雷达朝向后方
plants = [[0.34, 0.70, 1.02, 1.30, 1.62],
          [0.30, 0.68, 1.05, 1.32, 1.60],
          [0.33, 0.68, 1.10, 1.27, 1.58],
          [0.31, 0.72, 1.06, 1.26, 1.61],
          [0.32, 0.69, 1.08, 1.29, 1.60]]
ravine = [0.15, 0.73, 1.35, 1.92, 2.47]
'''
                     PLANTS
R   |=======================================
    |Plant00 Plant01 Plant02 Plant03 Plant04
A   |=======================================
    |Plant10 Plant11 Plant12 Plant13 Plant14
V   |=======================================
    |Plant20 Plant21 Plant22 Plant23 Plant24
I   |=======================================
    |Plant30 Plant31 Plant32 Plant33 Plant34
N   |=======================================
    |Plant40 Plant41 Plant42 Plant43 Plant44
E   |=======================================
'''
car_length = 0.19           # 小车雷达到中心的距离

car_id = 0
car_state = {'location': [0, 0],
             'battery': 7.8,
             'mileage': 0}


def logger(log_level, car_event, information):
    if log_level == "INFO":
        logging.info("Car%d (%d, %d)-%.2f-%.2f %s %s" % (car_id,
                                                         car_state['location'][0],
                                                         car_state['location'][1],
                                                         car_state['battery'],
                                                         car_state['mileage'],
                                                         car_event,
                                                         information))
    elif log_level == "WARNING":
        logging.warning("Car%d (%d, %d)-%.2f-%.2f %s %s" % (car_id,
                                                            car_state['location'][0],
                                                            car_state['location'][1],
                                                            car_state['battery'],
                                                            car_state['mileage'],
                                                            car_event,
                                                            information))
    elif log_level == "ERROR":
        logging.error("Car%d (%d, %d)-%.2f-%.2f %s %s" % (car_id,
                                                          car_state['location'][0],
                                                          car_state['location'][1],
                                                          car_state['battery'],
                                                          car_state['mileage'],
                                                          car_event,
                                                          information))
    else:
        return


def setup_logging(default_path="logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


class Controller:
    def __init__(self, gyro_address, gpio_trigger, gpio_echo):
        self.gyro_address = gyro_address
        self.gpio_trigger = gpio_trigger
        self.gpio_echo = gpio_echo

    def t_up(self, vel, t_time):
        time.sleep(t_time)

    def t_left(self, vel, t_time):
        time.sleep(t_time)

    def t_right(self, vel, t_time):
        time.sleep(t_time)

    def t_down(self, vel, t_time):
        time.sleep(t_time)

    def t_stop(self, t_time):
        time.sleep(t_time)

    def getLoc(self):
        return 0

    def forward(self, length, speed, end_time=0.0):
        length = math.fabs(length)
        car_state['mileage'] += length
        car_state['battery'] -= length * 0.005
        time.sleep(length/0.1+end_time+random.random())

    def backward(self, length, speed, end_time=0.0):
        length = math.fabs(length)
        car_state['mileage'] += length
        car_state['battery'] -= length * 0.005
        time.sleep(length/0.1+end_time+random.random())

    def turnRight(self, angle, speed, end_time=0.0):
        car_state['battery'] -= angle * 0.00001
        time.sleep(2+end_time+random.random())

    def turnLeft(self, angle, speed, end_time=0.0):
        car_state['battery'] -= angle * 0.00001
        time.sleep(2+end_time+random.random())

    def stop(self):
        return


def operate():
    if random.random() > 0.05:
        logger("INFO", "WORKING-IRRIGATE", "\"Execute irrigation mission.\"")
    else:
        logger("INFO", "WORKING-WEED", "\"Execute weeding mission.\"")
    time.sleep(5 + 10 * random.random())
    pass


def check_state():
    if car_state['battery'] < 1.5:
        logger("WARNING", "MOVING", "\"Low battery! Need charging.\"")
    if car_state['battery'] < 1.0:
        logger("ERROR", "HANG_UP", "\"Battery runs out.\"")
        raise KeyboardInterrupt


if __name__ == '__main__':
    setup_logging(default_path="logging.yaml")
    logger("INFO", "SLEEP", "\"Initialize car...\"")
    car = Controller(gyro_address=0x68, gpio_trigger=20, gpio_echo=21)
    logger("INFO", "WAIT", "\"Initialize successfully.\"")

    try:
        while True:
            for i in range(len(plants)):
                check_state()
                start_point = car.getLoc()
                current_location = start_point
                for j in range(len(plants[i])):
                    logger("INFO", "MOVING", "\"Move to plant[%d, %d].\"" % (i, j))
                    car.forward(plants[i][j]-current_location, 100, end_time=0.2)
                    car_state['location'] = [i, j]
                    logger("INFO", "MOVING", "\"Turn to plant[%d, %d].\"" % (i, j))
                    car.turnRight(90, 60, end_time=0.2)
                    operate()
                    logger("INFO", "MOVING", "\"Turn back from plant[%d, %d].\"" % (i, j))
                    car.turnLeft(90, 60, end_time=0.2)
                    current_location = car.getLoc()
                logger("INFO", "MOVING", "\"Back to the entrance of ravine[%d].\"" % i)
                car.backward(current_location-start_point, 100, 0.2)
                car_state['location'] = [i, 0]
                logger("INFO", "MOVING", "\"Turn to the ravine channel.\"")
                car.turnRight(90, 60, end_time=0.2)
                current_location = car.getLoc()
                if i != len(plants)-1:
                    logger("INFO", "MOVING", "\"Move to ravine[%d].\"" % (i+1))
                    car.forward(ravine[i+1]-current_location, 100, 0.2)
                else:
                    logger("INFO", "MOVING", "\"Back to ravine[0].\"")
                    car.backward(current_location-ravine[0], 100, 0.2)
                car_state['location'] = [(i+1) % len(ravine), 0]
                logger("INFO", "MOVING", "\"Turn into ravine[%d].\"" % ((i+1) % len(ravine)))
                car.turnLeft(90, 60, 0.2)

    except KeyboardInterrupt:
        car.stop()
        # GPIO.cleanup()



