#PPLAY IMPORTS
from PPlay.scenemanager import Scene, SceneManager

#CLASSES AUTORAIS
from Player import Player


class FaseUm(Scene):
    def __init__(self):
        super().__init__()
        self.player = Player(250, self.janela, 1)
        self.player.sprite.y = 600-self.player.sprite.height

    def loop(self):
        if self.teclado.key_down("ESC"):
            from Assets.Cenas.Menu import Menu
            SceneManager.change_scene(Menu())
        self.player.Update()

    def draw(self):
        self.janela.set_background_color((0, 0, 0))
        self.player.sprite.draw()
