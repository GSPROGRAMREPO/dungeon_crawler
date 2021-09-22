import pygame
from game_code import constants as const, item_generator
from game_code.ui import UI

class LootUI(UI):

    player_level = None
    enemy = None
    font = None
    all_loot = []

    is_looting = False

    loot_frame_positions = [(480, 32), (512, 32), (544, 32),
                            (480, 64), (512, 64), (544, 64),
                            (480, 96), (512, 96), (544, 96)]


    def __init__(self, screen, player_level, back_pack):

        super().__init__(screen)
        self.player_level = player_level
        self.player_back_pack = back_pack
        self.make_loot()

        return

    def make_loot(self):
        while len(self.all_loot) < 3:
            test_item = item_generator.item_generator(self.player_level)
            self.all_loot.append(test_item)

    def display_loot(self):
        self.display_item_frames()
        self.display_loot_items()
        # self.display_hover_information()
        self.display_hover_information(self.all_loot, self.loot_frame_positions)

    def display_item_frames(self):
        for index, position in enumerate(self.loot_frame_positions):
            self.screen.blit(pygame.image.load('sprites/ui/UI_ITEM_BOX.png'), position)


    def display_loot_items(self):
        # Blit current Items
        for index, item in enumerate(self.all_loot):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, self.loot_frame_positions[index])


    def handle_right_click(self):
        if self.is_looting == True:
            mouse_pos = pygame.mouse.get_pos()
            for index, item in enumerate(self.all_loot):
                item_rect = pygame.Rect(self.loot_frame_positions[index], (const.sprite_size))
                if const.is_over(item_rect, mouse_pos):
                    self.player_back_pack.append(item)
                    self.all_loot.remove(item)