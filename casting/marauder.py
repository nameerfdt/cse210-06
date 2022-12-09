import constants

from casting.actor import Actor

class Marauder(Actor):
    """An item of interest inheriting attributes and methods from parent.
    
    The responsibility of an Marauder is to provide a message about itself.
    
    Attributes:
        _message (string): A brief description
    """
    def __init__(self):
        """Constructs a new Marauder invoking the part constructor"""

        super().__init__()
        self.set_text("@")
        self.set_color(constants.WHITE)
        self.set_font_size(constants.FONT_SIZE)