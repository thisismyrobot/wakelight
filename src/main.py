import machine
import network
import time

import light
import timesource


OFFSET = 10  # UTC+10
DST = False  # TODO: Slider switch
DST_PIN = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)  # GPIO 9


WINDOWS = {
    (5.5, 6): light.amber,
    (6, 10): light.green,
    (21.5, 5.75): light.red,
}

def dst():
    return not DST_PIN.value()

def main(offset, windows, sleep=60, sync_every=60):

    light.off()
    time.sleep(2)
    light.red()
    time.sleep(2)
    light.amber()
    time.sleep(2)
    light.green()
    time.sleep(2)
    light.off()

    cycle = 0
    while True:
        if cycle % sync_every == 0:
            timesource.sync()

        time_of_day = timesource.time_of_day(offset + (dst() * 1))

        for ((start, end), action) in windows.items():
            if end > start and time_of_day >= start and time_of_day <= end:
                action()
                break
            elif end < start and (time_of_day >= start or time_of_day <= end):
                action()
                break
            else:
                light.off()

        time.sleep(sleep)
        cycle += 1

if __name__ == '__main__':
    time.sleep(5)
    main(OFFSET, WINDOWS)
