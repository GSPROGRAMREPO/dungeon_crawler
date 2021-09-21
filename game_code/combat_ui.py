import pygame
from game_code.combat_engine import CombatEngine
from game_code import constants as const

class CombatUI():

    screen = None
    player = None
    enemy = None

    combat_engine = None

    attack_button_position = (288, 212)
    run_button_position = (325, 212)

    font = None


    def __init__(self, screen, player, enemy):

        self.screen = screen
        self.player = player
        self.enemy = enemy

        self.attack_icon = pygame.image.load('sprites/ui/attack_icon.png')
        self.run_icon = pygame.image.load('sprites/ui/run_icon.png')

        self.combat_engine = CombatEngine(player, enemy)

        self.font = pygame.font.SysFont("comicsansms", 12)

        return

    def update_combat_ui(self):
        self.display_attack_button()
        self.display_run_button()
        self.display_enemy()
        self.display_enemy_health()

    def attack_button_pressed(self):
        self.combat_engine.resolve_player_attack()
        self.combat_engine.resolve_enemy_attack()

    def display_attack_button(self):

        self.screen.blit(pygame.image.load('sprites/ui/UI_ITEM_BOX.png'), self.attack_button_position)
        self.screen.blit(self.attack_icon,self.attack_button_position)

    def display_run_button(self):
        self.screen.blit(pygame.image.load('sprites/ui/UI_ITEM_BOX.png'), self.run_button_position)
        self.screen.blit(self.run_icon, self.run_button_position)

    def display_health_bars(self):
        self.display_player_health()
        self.display_enemy_health()

    def display_player_health(self):
        return

    def display_enemy_health(self):
        if self.enemy.is_alive():
            health_text = self.font.render(str(self.enemy.health), True, (255, 255, 255))
            self.screen.blit(health_text, (560, 212))

    def display_enemy(self):
        if self.enemy.is_alive():
            self.screen.blit(self.enemy.get_enemy_sprite(), (288, 32))

    def left_click_handler(self, mouse_pos):
        attack_rect = pygame.Rect(self.attack_button_position, const.sprite_size)
        if self.is_over(attack_rect,mouse_pos):
            self.attack_button_pressed()

        # if is over run button and leftclick
            #run button is pressed

    def loot_handler(self):

        return

    @staticmethod
    def is_over(rect, pos):
        # function takes a tuple of (x, y) coords and a pygame.Rect object
        # returns True if the given rect overlaps the given coords
        # else it returns False
        return True if rect.collidepoint(pos[0], pos[1]) else False