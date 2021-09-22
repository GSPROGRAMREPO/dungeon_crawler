import pygame
from game_code import constants as const

class UI():
    screen = None
    stat_frame = None
    font = None
    item_frame = None


    def __init__(self, screen):
        self.screen = screen
        self.stat_frame = pygame.image.load("sprites/ui/UI_BOX.png")
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.font.set_bold(True)
        self.name_font = pygame.font.SysFont("comicsansms", 16)
        self.item_frame = pygame.image.load("sprites/ui/UI_ITEM_BOX.png")

    def is_over(self, rect, pos):
        # function takes a tuple of (x, y) coords and a pygame.Rect object
        # returns True if the given rect overlaps the given coords
        # else it returns False
        return True if rect.collidepoint(pos[0], pos[1]) else False

    def display_hover_information(self, items, frame_positions):
        x_offset = 16
        y_offset = 8

        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        text_pos = (mouse_pos[0] + x_offset), (mouse_pos[1] + y_offset)

        for index, item in enumerate(items):
            item_rect = pygame.Rect(frame_positions[index], (const.sprite_size))
            if self.is_over(item_rect, mouse_pos):
                if items[index] is not None:
                    self.screen.blit(self.stat_frame, mouse_pos)
                    stats_to_print = items[index].item_description()
                    self.print_item_stats(stats_to_print, text_pos)

    def print_item_stats(self, stats, text_pos):
        y_offset = 16
        for index, stat in enumerate(stats):
            if index != 0:
                text_pos = (text_pos[0], (text_pos[1] + (y_offset)))
            item_text = self.font.render(str(stat), True, const.black)
            self.screen.blit(item_text, text_pos)
        return