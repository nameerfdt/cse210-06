from scripting.actions import Action

class MoveActorsAction(Action):
    """An update action that handles movement of actors
    
    The responsibility of the MoveActorsAction is to control the movement
    of the actors based on their velocity.
    """

    def execute(self, cast, script):
        actors = cast.get_all_actors()
        
        for actor in actors:
            actor.move_next()