from PPlay.scenemanager import Scene, SceneManager
from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.mouse import Mouse  # Importe a classe, não *

# 1. A JANELA DEVE SER A PRIMEIRA COISA (Essencial no Linux)
janela = Window(800, 600, "Invaders")

#Cenas
from Assets.Cenas.Menu import Menu

# Inicializa o gerenciador com uma instância do Menu
SceneManager.change_scene(Menu())

while True:
    SceneManager.run()
    janela.update()
