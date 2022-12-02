import constants
from actor import Actor


class Spaceship(Actor):
    """
    A hovering player.
    
    The responsibility of player is to move itself.

    Attributes:

    """
    def __init__(self):
        super().__init__()
        self.spaceship() #method prepare spaceship

 