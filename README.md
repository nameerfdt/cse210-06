# Final Project
_______

Space Marauder is an interactive game where they player moves a spaceship along the x axis and tries to shoot marauders that lower down the y axis. Marauders are created and move right and left. The spaceship launches bullets to try and shoot down the marauders. 

Player uses the left and right arrow keys to move the spaceship. The lauch the bullets, the player presses the space bar. When space bar is released, the bullets stop shooting. 

## Getting Started
_______

Make sure you have Python 3.10 or newer installed and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

Open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 __main__.py
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the puzzle folder and click the "run" button.

## Project Structure
_______

* main.py
    * setup game and act as initial launch point

* director.py
    * runs game operations for each cycle

* keyboard_service.py
    * enter key to start game
    * space for shooting
    * arrow keys left/right movement

* video_service.py
    * displays output to user through raylib

* actor.py (parent class)
    * velocity (attr)
    * color (attr)
    * position (attr)
    * font_sizes (attr)
    * text of actor (attr) how it's displayed
    * get_color (method)
    * get_font_sizes (method)
    * get_text (method)
    * get_position (method)
    * get_velocity (method)
    * set_color (method)
    * set_font_sizes (method)
    * set_text (method)
    * set_position (method)
    * set_velocity (method)
    * move_next (method)
    * aliens.py (child class)
    * spaceship.py (player) (child class)
    * bullets.py (child class)
    * score.py
    
* actions.py
    * control_player_action.py
        * uses keyboard_service to set player velocity
    * handle_collision_action.py
        * interprets what happens when actors touch each other
        * if player touches bullet player loses life
        * if alien touches bullet alien is removed
        * if alien touches player loses game
        * handle_game_over (method) if player out of lives
    * move_actors_action.py
        * tell actors to move to new positions as defined by velocity
    * draw_actors_action.py
        * calls video_service to draw related actors 
    * script.py
        * stores all actions
    
* color.py
    * hold information relating to the color of actor 
* point.py
    * hold information relating to the location of actor 
* constants.py
    * holds consistant values through game play


## Required Technologies
_______

* Python 3.10
* Raylib Python CFFI 3.7

## Authors
_______

* Alex Dahl (alexdahl@byui.edu)
* Tracy Freeman (nameerfdt@byui.edu)
* Joshua Herman (her21095@byui.edu)
* Chris Lynch (cjlynch@byui.edu)

