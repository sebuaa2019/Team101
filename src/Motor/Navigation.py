# coding=utf-8
import Controller
import RPi.GPIO as GPIO

plants = [1, 1.5, 2, 2.5, 3]    # 植株绝对位置，小车出发一侧为原点
plants_side = 'right'       # 初始植株在小车左手边或右手边，right 或者 left
ravine_length = 4
orientation = 'forward'     # 超声波雷达朝向，forward 或者 backward
direction = 'leave'         # 初始小车朝向，leave 或者 return


def operate():
    a = raw_input()


if __name__ == '__main__':
    car = Controller.Controller(gyro_address=0x68, gpio_trigger=20, gpio_echo=21)
    current_location = car.getLoc()
    if orientation == 'backward':
        current_location = ravine_length-current_location

    try:
        # 将小车姿态设为初始状态
        car.forward(plants[0]-current_location, 100, end_time=0.2)
        if plants_side == 'right':
            car.turnRight(90, 80, end_time=0.2)
        else:
            car.turnLeft(90, 80, end_time=0.2)

        # 开始循环
        while True:
            for i in range(len(plants)-1):
                operate()

                # 转回正常行驶
                if plants_side == 'right':
                    car.turnLeft(90, 80, end_time=0.2)
                else:
                    car.turnRight(90, 80, end_time=0.2)

                # 前进
                if direction == 'leave':
                    plant_from = i
                    plant_to = plant_from+1
                    forward_length = plants[plant_to] - plants[plant_from]
                else:
                    plant_from = len(plants)-1-i
                    plant_to = plant_from-1
                    forward_length = plants[plant_from] - plants[plant_to]
                car.forward(forward_length, 100, end_time=0.2)

                # 转向植株
                if plants_side == 'right':
                    car.turnRight(90, 80, end_time=0.2)
                else:
                    car.turnLeft(90, 80, end_time=0.2)

            # 小车改变前进方向，改变状态即可
            if direction == 'leave':
                direction = 'return'
            else:
                direction = 'leave'
            if plants_side == 'left':
                plants_side = 'right'
            else:
                plants_side = 'left'
    except KeyboardInterrupt:
        car.stop()
        GPIO.cleanup()


