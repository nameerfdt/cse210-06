import constants

from casting.actor import Actor
from casting.cast import Cast
from casting.spaceship import Spaceship

from directing.director import Director

from scripting.script import Script
from scripting.add_bullets_action import AddBulletsAction
from scripting.add_marauders_action import AddMarauderAction
from scripting.control_player_action import ControlPlayerAction
from scripting.draw_actors_action import DrawActorsAction
from scripting.handle_collision_action import HandleCollisionsAction
from scripting.move_actors_action import MoveActorsAction
from scripting.set_velocity_action import SetVelocityAction

from services.keyboard_service import KeyboardService
from services.video_service import VideoService
 
from shared.point import Point

def main():
    # create the cast
    cast = Cast()
    cast.add_actor("spaceships", Spaceship())

    # create the banner
    banner = Actor()
    banner.set_text("Points: 0")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)

    script = Script()
    script.add_action("input", ControlPlayerAction(keyboard_service))
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", AddMarauderAction())
    script.add_action("update", AddBulletsAction(keyboard_service))
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", SetVelocityAction())
    script.add_action("update", MoveActorsAction())

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
