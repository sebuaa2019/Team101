# coding=utf-8
import Controller
import RPi.GPIO as GPIO

plants = [0.34, 0.7, 1.02, 1.30, 1.62]    # 植株绝对位置，小车出发一侧为原点
plants_side = 'right'       # 初始植株在小车左手边或右手边，right 或者 left
ravine_length = 1.92
orientation = 'backward'     # 超声波雷达朝向，forward 或者 backward
direction = 'leave'         # 初始小车朝向，leave 或者 return
car_length = 0.19           # 小车雷达到中心的距离


def operate():
    while True:
        a = raw_input()
        if a == 'w':
            car.t_up(100, 0.2)
            car.t_stop(0)
        elif a == 'a':
            car.t_left(80, 0.2)
            car.t_stop(0)
        elif a == 's':
            car.t_down(100, 0.2)
            car.t_stop(0)
        elif a == 'd':
            car.t_right(80, 0.2)
            car.t_stop(0)
        elif a == '':
            break
        else:
            continue


if __name__ == '__main__':
    car = Controller.Controller(gyro_address=0x68, gpio_trigger=20, gpio_echo=21)
    current_location = car.getLoc()
    if orientation == 'forward':
        current_location = ravine_length-current_location-car_length
    else:
        current_location = current_location+car_length

    try:
        # 将小车姿态设为初始状态
        car.forward(plants[0]-current_location, 100, end_time=0.2)
        if plants_side == 'right':
            car.turnRight(90, 60, end_time=0.2)
        else:
            car.turnLeft(90, 60, end_time=0.2)

        # 开始循环
        while True:
            for i in range(len(plants)-1):
                operate()

                # 转回正常行驶
                if plants_side == 'right':
                    car.turnLeft(90, 60, end_time=0.2)
                else:
                    car.turnRight(90, 60, end_time=0.2)

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
                    car.turnRight(90, 60, end_time=0.2)
                else:
                    car.turnLeft(90, 60, end_time=0.2)

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



