import network
import time

import light
import timesource


OFFSET = 10  # UTC+10
DST = False  # TODO: Slider switch


TIMING = {
    (5.5, 6): light.amber,
    (6, 10): light.green,
    (22, 5.75): light.red,
}

def main(offset, dst, actions, sleep=60, sync_every=60):
    cycle = 0
    while True:
        if cycle % sync_every == 0:
            timesource.sync()

        time_of_day = timesource.time_of_day(offset, dst)

        for ((start, end), action) in actions.items():
            if end > start and time_of_day >= start and time_of_day <= end:
                action()
                break
            elif end < start and (time_of_day >= end or time_of_day <= start):
                action()
                break

        time.sleep(sleep)
        cycle += 1

if __name__ == '__main__':
    time.sleep(5)
    main(OFFSET, DST, TIMING)
