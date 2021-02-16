from Entity import Entity
from pygame import Color, Rect
from plataform.block import Block


class NoneBlock(Block):

    def __init__(self, x: int, y: int, ):
        super().__init__()
        self.image.fill(Color("#007bff"))
