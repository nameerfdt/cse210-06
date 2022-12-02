import constants
import random

from casting.actor import Actor
from casting.bullet import Bullet
from casting.marauder import Marauder
from shared.color import Color
from shared.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            cell_size: Cell size of the game board.
            font_size: Font size of the text.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 0
        self._updates_loop = 0
        self._bullets_to_fire = 0
        self._current_x = 10
        self._movement_count = 0

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
        """Gets directional input from the keyboard and applies it to the spaceship.
        
        Args:
            cast (Cast): The cast of actors.
        """
        spaceship = cast.get_first_actor("spaceships")
        velocity = self._keyboard_service.get_direction()
        spaceship.set_velocity(velocity)
        if self._keyboard_service.shoot_bullet():
            self._bullets_to_fire += 1
        if self._keyboard_service.gun_off():
            self._bullets_to_fire = 1

    def _do_updates(self, cast):
        """Updates the spaceship's position and resolves any collisions of bullets with marauders.
        Generates new row of marauders for each cycle.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        spaceship = cast.get_first_actor("spaceships")
        bullets = cast.get_actors("bullets")
        marauders = cast.get_actors("marauders")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        spaceship.move_next(max_x, max_y)

        for marauder in marauders:
            if marauder.get_position().get_y() == max_y + 30:
                cast.remove_actor("marauders", marauder)

            for bullet in bullets:
                if marauder.get_position().equals(bullet.get_position()):
                    cast.remove_actor("marauders", marauder)
                    cast.remove_actor("bullets", bullet)
                    self._points += 1

        if self._updates_loop % 32 == 0 and self._updates_loop !=0:
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

        for marauder in marauders:
            if self._updates_loop % 32 == 0 and self._updates_loop !=0:
                marauder.set_velocity(velocity)
                marauder.move_next(max_x, max_y)

        if self._updates_loop % 320 == 0:
            for n in range(9):
            
                text = "0"
                x = self._current_x
                y = 1
                position = Point(x, y)
                position = position.scale(constants.CELL_SIZE)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                
                marauder = Marauder()
                marauder.set_text(text)
                marauder.set_font_size(constants.FONT_SIZE)
                marauder.set_color(color)
                marauder.set_position(position)
                cast.add_actor("marauders", marauder)

                if x == constants.COLS - 10:
                    self._current_x = 10
                else:
                    self._current_x += 5

        if self._updates_loop % 4 == 0:
            if self._bullets_to_fire > 0:
                bullet = Bullet()
                bullet.set_position(Point(spaceship.get_position().get_x(), constants.MAX_Y - 30))
                cast.add_actor("bullets", bullet)

                self._bullets_to_fire -= 1

        for bullet in bullets:
            bullet.move_next(max_x, max_y)

        message = f"Points: {self._points}"
        banner.set_text(message)
        
        self._updates_loop += 1

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()