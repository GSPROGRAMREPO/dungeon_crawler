import pygame
from game_code import constants as const


class BackpackUI:
    screen = None
    stat_frame = None
    font = None
    item_frame = None


    def __init__(self, engine_screen):
        self.screen = engine_screen
        self.stat_frame = pygame.image.load("sprites/ui/UI_BOX.png")
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.name_font = pygame.font.SysFont("comicsansms", 16)
        self.item_frame = pygame.image.load("sprites/ui/UI_ITEM_BOX.png")

    def update_backpack_ui(self, player):
        self.display_frames()
        self.display_items_in_backpack(player.get_backpack_items())
        self.display_hover_information(player.get_backpack_items())

    def display_frames(self):

        # Blit the frames to the screen
        for frame in const.bpack_frame_locations:
            self.screen.blit(self.item_frame, frame)

    def display_items_in_backpack(self, items_in_back_pack):

        # Blit current Items
        for index, item in enumerate(items_in_back_pack):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, const.bpack_frame_locations[index])

    def display_hover_information(self, back_pack):
        self.font.set_bold(True)

        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()
        text_pos = (mouse_pos[0] + 16), (mouse_pos[1] + 8)

        for index, item in enumerate(back_pack):
            item_rect = pygame.Rect(const.bpack_frame_locations[index], (const.sprite_size))
            if self.is_over(item_rect, mouse_pos):
                self.screen.blit(self.stat_frame, mouse_pos)
                item_text = self.font.render(str(back_pack[index].item_description()),
                                             True, const.black)
                self.screen.blit(item_text, text_pos)

    @staticmethod
    def is_over(rect, pos):
        # function takes a tuple of (x, y) coords and a pygame.Rect object
        # returns True if the given rect overlaps the given coords
        # else it returns False
        return True if rect.collidepoint(pos[0], pos[1]) else False

    def handle_right_click(self, player):
        mouse_pos = pygame.mouse.get_pos()
        items_worn = player.get_current_items()

        for index, item in enumerate(items_worn):
            item_rect = pygame.Rect(const.worn_item_frame_locations[index], const.sprite_size)
            if self.is_over(item_rect, mouse_pos):
                if (items_worn[index] is not None):
                    if items_worn[index].slot == 'Armor':
                        player.back_pack.append(items_worn[index])
                        player.current_items[items_worn[index].type] = None

                    elif items_worn[index].slot == 'Weapon':
                        player.back_pack.append(items_worn[index])
                        player.current_items[items_worn[index].slot] = None


        for index, item in enumerate(player.back_pack):
            item_rect = pygame.Rect(const.bpack_frame_locations[index], (const.sprite_size))
            if self.is_over(item_rect, mouse_pos):
                if item.slot == 'Armor':
                    if player.current_items[item.type] == None:
                        player.current_items[item.type] = item
                        player.back_pack.remove(item)
                if item.slot == 'Weapon':
                    if player.current_items[item.slot] == None:
                        player.current_items[item.slot] = item
                        player.back_pack.remove(item)


        return