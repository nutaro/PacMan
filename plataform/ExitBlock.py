from plataform.Platform import Platform
from pygame import Color


class ExitBlock(Block):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.rect = Rect(x, y, 32, 32)
        self.image.fill(Color("#0033FF"))
