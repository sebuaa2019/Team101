import Controller


def tune():
    while True:
        a = raw_input()
        if a == 'w':
            motor.t_up(100, 0.2)
            motor.t_stop(0)
        elif a == 'a':
            motor.t_left(100, 0.2)
            motor.t_stop(0)
        elif a == 's':
            motor.t_down(100, 0.2)
            motor.t_stop(0)
        elif a == 'd':
            motor.t_right(100, 0.2)
            motor.t_stop(0)
        elif a == '':
            break
        else:
            continue


if __name__ == '__main__':
    motor = Controller.Controller()
    while True:
#    for i in range(5):
        tune()
        # motor.forward(100, 0.5)
        motor.t_stop(1)
        motor.t_right(85, 4.5)
        motor.t_stop(0)
        tune()
        motor.t_left(92, 4.5)
        motor.t_stop(0)
        tune()
    tune()
    motor.t_stop(0)
