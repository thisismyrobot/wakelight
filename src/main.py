import network
import time

import light
import timesource


def main():
    print(timesource.now())

    while True:
        print('Woo!')
        light.red()
        time.sleep(2)
        light.amber()
        time.sleep(2)
        light.green()
        time.sleep(2)


if __name__ == '__main__':
    time.sleep(5)
    main()

