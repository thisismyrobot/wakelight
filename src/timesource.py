import network  
import ntptime
import time

from credentials import SSID, PASSWORD


MAXFAILS = 10


def sync():
    wlan = network.WLAN(network.STA_IF)
    time.sleep(2)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    fails = 0
    while not wlan.isconnected():
        fails += 1
        if fails > MAXFAILS:
            import machine
            machine.reset()
        time.sleep(1)

    ntptime.settime()

    wlan.disconnect()
    wlan.active(False)


def time_of_day(offset, dst):
    local_time = time.localtime(time.time() + ((offset + 1*dst) * 3600))
    return local_time[3] + (local_time[4] / 60)
