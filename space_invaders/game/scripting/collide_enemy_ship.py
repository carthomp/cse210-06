from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.bullet import Bullet

# Formerly CollideBrickAction


class CollideEnemyShip(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def remake_bullet(self, cast):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()
        ship_position = ship_body.get_position()
        x = ship_position.get_x()
        y = SCREEN_HEIGHT - SHIP_HEIGHT - BULLET_HEIGHT  
        position = Point(x, y)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BULLET_IMAGE)
        bullet = Bullet(body, image, True)
        cast.add_actor(BULLET_GROUP, bullet)

    def execute(self, cast, script, callback):
<<<<<<< HEAD
        ball = cast.get_first_actor(BULLET_GROUP)
        enemies = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for enemy in enemies:
            ball_body = ball.get_body()
            enemy_body = enemy.get_body()

            if self._physics_service.has_collided(ball_body, enemy_body):
=======
        bullet = cast.get_first_actor(BULLET_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for brick in bricks:
            bullet_body = bullet.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(bullet_body, brick_body):
>>>>>>> 762512f0d0f73966597b28f7d56d88bfffb006a4
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = enemy.get_points()
                stats.add_points(points)
<<<<<<< HEAD
                cast.remove_actor(ENEMY_GROUP, enemy)
=======
                cast.remove_actor(BRICK_GROUP, brick)
                cast.remove_actor(BULLET_GROUP, bullet)
>>>>>>> 762512f0d0f73966597b28f7d56d88bfffb006a4
                self.remake_bullet(cast)
