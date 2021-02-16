from pygame import Rect
from Entity import Entity


class Platform(Entity):
    def __init__(self, x: int, y: int, image=None) -> None:
        super().__init__()
        self.image = image
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass
