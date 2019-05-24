# coding=utf-8
# 型号:DHT11温湿度传感器
# 该驱动暂时有问题
import RPi.GPIO as GPIO
import time


class TempMoiDriver:
    data = []           # 温湿度值

    def __init__(self, channel=4):
        GPIO.setmode(GPIO.BCM)      # 以BCM编码格式
        for i in range(40):
            self.data.append(0)
        self.channel = channel
        self.setup()

    def setup(self):
        time.sleep(1)           # 时延一秒
        GPIO.setup(self.channel, GPIO.OUT)
        GPIO.output(self.channel, GPIO.LOW)
        time.sleep(0.02)        # 给信号提示传感器开始工作
        GPIO.output(self.channel, GPIO.HIGH)
        GPIO.setup(self.channel, GPIO.IN)
        while GPIO.input(self.channel) == GPIO.LOW:
            continue
        while GPIO.input(self.channel) == GPIO.HIGH:
            continue

    def receive(self):
        for counter in range(40):
            k = 0
            while GPIO.input(self.channel) == GPIO.LOW:
                continue
 
            while GPIO.input(self.channel) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
 
            if k < 8:          # 通过计数的方式判断是数据位高电平长短，以置0或1。
                self.data[counter] = 0
            else:
                self.data[counter] = 1

    def getTempHum(self):
        self.receive()
        humidity_bit = self.data[0:8]        # 分组
        humidity_point_bit = self.data[8:16]
        temperature_bit = self.data[16:24]
        temperature_point_bit = self.data[24:32]
        check_bit = self.data[32:40]

        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0

        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7 - i)              # 转换成十进制数据
            humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
            temperature += temperature_bit[i] * 2 ** (7 - i)
            temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
            check += check_bit[i] * 2 ** (7 - i)
 
        tmp = humidity + humidity_point + temperature + temperature_point       # 十进制的数据相加
 
        if check == tmp:                                # 数据校验，相等则输出
            return temperature, humidity, True
        else:                                       # 错误输出错误信息，和校验数据
            return temperature, humidity, False


if __name__ == '__main__':
    driver = TempMoiDriver(4)
    print "DHT 11 Sensor is working"
    try:
        while True:
            temperature, humidity, receive = driver.getTempHum()
            if receive:
                print "temperature : ", temperature, ", humidity : " , humidity
            else:
                print "wrong"
            # 根据厂商要求频率最好高于0.5Hz
            time.sleep(5)
    except KeyboardInterrupt:
        print("DHT11 stopped by User")
        GPIO.cleanup()
