from pygame import Color, Rect

from plataform import Platform


class ExitBlock(Platform):

    def __init__(self, x: int, y: int, image):
        super().__init__(x, y, image)
        self.image.fill(Color("#0033FF"))
