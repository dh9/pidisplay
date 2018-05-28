import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, LCD_FONT

def display(message)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90)

    print(message)
    show_message(device, message, fill="white", font=proportional(LCD_FONT))

if __name__ == "__main__"
    parser = argparse.ArgumentParser(description='arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("message")

    args = parser.parse_args()

    try:
        display(args.message)
    except KeyboardInterrupt:
            pass
