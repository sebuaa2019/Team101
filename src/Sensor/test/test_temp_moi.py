import Adafruit_DHT
import time
from Sensor import GetHumTemp
import unittest


class Test(unittest.TestCase):
    def test_function(self):
        frequency = 5
        for i in range(5):
            begin_time = time.time()
            humidity, temperature, receive = GetHumTemp.get_hum_temp(pin=4)
            if receive:
                print "temperature is: %.1f, humidity is: %.1f%%" % (temperature, humidity)
            else:
                print "wrong"
            cost_time = time.time() - begin_time
            time.sleep(frequency - cost_time)


if __name__ == '__main__':
    unittest.main()
