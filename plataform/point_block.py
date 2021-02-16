from pygame import Color
from plataform import Platform


class PointBlock(Platform):

    def __init__(self, x: int, y: int, image):
        super().__init__(x, y, image)

    def update(self):
        pass
