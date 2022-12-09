from scripting.action import Action
from shared.point import Point

class SetVelocityAction(Action):
    """An update action that handles movement of actors
    
    The responsibility of the MoveActorsAction is to control the movement
    of the actors based on their velocity.
    """
    def __init__(self):
        """Constructs a new SetVelocityAction.
        
        Args:
        """
        self._movement_count = 0
        self._current_cycle = 0

    def execute(self, cast, script):
        if self._current_cycle % 32 == 0 and self._current_cycle !=0:
            if self._movement_count != 10:
                if self._movement_count == 0 or self._movement_count == 1 or self._movement_count == 8 or self._movement_count == 9:
                    velocity = Point(-15, 0)
                    self._movement_count += 1
                elif self._movement_count == 3 or self._movement_count == 4 or self._movement_count == 5 or self._movement_count == 6:
                    velocity = Point(15, 0)
                    self._movement_count += 1
                elif self._movement_count == 2 or self. _movement_count == 7:
                    velocity = Point(0, 15)
                    self._movement_count += 1
            else:
                velocity = Point(-15, 0)
                self._movement_count = 1

        marauders = cast.get_actors("marauders")

        for marauder in marauders:
            if self._current_cycle % 32 == 0 and self._current_cycle !=0:
                marauder.set_velocity(velocity)

        self._current_cycle += 1