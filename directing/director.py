import random
import constants
from casting.aliens import Alien
from shared.color import Color
from shared.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, cell_size, font_size):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cell_size = cell_size
        self._font_size = font_size
        self._points = 0
        self._updates_loop = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the actor.
        
        Args:
            cast (Cast): The cast of actors.
        """
        spaceship = cast.get_first_actor("spaceships")
        bullet = cast.get_first_actor("bullets")
        alien = cast.get_first_actor("aliens")
        velocity = self._keyboard_service.get_direction()
        spaceship.set_velocity(velocity)
        bullet.set_velocity(velocity)
        alien.set_velocity(velocity)

    def _do_updates(self, cast):
        """
        Creates and loops the artifacts.
        Updates the positions and resolves any collisions.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        spaceship = cast.get_first_actor("spaceships")
        bullet = cast.get_first_actor("bullets")
        aliens = cast.get_actors("aliens")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        spaceship.move_next(max_x, max_y)
        bullet.move_next(max_x, max_y)

        # for alien in aliens:
        #     alien.move_next(max_x, max_y)

        #     x = random.randint(1, constants.COLUMNS -1)
        #     y = 1
        #     position = Point(x, y)
        #     position = position.scale(self._cell_size)
            
        #     r = random.randint(0, 255)
        #     g = random.randint(0, 255)
        #     b = random.randint(0, 255)
        #     color = Color(r, g, b)

        #     alien = Alien()
        #     alien.set_velocity(Point(0,5))
        #     alien.set_font_size(self._font_size)
        #     alien.set_color(color)
        #     alien.set_position(position)
        #     cast.add_actor("aliens", alien)            

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        self._video_service._draw_grid()
    