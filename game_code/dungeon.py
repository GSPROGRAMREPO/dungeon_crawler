import pygame
import game_code.dungeon_image_loader as images
import random


class Dungeon:
    screen = None
    dungeon_frame = None

    background = None
    sky_ground = None
    middle_ground = None
    floor = None

    hero = pygame.image.load('sprites/Dungeon/hero.png')
    arrow_button = pygame.image.load('sprites/Dungeon/right_arrow.png')

    def __init__(self, engine_screen):
        self.screen = engine_screen
        self.dungeon_frame = pygame.image.load("sprites/Dungeon/dungeon_frame.png")

        self.background = random.choice(images.backgrounds)
        self.sky_ground = random.choice(images.sky_grounds)
        self.middle_ground = random.choice(images.middle_grounds)
        self.floor = random.choice(images.floors)

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


    def display_hero(self):
        self.screen.blit(self.hero, (288, 32))

    def display_buttons(self):
        self.display_right_button()
        self.display_left_button()

    def display_right_button(self):
        self.screen.blit(self.arrow_button, (580, 210))

    def display_left_button(self):
        left_arrow = pygame.transform.flip(self.arrow_button, True, False)
        self.screen.blit(left_arrow, (283, 210))