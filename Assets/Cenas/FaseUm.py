#PPLAY IMPORTS
from PPlay.scenemanager import Scene, SceneManager

#CLASSES AUTORAIS


class FaseUm(Scene):
    def __init__(self):
        super().__init__()

    def loop(self):
        if self.teclado.key_down("ESC"):
            from Assets.Cenas.Menu import Menu
            SceneManager.change_scene(Menu())

    def draw(self):
        self.janela.set_background_color((0, 0, 0))