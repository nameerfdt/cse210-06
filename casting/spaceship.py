import constants

from casting.actor import Actor
from shared.point import Point

class Spaceship(Actor):
    """An item of interest inheriting attributes and methods from parent.
    
    The responsibility of an Bullet is to provide a message about itself.
    
    Attributes:
        _message (string): A brief description
    """
    def __init__(self):
        """Constructs a new spaceship"""
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y) - int(constants.CELL_SIZE)
        position = Point(x, y)

        self.set_text("#")
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.WHITE)
        self.set_position(position)

