from PPlay.sprite import Sprite;
from PPlay.gameobject import GameObject

class Button(GameObject):

    def __init__(self, sprite_end: str, event):
        self.sprite_end = sprite_end
        self.sprite = Sprite(sprite_end)
        self.event = event

    def Update(self, mouse):
        self.sprite.draw()
        if mouse.is_over_object(self.sprite) and mouse.button_down(1):
            self.event()