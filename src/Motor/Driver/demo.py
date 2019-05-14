import motordriver as driver

if __name__ == '__main__':
    while True:
        driver.t_up(100, 5)
        driver.t_stop(1)
        driver.t_right(100, 1)
        driver.t_stop(1)
