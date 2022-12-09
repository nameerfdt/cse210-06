import constants

from casting.bullet import Bullet
from scripting.action import Action
from shared.point import Point

class AddBulletsAction(Action):
    """An update action that handles movement of actors
    
    The responsibility of the MoveActorsAction is to control the movement
    of the actors based on their velocity.
    """
    def __init__(self, keyboard_service):
        """Constructs a new SetVelocityAction.
        
        Args:
        """
        self._bullets_to_fire = 0
        self._keyboard_service = keyboard_service
        self._current_cycle = 0

    def execute(self, cast, script):
        if self._keyboard_service.shoot_bullet():
            self._bullets_to_fire += 1
        if self._keyboard_service.gun_off():
            self._bullets_to_fire = 1        
        
        if self._current_cycle % 4 == 0:                    
            if self._bullets_to_fire > 0:
                bullet = Bullet()
                spaceship = cast.get_first_actor("spaceships")
                bullet.set_position(Point(spaceship.get_position().get_x(), constants.MAX_Y - 30))
                cast.add_actor("bullets", bullet)

                self._bullets_to_fire -= 1

        self._current_cycle += 1

