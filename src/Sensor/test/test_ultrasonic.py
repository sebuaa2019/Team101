from Sensor import UltrasonicDriver
import time
import unittest


class TestDict(unittest.TestCase):
    def test_init(self):
        ultrasonic = UltrasonicDriver.UltrasonicDriver()

    def test_function(self):
        ultrasonic = UltrasonicDriver.UltrasonicDriver()
        for i in range(10):
            dist = ultrasonic.distance()
            print "Measured Distance = %.2f m" % dist
            # frequency: 1Hz
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
