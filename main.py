import pygame
import config
from game import Game
from menu import Menu
import sys

"""
- Initialize essential components of the game, such as screen, music, framerate.
- Sets up menu loop
- Sets up game loop
"""

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Mystic Realm")

clock = pygame.time.Clock()
clock.tick(50)

music_file = "music/menu_music.mp3"
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

menu = Menu(screen)

while menu.running:
    menu.update()

pygame.mixer.music.stop()
music_file = "music/game_music.mp3"
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

game = Game(screen)

while game.running:
    game.update()
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()