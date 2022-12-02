import constants
import random
from casting.actor import Actor
from shared.point import Point


class Alien(Actor):
    """A flying object dropping from the sky who gain it's attributes and methods from parent.
    
    The responsibility of an alian is to 
    
    Attributes:

    """

    def __init__(self):
        """Constructs a new alien"""
        super().__init__()

        for i in range (constants.NUMBER_OF_ALIENS):
            text = "@"
            x = random.randint(1, constants.COLUMNS -1)
            y = random.randint(1, constants.ROWS -1)
            position = Point(x, y)
            position = position.scale (constants.CELL_SIZE)

            color = constants.RED
            alien = Actor()
            alien.set_text(text)
            alien.set_font_size(constants.FONT_SIZE)
            alien.set_color(color)
            alien.set_position(position)

            


            







