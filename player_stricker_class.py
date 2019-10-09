from stricker import Stricker
from pygame import mouse

class Player_stricker(Stricker):
    def __init__(self, sprite, center, size):
        super().__init__(sprite, center, size)

    def move(self):
        self.rect.center = mouse.get_pos()