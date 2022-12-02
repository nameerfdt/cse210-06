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