from constants import *
from game.scripting.action import Action
from game.casting.sound import Sound

# Formerly ControlRacketAction


class ControlShip(Action):

    def __init__(self, keyboard_service, audio_service):
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service

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
            if not bullet.is_released():
                bullet_body = bullet.get_body()
                ship_body = ship.get_body()
                ship_position = ship_body.get_position()
                bullet_body.set_position(ship_position)
                bullet.release()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
        else: 
            ship.stop_moving()
            bullet.stop_moving()

