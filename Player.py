import pygame
import threading

from PPlay.sprite import Sprite
from PPlay.gameobject import GameObject

from Shoot import Shoot

class Player(GameObject):

    def __init__(self, speed:float, janela, dificuldade):
        self.sprite = Sprite("Assets/Sprites/Player/player_b_m.png")
        self.speed = speed
        self.janela = janela
        self.shoots = []
        self.shootCooldownTime = 0.5*dificuldade  # Tempo de espera entre tiros
        self.timer = 0

    def Update(self):
        self.timer += self.janela.delta_time()
        if self.janela.keyboard.key_pressed("Right"):
            self.onMove(1)
        elif self.janela.keyboard.key_pressed("Left"):
            self.onMove(-1)
        if self.janela.keyboard.key_pressed("Space") and self.timer >= self.shootCooldownTime:
            self.onShoot()
        for shoot in self.shoots:
            shoot.Update()
            shoot.sprite.draw()


    def onMove(self, direction):
        if 0 <= self.sprite.x and self.sprite.x <= self.janela.width-self.sprite.width:
            self.sprite.x += direction*self.speed*self.janela.delta_time()
        if self.sprite.x < 0:
            self.sprite.x = 0
        if self.sprite.x > self.janela.width-self.sprite.width:
            self.sprite.x = self.janela.width-self.sprite.width

    def manageShootCooldown(self):
        self.shootCooldown = True


    def onShoot(self):
        if self.shootCooldownTime:
            self.shoots.append(Shoot(self.janela, self.sprite.x + self.sprite.width / 2 - 5, self.sprite.y))
            self.timer = 0  # Reseta o cronômetro
