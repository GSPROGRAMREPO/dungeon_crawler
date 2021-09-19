import pygame
import game_code.dungeon_image_loader as images
import random
from game_code.enemy import Enemy


class Dungeon():
    screen = None
    dungeon_frame = None

    background = None
    sky_ground = None
    middle_ground = None
    floor = None

    arrow_button = None

    player = None
    enemy = None

    def __init__(self, engine_screen, player):
        self.screen = engine_screen
        self.dungeon_frame = pygame.image.load("sprites/Dungeon/dungeon_frame.png")
        self.arrow_button = pygame.image.load('sprites/Dungeon/right_arrow.png')

        self.background = random.choice(images.backgrounds)
        self.sky_ground = random.choice(images.sky_grounds)
        self.middle_ground = random.choice(images.middle_grounds)
        self.floor = random.choice(images.floors)

        self.enemy = Enemy(1)
        self.player = player


    def update_dungeon_ui(self):
        mouse_pos = pygame.mouse.get_pos()
        self.display_graphics()
        self.display_buttons()
        self.screen.blit(self.dungeon_frame, (288, 32))

    def display_graphics(self):
        self.screen.blit(self.background, (288, 32))
        self.screen.blit(self.sky_ground, (288, 32))
        self.screen.blit(self.middle_ground, (288, 32))
        self.display_hero()
        self.screen.blit(self.floor, (288, 32))
        self.display_buttons()
        self.display_enemy()


    def display_hero(self):
        self.screen.blit(self.player.get_player_sprite(), (288, 32))

    def display_buttons(self):
        self.display_right_button()
        self.display_left_button()

    def display_right_button(self):
        self.screen.blit(self.arrow_button, (580, 210))

    def display_left_button(self):
        left_arrow = pygame.transform.flip(self.arrow_button, True, False)
        self.screen.blit(left_arrow, (283, 210))

    def display_enemy(self):
        self.screen.blit(self.enemy.get_enemy_sprite(), (288, 32))
