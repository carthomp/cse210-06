from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.stats import Stats

# We need to rewrite this to see if enemies collide, not the ball.

class CollideShipAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()
        enemies = cast.get_actors(ENEMY_GROUP)
        over_sound = Sound(OVER_SOUND)
        collided = False
        for enemy in enemies:
            enemy_body = enemy.get_body()
            if self._physics_service.has_collided(enemy_body, ship_body):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                collided = True
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)
        # for enemy in enemies:
        #     enemy_body = enemy.get_body()
            # enemy_body.set_position(enemy.get_starting_position())
