import constants

from casting.actor import Actor
from shared.point import Point


class Bullet(Actor):
    """An item of interest inheriting attributes and methods from parent.
    
    The responsibility of an Bullet is to provide a message about itself.
    
    Attributes:
        _message (string): A brief description
    """
    def __init__(self):
        """Constructs a new Bullet invoking the part constructor"""

        super().__init__()
        self.set_velocity(Point(0, -10))
        self.set_color(constants.RED)
        self.set_text("^")
