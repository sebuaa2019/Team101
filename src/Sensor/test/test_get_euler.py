from Sensor import GetEuler
import unittest


class Test(unittest.TestCase):
    def test_IMU(self):
        for i in range(200):
            pitch, roll, yaw = GetEuler.Update_IMU(9.8, 0, 0, 0, 0, 0)
        self.assertEquals([round(pitch), round(roll), round(yaw)], [-90, 180, 180])


if __name__ == '__main__':
    unittest.main()
