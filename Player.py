# -*- coding: utf-8 -*-

import pygame
import os
from Entity import Entity


class Player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = pygame.image.load(os.path.join('', 'img/player.png'))
        self.rect = pygame.Rect(128, 128, x, y)

    def update(self, up, down, left, right, running, platform):
        if up:
            self.yvel -= 7
        if down:
            self.yvel = 7
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8

        if not (up or down):
            self.yvel = 0
        if not (left or right):
            self.xvel = 0

        self.rect.left += self.xvel

        self.collide(self.xvel, 0, platform)

        self.rect.top += self.yvel

        self.onGround = False

        self.collide(0, self.yvel, platform)

    def collide(self, xvel, yvel, platform):
        for p in platform:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print("collide right")
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print("collide left")
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    # self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
