import arcade

VEL_TIRO = 8

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen = True)
        arcade.set_background_color(arcade.color.AMAZON)
        self.imagem_fundo = None
        self.largura_tela = None
        self.altura_tela = None

        self.player_sprite = None

        self.set_mouse_visible(False)

        self.lista_tiros = None

    def setup(self):
        self.largura_tela, self.altura_tela = self.get_size()

        self.imagem_fundo = arcade.load_texture("imagens/space2.jpg")

        self.player_sprite = arcade.Sprite("imagens/bgbattleship.png")
        self.player_sprite.center_x = self.largura_tela // 2
        self.player_sprite.center_y = 50

        self.lista_tiros = arcade.SpriteList()

    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_texture_rectangle(self.largura_tela // 2, self.altura_tela // 2, self.largura_tela, self.altura_tela, self.imagem_fundo)
        self.player_sprite.draw()

        self.lista_tiros.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.lista_tiros.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            tiro = arcade.Sprite("imagens/laserBlue01.png")
            tiro.center_x = self.player_sprite.center_x
            tiro.center_y = self.player_sprite.center_y + 30
            tiro.angle = 90
            tiro.change_y = VEL_TIRO
            self.lista_tiros.append(tiro)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()