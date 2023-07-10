import neopixel


LIGHT_PIN = 22  # GPIO 22, hardware pin 29
LEDS = 1

pixels = neopixel.Neopixel(LEDS, 0, LIGHT_PIN, 'GRB')


def red(brightness=10):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (255, 0, 0))
    pixels.show()


def amber(brightness=20):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (255, 128, 128))
    pixels.show()


def green(brightness=30):
    pixels.brightness(brightness)
    pixels.set_pixel_line(0, LEDS, (0, 255, 0))
    pixels.show()
