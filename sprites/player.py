import arcade
from typing_extensions import Literal

SPEED: int = 200

class V1(arcade.SpriteSolidColor):
    def __init__(self, x, y):
        super().__init__(40, 100, x, y, arcade.types.Color(128, 128, 128))
        self.y = y
        self.speed = SPEED

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self, delta_time: float = 1 / 60, *args, **kwargs):
        self.change_x = 0
        self.change_y = 0

        if self.moving_right:
            self.change_x = SPEED
        if self.moving_left:
            self.change_x -= SPEED
        if self.moving_up:
            self.change_y = SPEED
        if self.moving_down:
            self.change_y -= SPEED

        super().update()