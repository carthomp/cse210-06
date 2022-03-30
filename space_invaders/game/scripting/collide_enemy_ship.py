from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

# Formerly CollideBrickAction


class CollideEnemyShip(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for brick in bricks:
            bullet_body = bullet.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(bullet_body, brick_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
                cast.remove_actor(BULLET_GROUP, bullet)
