from pygame import *

from maze import Maze
from plataform import Platform, ExitBlock
from Player import Player

import pygame
import os

# https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

WIN_WIDTH = 896
WIN_HEIGHT = 736
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l +HALF_WIDTH, -t +HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l +HALF_WIDTH, -t +HALF_HEIGHT, w, h

    l = min(0, l)  # stop scrolling at the left edge
    l = max(-(camera.width -WIN_WIDTH), l)  # stop scrolling at the right edge
    t = max(-(camera.height -WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)  # stop scrolling at the top
    return Rect(l, t, w, h)


def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    up = down = left = right = running = False

    maze = Maze(32, 32)
    maze.background.convert()
    maze.background.fill(Color("#000000"))
    maze.entities.add(maze.player)
    maze.build()

    total_level_width = len(maze.level[0]) * 32
    total_level_height = len(maze.level) * 32
    camera = Camera(complex_camera, total_level_width, total_level_height)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        # draw background
        maze.draw_screen(screen)

        camera.update(maze.player)

        # update player, draw everything else
        maze.player.update(up, down, left, right, running, maze.platforms)
        for e in maze.entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


if __name__ == "__main__":
    main()
