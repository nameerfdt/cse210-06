import constants
from actor import Actor


class Bullet(Actor):
    """
    A hovering player.
    
    The responsibility of player is to move itself.

    Attributes:

    """
    def __init__(self):
        super().__init__()
        self.bullet() #method prepare bullet
        self.set_text("^")
        self.set_color(constants.YELLOW)  
    
    


 