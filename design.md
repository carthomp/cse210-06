# Space Invaders

## Design Priority

```
(2) Main Scene
·        (2) Play button
·        (3) Difficulty
(1) Game Scene
·        (1) User-controlled spaceship
·        (1) Aliens movement
·        (1) Multicolored Aliens
·        (1) Collision detection
·        (2) Life display
·        (2) Score display
·        (2) Sound effects
(3) Difficulty Scene
·        (3) Difficulty choice (easy, normal, expert)
·        (3) Back button
(2) Win Scene
·        (2) Announcement
·        (3) Smiley face animation
(2) Lose Scene
·        (2) Announcement
·        (2) Restart button
·        (3) Sad face animation
```

## Class Design

```
Directing:
-       Director
Scripting:
-       Script
-       Action
-       Control Actors
-       Move Actors
-       Handle Collisions
-       Change Scene
-       Draw Actors
Acting:
-       Actor
-       Cast
-       Alien
-       Spaceship
-       Bullet
-       Text (for Game Over, Lives, Score, etc)
Services:
-       Video Service
-       Keyboard Service
-       Audio Service?
Other:
-       Point
-       Color




Casting:
-       actor
-       animation
-       bullet
-       body
-       alien
-       cast
-       color
-       image
-       label
-       point
-       my spaceship
-       sound
-       stats
-       text

Services
  raylib
  -       audio-service
  -       keyboard-service
  -       mouse-service
  -       physics-service
  -       video-service
-       audio-service
-       keyboard-service
-       mouse-service
-       physics-service
-       video-service


Scripting
-       action-callback
-       action
-       change-scene
-       check-over-action
-       collide alien
-       shoot bullet
-       collide alien and my spaceship
-       control  ship
-       draw bullets
-       move alien
-       draw dialog action
-       draw hud action
-       draw my ship action
-       end drawing action
-       initialize devices
-       load assets action
-       move bullet action
-       move my spaceship action
-       move alien action
-       play sound action
```
