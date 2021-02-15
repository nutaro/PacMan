import json
import os
import pygame

from pygame import Surface

from Entity import Entity
from Player import Player
from plataform import Platform, ExitBlock


class Maze:

    def __init__(self, x: int, y: int) -> None:
        self._players = Player()
        self._block = pygame.image.load(os.path.join('', 'img/block.png'))
        self._entities = pygame.sprite.Group()
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
        return self._players

    @property
    def platforms(self) -> list:
        return self._platforms

    @property
    def entities(self) -> Entity:
        return self._entities

    def build(self):
        x = y = 0
        # build the level
        for row in self._level:
            for col in row:
                if col not in ["0", "E"]:
                    platform = Platform(x, y, pygame.image.load(os.path.join('', 'img/block2.png')))
                if col == "0":
                    platform = Platform(x, y, self._block)
                if col == "E":
                    platform = ExitBlock(x, y)
                self._entities.add(platform)
                self._platforms.append(platform)
            x += 32
        y += 32
        x = 0

    def draw_screen(self, screen: object) -> None:
        for y in range(32):
            for x in range(32):
                screen.blit(self.background, (x * 32, y * 32))
