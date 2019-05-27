# coding=utf-8
import time
import unittest
from Sensor import GetEuler
from Sensor import GetYaw
from Sensor import GyroscopeDriver


class Test(unittest.TestCase):
    def test_init(self):
        mpu = GyroscopeDriver.GyroscopeDriver(0x68)

    def test_function_eular(self):
        mpu = GyroscopeDriver.GyroscopeDriver(0x68)
        pitch = 0
        roll = 0
        yaw = 0
        for i in range(1000):
            time_begin = time.time()
            accel_data = mpu.get_accel_data()
            gyro_data = mpu.get_gyro_data()
            pitch, roll, yaw = GetEuler.Update_IMU(accel_data['x'],
                                                   accel_data['y'],
                                                   accel_data['z'],
                                                   gyro_data['x'] * 0.01745,
                                                   gyro_data['y'] * 0.01745,
                                                   gyro_data['z'] * 0.01745)
            time.sleep(2 * GetEuler.halfT - (time.time() - time_begin))

        print "pitch is %.4f" % pitch
        print "roll is %.4f" % roll
        print "yaw is %.4f" % yaw

    def test_function_yaw(self):
        mpu = GyroscopeDriver.GyroscopeDriver(0x68)
        angle = GetYaw.get_angle(mpu, 5)
        print "5秒内转过 %.2f 度" % angle
        time_window = GetYaw.get_time(mpu, 90)
        print "转过90度花了 %.2f 秒" % time_window


if __name__ == '__main__':
    unittest.main()
