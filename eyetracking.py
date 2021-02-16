from talon import actions, app, Module
from talon_plugins import eye_zoom_mouse
from talon_plugins import eye_mouse

def calibrate_eye_tracking():
    # Menu point stays unticked, don't know how to tick it.
    # talon.app.menu.toggle('Control Mouse (Zoom)', True) doesn't work and I don't know how to either provide or get the parent 'Eye Tracking'.
    print("Calibrating eye tracking.")
    eye_mouse.calib_start()

def disable_eye_tracking():
    # Menu point stays unticked, don't know how to tick it.
    # talon.app.menu.toggle('Control Mouse (Zoom)', True) doesn't work and I don't know how to either provide or get the parent 'Eye Tracking'.
    print("Disabling eye tracking (zoom mouse).")
    eye_zoom_mouse.toggle_zoom_mouse(False)

def enable_eye_tracking():
    # Menu point stays unticked, don't know how to tick it.
    # talon.app.menu.toggle('Control Mouse (Zoom)', True) doesn't work and I don't know how to either provide or get the parent 'Eye Tracking'.
    print("Enabling eye tracking (zoom mouse).")
    eye_zoom_mouse.toggle_zoom_mouse(True)


mod = Module()
@mod.action_class
class Actions:
    def eyes_calib():
        """Calibrates eye tracking."""
        calibrate_eye_tracking()
    def eyes_on():
        """Enables eye tracking (zoom mouse)."""
        enable_eye_tracking()
    def eyes_off():
        """Disables eye tracking (zoom mouse)."""
        disable_eye_tracking()


def app_launch():
    # print("Disabling SRE.")
    # actions.speech.disable()
    enable_eye_tracking()

app.register("launch", app_launch)
