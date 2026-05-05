#PPLAY IMPORTS
import json

from PPlay.window import Window
from PPlay.scenemanager import Scene, SceneManager

#CLASSES AUTORAIS
from Button import Button
from Player import Player

#CENAS


class EscolherDificuldade(Scene):
    def __init__(self):
        super().__init__()
        self.fundo = (10, 10, 30)

        self.facil = Button(
            "Assets/Sprites/UI/Facil.png",
            lambda: print("Hello world")
        )
        self.facil.sprite.set_position(300, 250)  # Posicione o botão

        self.medio = Button(
            "Assets/Sprites/UI/Medio.png",
            lambda: print("Hello world")
        )
        self.medio.sprite.set_position(300, 310)  # Posicione o botão

        self.dificil = Button(
            "Assets/Sprites/UI/Dificil.png",
            lambda: print("Hello world")
        )
        self.dificil.sprite.set_position(300, 370)  # Posicione o botão

    def loop(self):
        # O botão precisa ser atualizado para checar o clique
        self.facil.Update(self.mouse)
        self.medio.Update(self.mouse)
        self.dificil.Update(self.mouse)
        if self.teclado.key_down("ESC"):
            from Assets.Cenas.Menu import Menu
            SceneManager.change_scene(Menu())

    def changeDifficulty(self, difficulty):
        pass
