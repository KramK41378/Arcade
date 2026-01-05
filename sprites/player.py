import arcade
from typing_extensions import Literal

from constants import PLAYER_SPEED


class V1(arcade.SpriteSolidColor):
    def __init__(self, x: float, y: float, speed: int = PLAYER_SPEED):
        super().__init__(40, 100, x, y, arcade.types.Color(128, 128, 128))
        self.speed = speed

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self, delta_time: float = 1 / 60, *args, **kwargs):
        self.change_x = 0
        self.change_y = 0

        if self.moving_right:
            self.change_x = self.speed
        if self.moving_left:
            self.change_x -= self.speed
        if self.moving_up:
            self.change_y = self.speed
        if self.moving_down:
            self.change_y -= self.speed

        super().update()
