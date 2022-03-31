from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.bullet import Bullet
from game.casting.image import Image


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()
        ship_position = ship_body.get_position()
        
        
        
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        if x < FIELD_LEFT:
            position = Point(0, position.get_y())
            body.set_position(position)

        elif x >= (FIELD_RIGHT - BULLET_WIDTH):
            position = Point(ship_position.get_x(), SCREEN_HEIGHT - 50  )
            body.set_position(position)

        if y < FIELD_TOP:
            ship_x = ship_position.get_x()
            position = Point(ship_x, 10000)
            body.set_position(position)
            velocity = Point(0,0)
            body.set_velocity(velocity)
            bullet.reset_release()

        elif y >= (FIELD_BOTTOM - BULLET_WIDTH):
            # stats = cast.get_first_actor(STATS_GROUP)
            # stats.lose_life()

            # if stats.get_lives() > 0:
            #     callback.on_next(TRY_AGAIN)
            # else:
            #     callback.on_next(GAME_OVER)
            #     self._audio_service.play_sound(over_sound)
            pass
    
    def remake_bullet(self, cast):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()
        ship_position = ship_body.get_position()
        x = ship_position.get_x()
        y = SCREEN_HEIGHT - SHIP_HEIGHT - BULLET_HEIGHT  
        position = Point(x, y)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = ship_body.get_velocity()
        body = Body(position, size, velocity)
        # body.set_position(position)
        image = Image(BULLET_IMAGE)
        bullet = Bullet(body, image, True)
        cast.add_actor(BULLET_GROUP, bullet)
