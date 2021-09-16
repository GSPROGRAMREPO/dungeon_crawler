import pygame
import game_code.constants as const


class DungeonUI:
    screen = None
    dungeon_frame = None
    floor = pygame.image.load("sprites/Dungeon/basicground.png")
    middle_ground = pygame.image.load(("sprites/Dungeon/middle_ground.png"))
    sky_ground = pygame.image.load(("sprites/Dungeon/cloud_layer.png"))
    background = pygame.image.load("sprites/Dungeon/background.png")


    def __init__(self, engine_screen):
        self.screen = engine_screen
        self.dungeon_frame = pygame.image.load("sprites/Dungeon/dungeon_frame.png")

    def update_dungeon_ui(self):
        self.display_background()
        self.display_sky_ground()
        self.display_middle_ground()
        self.display_floor()

        self.screen.blit(self.dungeon_frame, (288,32))

    def display_floor(self):
        self.screen.blit(self.floor, (288,32))

    def display_middle_ground(self):
        self.screen.blit(self.middle_ground, (288,32))

    def display_sky_ground(self):
        self.screen.blit(self.sky_ground, (288, 32))

    def display_background(self):
        self.screen.blit(self.background, (288,32))

    def display_buttons(self):

        return