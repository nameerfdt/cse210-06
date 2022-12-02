from Game.Shared.color import Color
from Game.Shared.point import Point

class Actor:
    def __init__(self):
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._points = 0


    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size

    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity

    def move_next(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y

    