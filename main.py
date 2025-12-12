import arcade

class V1(arcade.SpriteSolidColor):
    def __init__(self, x, y):
        super().__init__(40, 100, x, y, arcade.types.Color(128, 128, 128))
        self.y = y
        self.jump: bool = False
        self.in_air: bool = False
        self.slam: bool = False

    def update(self, delta_time):
        if self.jump:
            self.jump = False
            self.change_y = 500
            self.in_air = True

        if self.slam:
            self.change_y = -1000
            self.change_x = 0

        if self.in_air:
            self.change_y -= 10
            if self.center_y < self.y:
                self.change_y = 0
                self.in_air = False
                self.slam = False
                self.center_y = self.y


        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time



class Game(arcade.Window):
    def __init__(self, speed):
        super().__init__(800, 600, 'free Ultrakill clone')
        self.speed = speed

    def setup(self):
        self.v1: V1 = V1(self.center_x, self.center_y)
        self.player_list: arcade.SpriteList = arcade.SpriteList()
        self.player_list.append(self.v1)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_update(self, delta_time: float) -> bool | None:
        self.player_list.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.v1.jump = True if self.v1.in_air is False else False
        if symbol == arcade.key.D:
            if not self.v1.slam:
                self.v1.change_x += self.speed
        if symbol == arcade.key.A:
            if not self.v1.slam:
                self.v1.change_x -= self.speed
        if symbol == arcade.key.LCTRL:
            if self.v1.in_air:
                self.v1.slam = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.v1.change_x -= self.speed
        if symbol == arcade.key.A:
            self.v1.change_x += self.speed

def main():
    game = Game(200)
    game.setup()
    arcade.run()

if __name__ == '__main__':
    main()