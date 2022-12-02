import pyray
from Game.Shared.point import Point

class KeyboardService:
    def __init__(self):
        self._keys = {}

        self._keys["left arrow"] = pyray.K_LEFT
        self._keys["right arrow"] = pyray.K_RIGHT
        self._keys["spacebar"] = pyray.K_SPACE

    def is_key_up(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)