from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ship(Actor):
    """The player-controlled spaceship that fires on enemy aliens in the game."""

    def __init__(self, body, animation, debug=False):
        """Constructs a new ship.

        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the ship's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the ship's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the ship using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the ship to the left."""
        velocity = Point(-SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_right(self):
        """Steers the ship to the right."""
        velocity = Point(SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the ship from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
