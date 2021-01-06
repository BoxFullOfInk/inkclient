# This is meant to be imported by GUI
from pynput import keyboard, mouse
import inkclicker
import inksprint
import win32api

from inkgui import Ui_MainWindow

listening = False


class Window:
    window = Ui_MainWindow()


def init_window(win):
    """"Give this file access to the gui. This has to be run before starting other threads."""
    Window.window = win


def init_keyboard_listener():
    """Creates listener that can be started by gui."""
    new_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    return new_listener


def init_mouse_listener():
    """Creates listener that can be started by gui."""
    new_m_listener = mouse.Listener(on_scroll=on_scroll)
    return new_m_listener


def on_scroll(x, y, dx, dy):
    """Disable autoclicker on scroll. This avoids suspicious clicking."""
    inkclicker.clicker_settings.toggled = False


def on_press(key):
    """Toggles in addition to sprints."""
    if listening:
        # For autoclick and sprint toggles, I tried using GetAsyncKeyState instead of pynput's listener
        # but it ends up not triggering at times. This is why minecraft's sprint key has to be bound to a letter.

        # Toggle autoclicker
        if key in (keyboard.KeyCode(char=inkclicker.clicker_settings.keybind),
                   keyboard.KeyCode(char=inkclicker.clicker_settings.keybind.upper())):
            inkclicker.toggle_ac()
            Window.window.autoclick_box.setTitle(
                "Autoclick - {}".format('On' if inkclicker.clicker_settings.toggled else 'Off'))
            inkclicker.clicker_settings.keybind_pressed = True
        # Sprint when toggled
        elif win32api.GetAsyncKeyState(ord('W')):
            inksprint.press_sprint()
        # Toggle sprint
        elif key in (keyboard.KeyCode(char=inksprint.sprint_settings.keybind),
                     keyboard.KeyCode(char=inksprint.sprint_settings.keybind.upper())):
            inksprint.toggle_sprint()
            Window.window.sprint_box.setTitle(
                "Sprint - {}".format('On' if inksprint.sprint_settings.toggled else 'Off'))
            Window.window.sprint_box.update()


def on_release(key):
    """Sets all key pressed bools to false."""
    if listening:
        if key in (keyboard.KeyCode(char='W'), keyboard.KeyCode(char='w')):
            inksprint.sprint_settings.key_down = False
            if inksprint.sprint_settings.toggled:
                inksprint.release_sprint()
        elif key in (keyboard.KeyCode(char='R'), keyboard.KeyCode(char='r')):
            inkclicker.clicker_settings.keybind_pressed = False
