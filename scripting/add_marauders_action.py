import constants

from casting.marauder import Marauder
from scripting.action import Action
from shared.point import Point

class AddMarauderAction(Action):
    """An update action that handles movement of actors
    
    The responsibility of the MoveActorsAction is to control the movement
    of the actors based on their velocity.
    """
    def __init__(self):
        """Constructs a new SetVelocityAction.
        
        Args:
        """
        self._current_x = 9
        self._current_cycle = 0

    def execute(self, cast, script):
        current_marauder = 0
        if self._current_cycle % 320 == 0:
            for n in range(9):
                current_marauder += 1
                x = self._current_x
                y = 1
                position = Point(x, y)
                position = position.scale(constants.CELL_SIZE)
                
                marauder = Marauder()
                marauder.set_position(position)
                cast.add_actor("marauders", marauder)

                if current_marauder == 9:
                    self._current_x = 10
                else:
                    self._current_x += 5

        self._current_cycle += 1
