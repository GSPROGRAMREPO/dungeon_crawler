import pygame
import game_code.dungeon_image_loader as image_loader
import random
from game_code.enemy import Enemy


class Dungeon():
    screen = None
    dungeon_frame = None

    background = None
    sky_ground = None
    middle_ground = None
    floor = None

    player = None
    enemy = None

    def __init__(self, engine_screen, player):
        self.screen = engine_screen
        self.dungeon_frame = pygame.image.load("sprites/Dungeon/dungeon_frame.png")

        self.background = random.choice(image_loader.backgrounds)
        self.sky_ground = random.choice(image_loader.sky_grounds)
        self.middle_ground = random.choice(image_loader.middle_grounds)
        self.floor = random.choice(image_loader.floors)
        self.enemy = Enemy(1)
        self.player = player


    def update_dungeon_ui(self):
        self.display_graphics()
        self.screen.blit(self.dungeon_frame, (288, 32))

    def display_graphics(self):
        self.screen.blit(self.background, (288, 32))
        self.screen.blit(self.sky_ground, (288, 32))
        self.screen.blit(self.middle_ground, (288, 32))
        self.display_hero()
        self.screen.blit(self.floor, (288, 32))


    def display_hero(self):
        self.screen.blit(self.player.get_player_sprite(), (288, 32))
