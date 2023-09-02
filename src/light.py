import neopixel


LIGHT_PIN = 22  # GPIO 22, hardware pin 29
LEDS = 8

pixels = neopixel.Neopixel(LEDS, 0, LIGHT_PIN, 'GRB')


def red(brightness=2):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (255, 0, 0))
    pixels.show()


def amber(brightness=5):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (255, 64, 0))
    pixels.show()


def green(brightness=20):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (0, 255, 0))
    pixels.show()


def off():
    pixels.brightness(0)
    pixels.clear()
    pixels.show()
