from pygame import Rect

from Entity import Entity


class Block(Entity):

    def __init__(self, x: int, y: int):
        self.rect = Rect(x, y, 32, 32)
        super().__init__()
