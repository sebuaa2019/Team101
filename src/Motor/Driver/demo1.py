import driver

if __name__ == '__main__':
    motor = driver.MotorDriver()
    for i in range(2):
        motor.t_up(100, 5)
        motor.t_right(100, 2)
        motor.t_stop(2)
        motor.t_left(100, 2)
    motor.t_up(100, 2)
