import pydirectinput
import random
from time import sleep
import threading


def toggle_ac():
    """Toggle autoclicker."""
    if not clicker_settings.keybind_pressed:
        clicker_settings.toggled = not clicker_settings.toggled


class clicker_settings:
    # global settings for clicker class.
    running = True
    min_cps = 6
    max_cps = 8
    toggled = False
    keybind = 'r'
    keybind_pressed = False
    mode = 18  # minecraft version

    sword, axe = 0.6, 1.25
    cooldown_mode = sword


class clicker(threading.Thread):
    def __init__(self):
        super().__init__()
        pydirectinput.PAUSE = 0  # sleep() is used for delays instead

    def run(self):
        while clicker_settings.running:  # keeps thread running
            while clicker_settings.toggled and clicker_settings.running:
                # delay is halved to simulate time between mouse down and mouse up
                half_delay = 1 / random.uniform(clicker_settings.min_cps, clicker_settings.max_cps) / 2
                half_offset = random.uniform(0, half_delay / 2)
                pydirectinput.mouseDown()
                sleep(half_delay - half_offset)
                pydirectinput.mouseUp()

                if clicker_settings.mode == 18:
                    sleep(half_delay + half_offset)
                else:
                    sleep(clicker_settings.cooldown_mode)
            sleep(0.1)  # allow for threading to work


