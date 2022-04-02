from game.casting.actor import Actor
from game.casting.point import Point
from constants import ENEMY_HEIGHT, ENEMY_WIDTH


class Enemy(Actor):
    """A hostile entity that moves in a set pattern towards the bottom of the screen and has a deadly touch."""

    def __init__(self, body, animation, points, debug=False):
        """Constructs a new enemy.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
            move_counter: Int used to track the timing of the enemy movements.
            starting_position: Start position used to return the enemies to their start if a life is lost.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        self._move_counter = 0
        self._starting_position = Point(0,0)

    def get_animation(self):
        """Gets the enemy's image.

        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the enemy's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the enemy's points.

        Returns:
            A number representing the enemy's points.
        """
        return self._points
    
    def move_self(self):
        body = self._body
        if self._move_counter % 50 == 0:
            if (self._move_counter / 50) % 6 == 0:
                velocity = Point(ENEMY_WIDTH, 0)
            elif (self._move_counter / 50) % 6 == 1:
                velocity = Point(0, ENEMY_HEIGHT)
            elif (self._move_counter / 50) % 6 == 2:
                velocity = Point(-ENEMY_WIDTH, 0)
            elif (self._move_counter / 50) % 6 == 3:
                velocity = Point(-ENEMY_WIDTH, 0)
            elif (self._move_counter / 50) % 6 == 4:
                velocity = Point(0, ENEMY_HEIGHT)
            elif (self._move_counter / 50) % 6 == 5:
                velocity = Point(ENEMY_WIDTH, 0)
            else:
                velocity = Point(0,0)
            body.set_velocity(velocity)
        else:
            velocity = Point(0,0)
            body.set_velocity(velocity)
        self._move_counter += 1

    def get_starting_position(self):
        return self._starting_position
    
    def set_starting_position(self,position):
        """Sets the starting position for the enemy ships."""
        self._starting_position = position
    
    def reset_move_counter(self):
        self._move_counter = 0
    
