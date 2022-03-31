import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that is bounced around in the game."""

    def __init__(self, body, image, debug=False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._released = False

    def get_body(self):
        """Gets the ball's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.

        Returns:
            An instance of Image.
        """
        return self._image

    def release(self):
        """Release the ball in a random direction."""
        vx = 0
        vy = -BULLET_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
        self._released =  True
    
    def is_released(self):
        return self._released

    def reset_release(self):
        self._released = False
    
    def swing_left(self):
        """Steers the bat to the left."""
        if not self._released:
            velocity = Point(-(BULLET_VELOCITY ), 0)
            self._body.set_velocity(velocity)

    def swing_right(self):
        """Steers the bat to the right."""
        if not self._released:
            velocity = Point(BULLET_VELOCITY , 0)
            self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the bat from moving."""
        if not self._released:
            velocity = Point(0, 0)
            self._body.set_velocity(velocity)
