import constants
from casting.actor import Actor
from shared.point import Point

x = int(constants.MAX_X / 2) #x=900/2=450
y = int(constants.MAX_Y)-int(constants.FONT_SIZE) #y=600-15= 585
position = Point(x, y) #(450, 585)

class Spaceship(Actor):
    """
    A hovering player.
    
    The responsibility of player is to move itself.

    Attributes:

    """
    def __init__(self):
        super().__init__()
        self.set_text("%")
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.WHITE)
        self.set_position(position)


    


 