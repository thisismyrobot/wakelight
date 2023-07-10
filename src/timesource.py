import network
import ntptime
import time

from credentials import SSID, PASSWORD


MAXFAILS = 10


def now():
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

    print(wlan.ifconfig())

    print(time.localtime())
    ntptime.settime()
    print(time.localtime())

    wlan.disconnect()
    wlan.active(False)
