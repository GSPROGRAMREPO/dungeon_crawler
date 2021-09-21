import pygame
from game_code import constants as const


class PlayerUI:
    screen = None
    stat_frame = None
    font = None
    name_font = None

    def __init__(self, engine_screen):
        self.screen = engine_screen
        self.stat_frame = pygame.image.load("sprites/ui/UI_BOX.png")
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.name_font = pygame.font.SysFont("comicsansms", 16)


    def display_frames(self):
        # Build UI frames
        item_frame = pygame.image.load("sprites/ui/UI_ITEM_BOX.png")

        # Blit the frames to the screen
        for frame in const.worn_item_frame_locations:
            self.screen.blit(item_frame, frame)


    def update_player_ui(self, player):
        self.display_frames()
        self.show_whats_worn(player.get_current_items())
        self.show_char_stats(player)
        self.display_hover_information(player)

    def show_whats_worn(self, current_items):

        # Blit current Items
        for index, item in enumerate(current_items):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, const.worn_item_frame_locations[index])

        return

    def show_char_stats(self, player):

        self.screen.blit(self.stat_frame, (32, 128))

        # Display Character Name
        name_text = self.name_font.render(player.name, True, (0, 0, 0))
        self.screen.blit(name_text, (40, 132))

        # Display Character HP
        hp_text = self.font.render('HP: ' + (str(player.current_health)), True, const.black)
        self.screen.blit(hp_text, (40, 158))

        # Display Character HP
        mana_text = self.font.render('MANA: ' + (str(player.mana)), True, const.black)
        self.screen.blit(mana_text, (40, 170))

        defence_text = self.font.render('DEF: ' + (str(player.get_player_defence())), True, const.black)
        self.screen.blit(defence_text, (40, 182))

        return

    def display_hover_information(self, player):
        self.font.set_bold(True)

        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        text_pos = (mouse_pos[0] + 16), (mouse_pos[1] + 8)

        items_worn = player.get_current_items()

        for index, item in enumerate(items_worn):
            item_rect = pygame.Rect(const.worn_item_frame_locations[index], const.sprite_size)
            if self.is_over(item_rect, mouse_pos):
                if (items_worn[index] is not None):
                    self.screen.blit(self.stat_frame, mouse_pos)
                    # Test Code
                    stats_to_print = items_worn[index].item_description()
                    self.print_item_stats(stats_to_print, text_pos)


    def print_item_stats(self, stats, text_pos):
        y_offset = 16

        for index, stat in enumerate(stats):
            if index != 0:
                text_pos = (text_pos[0], (text_pos[1] + (y_offset)))
            item_text = self.font.render(str(stat), True, const.black)
            self.screen.blit(item_text, text_pos)

    @staticmethod
    def is_over(rect, pos):
        # function takes a tuple of (x, y) coords and a pygame.Rect object
        # returns True if the given rect overlaps the given coords
        # else it returns False
        return True if rect.collidepoint(pos[0], pos[1]) else False





