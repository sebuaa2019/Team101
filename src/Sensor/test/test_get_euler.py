from Sensor import GetEuler
import unittest


class Test(unittest.TestCase):
    def test_IMU_special(self):
        # -90, +180, +180
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(9.8, 0, 0, 0, 0, 0)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [-90, 180, 180])
        # +90, 0, 0
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(-9.8, 0, 0, 0, 0, 0)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [90, 0, 0])
        # -45, 0, 0
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(6.9, 0, 6.9, 0, 0, 0)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [-45, 0, 0])
        # +45, 0, 0
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(-6.9, 0, 6.9, 0, 0, 0)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [45, 0, 0])
        # +43, +22, +10
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(-6.9, 2.8, 6.9, 0.4, 0.2, -0.01)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [43, 22, 10])
        # -59, -113, 72
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(4.6, -2.5, -1.08, 0.09, -0.16, 0.63)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [-59, -113, 72])


if __name__ == '__main__':
    unittest.main()
