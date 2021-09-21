import pygame
from game_code import constants as const, item_generator
class LootUI():

    screen = None
    player_level = None
    enemy = None
    font = None
    all_loot = []

    is_looting = False

    item_frame = pygame.image.load('sprites/ui/UI_ITEM_BOX.png')
    item_frame_positions = [(480,32), (512,32),(544,32),
                            (480, 64), (512, 64), (544, 64),
                            (480, 96), (512, 96), (544, 96)]


    def __init__(self, screen, player_level, back_pack):

        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.player_level = player_level
        self.player_back_pack = back_pack
        self.make_loot()
        self.stat_frame = pygame.image.load("sprites/ui/UI_BOX.png")

        return

    def make_loot(self):
        while len(self.all_loot) < 3:
            test_item = item_generator.item_generator(self.player_level)
            self.all_loot.append(test_item)

    def display_loot(self):
        self.display_item_frames()
        self.display_loot_items()
        self.display_hover_information()

    def display_item_frames(self):
        for index, position in enumerate(self.item_frame_positions):
            self.screen.blit(pygame.image.load('sprites/ui/UI_ITEM_BOX.png'), position)
            item_rect = pygame.Rect(position, (const.sprite_size))


    def display_loot_items(self):
        # Blit current Items
        for index, item in enumerate(self.all_loot):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, self.item_frame_positions[index])

    def display_hover_information(self):
        self.font.set_bold(True)
        x_offset = 16
        y_offset = 8

        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        text_pos = (mouse_pos[0] + x_offset), (mouse_pos[1] + y_offset)

        for index, item in enumerate(self.all_loot):
            item_rect = pygame.Rect(self.item_frame_positions[index], (const.sprite_size))
            if self.is_over(item_rect, mouse_pos):
                self.screen.blit(self.stat_frame, mouse_pos)
                # Test Code
                stats_to_print = self.all_loot[index].item_description()
                self.print_item_stats(stats_to_print, text_pos)

    def handle_right_click(self):
        if self.is_looting == True:
            mouse_pos = pygame.mouse.get_pos()
            for index, item in enumerate(self.all_loot):
                item_rect = pygame.Rect(self.item_frame_positions[index], (const.sprite_size))
                if self.is_over(item_rect, mouse_pos):
                    self.player_back_pack.append(item)
                    self.all_loot.remove(item)

    @staticmethod
    def is_over(rect, pos):
        # function takes a tuple of (x, y) coords and a pygame.Rect object
        # returns True if the given rect overlaps the given coords
        # else it returns False
        return True if rect.collidepoint(pos[0], pos[1]) else False

    def print_item_stats(self, stats, text_pos):
        y_offset = 16

        for index, stat in enumerate(stats):
            if index != 0:
                text_pos = (text_pos[0], (text_pos[1] + (y_offset)))
            item_text = self.font.render(str(stat), True, const.black)
            self.screen.blit(item_text, text_pos)