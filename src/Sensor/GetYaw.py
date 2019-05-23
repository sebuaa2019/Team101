# coding:utf-8
import math
import GyroscopeDriver
import time

frequency = 0.01    # 陀螺仪采样周期


def get_angle(gyro, time_window):
    # 得到陀螺仪gyro在一段时间内转过的角度
    # 该角度有正负区别
    angle = 0
    start_time = time.time()
    while time.time()-start_time < time_window:
        begin_time = time.time()
        v = gyro.get_gyro_data()['z']
        angle = angle + v * frequency
        cost_time = time.time()-begin_time
        # print cost_time
        time.sleep(frequency - cost_time)
    return angle


def get_time(gyro, angle):
    # 得到陀螺仪gyro转过一定角度所需要的时间
    current_angle = 0
    start_time = time.time()
    while math.fabs(current_angle) < angle:
        begin_time = time.time()
        v = gyro.get_gyro_data()['z']
        current_angle += v * frequency
        cost_time = time.time()-begin_time
        time.sleep(frequency - cost_time)
    return time.time()-start_time


if __name__ == "__main__":
    mpu = GyroscopeDriver.GyroscopeDriver(0x68)
    angle = 0
    try:
        while True:
            begin_time = time.time()
            v = mpu.get_gyro_data()['z']
            angle = angle + v * frequency
            cost_time = time.time()-begin_time
            # print cost_time
            time.sleep(frequency - cost_time)
    except KeyboardInterrupt:
        print "angle: %.2f" % angle

