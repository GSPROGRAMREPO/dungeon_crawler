import pygame
from game_code import constants as const
from game_code.ui_code.ui import UI


class PlayerUI(UI):

    name_font = pygame.font.SysFont("comicsansms", 16)

    def handle_player_ui(self, player):
        self.display_frames(const.worn_item_frame_locations)
        self.show_whats_worn(player.get_current_items())
        self.show_char_stats(player)
        self.display_hover_information(player.get_current_items(), const.worn_item_frame_locations)

    def show_whats_worn(self, current_items):

        # Blit current Items
        for index, item in enumerate(current_items):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, const.worn_item_frame_locations[index])

        return

    def show_char_stats(self, player):

        self.screen.blit(self.stat_frame, (32, 160))

        # Display Character Name
        name_text = self.name_font.render(player.name, True, (0, 0, 0))
        self.screen.blit(name_text, (40, 160))

        # Display Character HP
        hp_text = self.font.render('HP: ' + (str(player.current_health) + ' / ' + str(player.get_player_max_health())), True, const.black)
        self.screen.blit(hp_text, (40, 190))

        # Display Character HP
        mana_text = self.font.render('MANA: ' + (str(player.mana)), True, const.black)
        self.screen.blit(mana_text, (40, 202))

        defence_text = self.font.render('DEF: ' + (str(player.get_player_defence())), True, const.black)
        self.screen.blit(defence_text, (40, 214))

        return