
from casting.actor import Actor
from shared.point import Point


class Marauder(Actor):
    """A flying object dropping from the sky who gain it's attributes and methods from parent.
    
    The responsibility of an alian is to 
    
    Attributes:

    """

    def __init__(self):
        """Constructs a new alien"""
        super().__init__()
        self._message = ""

    def get_message(self):
        """Gets the marauders message
        
        Returns:
            string: the message
        """
        return self._message
        
    def set_message(self, message):
        """Updates the marauders message.
        
        Args:
            message (str): the message
        """
        self._message = message

        # for i in range (constants.NUMBER_OF_ALIENS):
        #     text = "@"
        #     x = random.randint(1, constants.COLUMNS -1)
        #     y = random.randint(1, constants.ROWS -1)
        #     position = Point(x, y)
        #     position = position.scale (constants.CELL_SIZE)

        #     color = constants.RED
        #     alien = Actor()
        #     alien.set_text(text)
        #     alien.set_font_size(constants.FONT_SIZE)
        #     alien.set_color(color)
        #     alien.set_position(position)

            


            







