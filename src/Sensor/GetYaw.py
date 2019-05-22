# coding:utf-8
import math
import GyroscopeDriver
import time

frequency = 0.01
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

