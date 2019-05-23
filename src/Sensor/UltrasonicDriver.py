# coding=utf-8
# 型号:HC-SR04超声波雷达
import RPi.GPIO as GPIO
import time


class UltrasonicDriver:
    def __init__(self, GPIO_TRIGGER=20, GPIO_ECHO=21):
        # 定义 GPIO 引脚
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO

        # 设置 GPIO 模式为 BCM
        GPIO.setmode(GPIO.BCM)
        # 设置 GPIO 的工作方式 (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        # 发送高电平信号到 Trig 引脚
        GPIO.output(self.GPIO_TRIGGER, True)

        # 持续 10 us
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        start_time = time.time()
        stop_time = time.time()

        # 记录发送超声波的时刻1
        while GPIO.input(self.GPIO_ECHO) == 0:
            start_time = time.time()

        # 记录接收到返回超声波的时刻2
        while GPIO.input(self.GPIO_ECHO) == 1:
            stop_time = time.time()

        # 计算超声波的往返时间 = 时刻2 - 时刻1
        time_elapsed = stop_time - start_time
        # 声波的速度为 343m/s， 转化为 34300cm/s。
        dist = (time_elapsed * 343) / 2

        return dist


if __name__ == '__main__':
    try:
        ultrasonic = UltrasonicDriver()
        while True:
            dist = ultrasonic.distance()
            print "Measured Distance = %.2f m" % dist
            # frequency: 1Hz
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
