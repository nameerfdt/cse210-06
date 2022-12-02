import constants
from Game.Scripting.action import Action
from Game.Shared.point import Point

class ControlActorsAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        alien = cast.get_first_actor ("aliens")

        if self._keyboard_service.is_k_left("left arrow"):
            