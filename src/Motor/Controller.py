# coding=utf-8
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Sensor import GyroscopeDriver as Gyro
from Sensor import UltrasonicDriver as UltraS
from Driver import MotorDriver
import time
import math
import RPi.GPIO as GPIO


class Controller:
    def __init__(self, gyro_address=0x68, gpio_trigger=20, gpio_echo=21):
        self.motor = MotorDriver.MotorDriver()
        self.mpu = Gyro.GyroscopeDriver(gyro_address)
        self.mpu_freq = 0.05
        self.ultraS = UltraS.UltrasonicDriver(gpio_trigger, gpio_echo)
        self.ultraS_freq = 0.1

    def getLoc(self):
        return self.ultraS.distance()

    # end_time 表示动作完成后暂停时间，为0表示不暂停
    def forward(self, length, speed, end_time=0):
        start_loc = self.ultraS.distance()
        self.motor.t_up(speed, 0)
        while True:
            begin_time = time.time()
            current_loc = self.ultraS.distance()
            if math.fabs(current_loc-start_loc) >= length:
                self.motor.t_stop(end_time)
                break
            passed_time = time.time()-begin_time
            time.sleep(self.ultraS_freq-passed_time)

    def backward(self, length, speed, end_time=0):
        start_loc = self.ultraS.distance()
        self.motor.t_down(speed, 0)
        while True:
            begin_time = time.time()
            current_loc = self.ultraS.distance()
            if math.fabs(current_loc-start_loc) >= length:
                self.motor.t_stop(end_time)
                break
            passed_time = time.time()-begin_time
            time.sleep(self.ultraS_freq-passed_time)

    def turnLeft(self, angle, speed, end_time=0):
        current_angle = 0
        self.motor.t_left(speed, 0)
        while True:
            begin_time = time.time()
            if math.fabs(current_angle) >= angle:
                self.motor.t_stop(end_time)
                break
            v = self.mpu.get_gyro_data()['z']
            current_angle = current_angle + v * self.mpu_freq
            passed_time = time.time()-begin_time
            time.sleep(self.mpu_freq-passed_time)

    def turnRight(self, angle, speed, end_time=0):
        current_angle = 0
        self.motor.t_right(speed, 0)
        while True:
            begin_time = time.time()
            if math.fabs(current_angle) >= angle:
                self.motor.t_stop(end_time)
                break
            v = self.mpu.get_gyro_data()['z']
            current_angle = current_angle + v * self.mpu_freq
            passed_time = time.time()-begin_time
            time.sleep(self.mpu_freq-passed_time)

    def stop(self, end_time=0):
        self.motor.t_stop(end_time)

    def t_up(self, speed, t_time):
        self.motor.t_up(speed, t_time)

    def t_down(self, speed, t_time):
        self.motor.t_down(speed, t_time)

    def t_left(self, speed, t_time):
        self.motor.t_left(speed, t_time)

    def t_right(self, speed, t_time):
        self.motor.t_right(speed, t_time)

    def t_stop(self, t_time):
        self.motor.t_stop(t_time)


if __name__ == '__main__':
    controller = Controller(gyro_address=0x68, gpio_trigger=20, gpio_echo=21)
    try:
        controller.forward(0.5, 100)
        controller.turnRight(90, 80)
        time.sleep(5)
        controller.turnLeft(90, 80)
    except KeyboardInterrupt:
        controller.stop()
        GPIO.cleanup()


