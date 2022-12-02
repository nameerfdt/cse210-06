from casting.actor import Actor
from casting.cast import Cast
from constants import FONT_SIZE, WHITE, CELL_SIZE, MAX_X, MAX_Y, CAPTION, FRAME_RATE

from directing.director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.point import Point


def main():
    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("Points: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the miner
    x = int(MAX_X / 2)
    y = int(MAX_Y) - int(CELL_SIZE)
    position = Point(x, y)

    miner = Actor()
    miner.set_text("#")
    miner.set_font_size(FONT_SIZE)
    miner.set_color(WHITE)
    miner.set_position(position)
    cast.add_actor("miners", miner)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, CELL_SIZE, FONT_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()
