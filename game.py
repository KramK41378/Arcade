import arcade


class Game(arcade.Window):
    def __init__(self, speed):
        super().__init__(800, 600, 'free Ultrakill clone')
        self.v1: V1 = V1(self.center_x, self.center_y)
        self.player_list: arcade.SpriteList = arcade.SpriteList()
        self.player_list.append(self.v1)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_update(self, delta_time: float) -> bool | None:
        self.player_list.update()

    def on_key_press(self, symbol, modifiers):
        print('key pressed')
        if symbol == arcade.key.SPACE:
            self.v1.jump = True if self.v1.in_air is False else False
        if symbol == arcade.key.D:
            self.v1.moving_right = True
        if symbol == arcade.key.A:
            self.v1.moving_left = True
        if symbol == arcade.key.LCTRL:
            if self.v1.in_air:
                self.v1.slam = True
            else:
                self.v1.sliding = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.v1.moving_right = False
            if not self.v1.sliding:
                self.v1.sliding_direction = 'right'
        if symbol == arcade.key.A:
            self.v1.moving_left = False
            if not self.v1.sliding:
                self.v1.sliding_direction = 'left'
        if symbol == arcade.key.LCTRL:
            if self.v1.sliding:
                self.v1.sliding = False

def main():
    game = Game(200)
    arcade.run()