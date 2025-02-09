import pygame
from pygame_sheetcut import cut_grid
from os.path import join

pygame.init()
test_screen = pygame.display.set_mode((480, 360))

attack = pygame.image.load(join('', 'test_images', 'attack_strip10.png'))
r, c = 1, 10
frms = r * c
expected_frames = frms
frames = cut_grid(attack, r, c)
assert len(frames) == expected_frames