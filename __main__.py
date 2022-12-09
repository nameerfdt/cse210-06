import constants

from casting.actor import Actor
from casting.cast import Cast
from casting.spaceship import Spaceship
from casting.marauder import Marauder

from directing.director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.point import Point


def main():
    
    # create the cast
    cast = Cast()

    marauder = Marauder()
    cast.add_actor("marauders",marauder)

    spaceship = Spaceship()
    cast.add_actor("spaceships",spaceship)
    
    # create the banner for displaying the points
    banner = Actor()
    banner.set_text("Points: 0") #displays this text in banner position
    banner.set_font_size(constants.FONT_SIZE) 
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0)) #(x=15, y=0)
    cast.add_actor("banners", banner) #group name:banners" actor name: banner
    
    #create the spaceship
    # spaceship = Spaceship()
    # cast.add_actor("spaceships",spaceship)
    # x = int(constants.MAX_X / 2) #x=900/2=450
    # y = int(constants.MAX_Y)-int(constants.FONT_SIZE) #y=600-15= 585
    # position = Point(x, y) #(450, 585)

    # spaceship = Actor()
    # spaceship.set_text("#")
    # spaceship.set_font_size(constants.FONT_SIZE)
    # spaceship.set_color(constants.WHITE)
    # spaceship.set_position(position) #(450, 585)
    # cast.add_actor("spaceships", spaceship)

    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()