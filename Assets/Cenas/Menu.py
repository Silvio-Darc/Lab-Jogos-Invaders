#PPLAY IMPORTS
from PPlay.scenemanager import Scene, SceneManager

#GENERIC IMPORTS
import importlib

#CLASSES AUTORAIS
from Button import Button

class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.fundo = (10, 10, 30)

        self.jogar = Button(
            "Assets/Sprites/UI/Jogar.png",
            lambda: SceneManager.change_scene("FaseUm")
        )
        self.jogar.sprite.set_position(300, 250)  # Posicione o botão

        self.dificuldade = Button(
            "Assets/Sprites/UI/Dificuldade.png",
            lambda: SceneManager.change_scene("EscolherDificuldade")
        )
        self.dificuldade.sprite.set_position(300, 310)  # Posicione o botão

        self.ranking = Button(
            "Assets/Sprites/UI/Ranking.png",
            lambda: print("Hello world")
        )
        self.ranking.sprite.set_position(300, 370)  # Posicione o botão

        self.sair = Button(
            "Assets/Sprites/UI/Sair.png",
            lambda: self.janela.close()
        )
        self.sair.sprite.set_position(300, 430)  # Posicione o botão


    def loop(self):
        # O botão precisa ser atualizado para checar o clique
        self.jogar.Update(self.mouse)
        self.dificuldade.Update(self.mouse)
        self.ranking.Update(self.mouse)
        self.sair.Update(self.mouse)


    def draw(self):
        self.janela.set_background_color(self.fundo)

    def change_to_scene(self, scene_name):
        # 1. Constrói o caminho do módulo (Ex: Assets.Cenas.FaseUm)
        module_path = f"Assets.Cenas.{scene_name}"
        
        # 2. Importa o módulo dinamicamente (resolve o erro circular)
        module = importlib.import_module(module_path)
        
        # 3. Pega a classe dentro do módulo (Ex: module.FaseUm)
        scene_class = getattr(module, scene_name)
        
        # 4. Muda a cena instanciando a classe
        SceneManager.change_scene(scene_class())
