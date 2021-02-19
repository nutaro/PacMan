import json
import os

from pygame import Surface, image
from pygame.sprite import Group

from Entity import Entity
from Player import Player
from plataform import Platform, ExitBlock, PointBlock


class Maze:

    def __init__(self, x: int, y: int) -> None:
        self._player = Player(x, y)
        self._block = image.load(os.path.join('', 'img/block.png'))
        self._point_block = image.load(os.path.join('', 'img/points.png'))
        self._entities = Group()
        self._platforms = list()
        self._level = json.load(open("maze.json", "rb"))
        self._surface = Surface((x, y))

    @property
    def background(self) -> Surface:
        return self._surface

    @property
    def level(self) -> json:
        return self._level

    @property
    def player(self) -> Player:
        return self._player

    @property
    def platforms(self) -> list:
        return self._platforms

    @property
    def entities(self) -> Entity:
        return self._entities

    def build_platform(self):
        row_number = col_number = 0
        for row in self._level:
            for col in row:
                if col not in ["0", "E"]:
                    platform = PointBlock(row_number, col_number, self._point_block)
                if col == "0":
                    platform = Platform(row_number, col_number, self._block)
                if col == "E":
                    platform = ExitBlock(row_number, col_number, self._block)
                self._entities.add(platform)
                self._platforms.append(platform)
                row_number += 32
            col_number += 32
            row_number = 0

    def draw_screen(self, screen) -> None:
        for y in range(32):
            for x in range(32):
                screen.blit(self.background, (x * 32, y * 32))
