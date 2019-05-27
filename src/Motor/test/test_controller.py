from Motor import Controller


if __name__ == '__main__':
    motor = Controller.Controller()
    while True:
        a = raw_input()
        if a == 'w' or a == 'W':
            motor.t_up(100, 0.2)
            motor.t_stop(0)
        elif a == 'a' or a == 'A':
            motor.t_left(100, 0.2)
            motor.t_stop(0)
        elif a == 's' or a == 'S':
            motor.t_down(100, 0.2)
            motor.t_stop(0)
        elif a == 'd' or a == 'D':
            motor.t_right(100, 0.2)
            motor.t_stop(0)
        elif a == '':
            break
        else:
            continue
