# coding=utf-8
# 温度传感器驱动使用 Adafruit 提供的开源驱动
# 该驱动兼容DHT11,DHT22, AM2302
# 使用前应：
# cd Adafruit_Python_DHT
# sudo python setup.py install
# 或 sudo python3 setup.py install
import Adafruit_DHT
import time

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }


def get_hum_temp(pin=4, sensor='11'):
    # 第一个参数为树莓派上GPIO BCM编号，第二个参数为传感器型号
    # 返回值有三个：湿度(humidity%)，温度(摄氏度)，获取数据是否成功
    humidity, temperature = Adafruit_DHT.read_retry(sensor_args[sensor], pin)
    if humidity is not None and temperature is not None:
        return humidity, temperature, True
    else:
        return 255, 255, False


if __name__ == '__main__':
    # setup frequency, should be lower than 0.5Hz
    frequency = 5
    try:
        while True:
            begin_time = time.time()
            humidity, temperature, receive = get_hum_temp(pin=4)
            if receive:
                print "temperature is: %.1f, humidity is: %.1f%%" % (temperature, humidity)
            else:
                print "wrong"
            cost_time = time.time() - begin_time
            time.sleep(frequency - cost_time)
    except KeyboardInterrupt:
        print "DHT11 End"
