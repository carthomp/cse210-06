from constants import *
from game.scripting.action import Action

# Formerly ControlRacketAction


class ControlShip(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        bullet = cast.get_first_actor(BULLET_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            ship.swing_left()
            bullet.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.swing_right()
            bullet.swing_right()
        elif self._keyboard_service.is_key_down(SPACE):
            bullet.release()
        else: 
            ship.stop_moving()
            bullet.stop_moving()

