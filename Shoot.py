import pygame

from PPlay.sprite import Sprite
from PPlay.gameobject import GameObject

class Shoot(GameObject):

    def __init__(self, janela,  x, y):
        self.sprite = Sprite("Assets/Sprites/Player/plasma_1.png")
        self.speed = 300
        self.janela = janela
        self.sprite.set_position(x, y)

    def Update(self):
        self.sprite.y -= self.speed*self.janela.delta_time()
