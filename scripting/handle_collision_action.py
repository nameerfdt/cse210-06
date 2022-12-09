import constants
from casting.actor import Actor
from scripting.action import Action
from shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._points = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        marauders = cast.get_actors("marauders")
        bullets = cast.get_actors("bullets")
        banner = cast.get_first_actor("banners")
        
        for marauder in marauders:

            for bullet in bullets:
                if marauder.get_position().equals(bullet.get_position()):
                    cast.remove_actor("marauders", marauder)
                    cast.remove_actor("bullets", bullet)
                    self._points += 1

        message = f"Points: {self._points}"
        banner.set_text(message)