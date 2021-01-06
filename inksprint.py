import pydirectinput


class sprint_settings:
    # global settings for sprint class.
    toggled = False
    keybind = 'n'
    sprint_button = 'v'
    key_down = False  # W key pressed


# These functions are meant to be used by inkcontrols.py

def press_sprint():
    """Press sprint button."""
    if not sprint_settings.key_down and sprint_settings.toggled:
        pydirectinput.keyDown(sprint_settings.sprint_button)
        sprint_settings.key_down = True  # Key down changes to false in inkcontrols.py on release of w key


def release_sprint():
    """Release sprint button."""
    pydirectinput.keyUp(sprint_settings.sprint_button)


def toggle_sprint():
    """Toggle sprint."""
    sprint_settings.toggled = not sprint_settings.toggled
