import constants
from scripting.action import Action

class MoveActorsAction(Action):
    """An update action that handles movement of actors
    
    The responsibility of the MoveActorsAction is to control the movement
    of the actors based on their velocity.
    """
    def __init__(self):
        """Constructs a new MoveActorsAction.
        
        Args:
        """
        self._current_cycle = 0

    def execute(self, cast, script):
        bullets = cast.get_actors("bullets")
        marauders = cast.get_actors("marauders")
        
        for bullet in bullets:
            bullet.move_next(constants.MAX_X, constants.MAX_Y)

        for marauder in marauders:
            if self._current_cycle % 32 == 0 and self._current_cycle !=0:
                marauder.move_next(constants.MAX_X, constants.MAX_Y)
        
        spaceship = cast.get_first_actor("spaceships")
        spaceship.move_next(constants.MAX_X, constants.MAX_Y)

        self._current_cycle += 1
        

        