import pygame
from game_code import constants as const
from game_code.ui_code.ui import UI


class BackpackUI(UI):

    is_open = False

    def toggle(self):
        if self.is_open:
            self.is_open = False
        else:
            self.is_open = True
        return

    def handle_backpack_ui(self, player):
        if self.is_open:
            self.display_frames(const.bpack_frame_locations)
            self.display_items_in_backpack(player.get_backpack_items())
            self.display_hover_information(player.get_backpack_items(), const.bpack_frame_locations)

    def display_items_in_backpack(self, items_in_back_pack):
        # Blit current Items
        for index, item in enumerate(items_in_back_pack):
            if item is not None:
                item_sprite = pygame.image.load(item.sprite_path)
                self.screen.blit(item_sprite, const.bpack_frame_locations[index])

    def handle_right_click(self, player):
        if self.is_open:
            mouse_pos = pygame.mouse.get_pos()
            self.right_click_on_worn_items(player, mouse_pos)
            self.right_click_on_backp_items(player, mouse_pos)
        return

    def right_click_on_worn_items(self, player, mouse_pos):

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
        return

    def right_click_on_backp_items(self, player, mouse_pos):

        for index, item in enumerate(player.back_pack):
            item_rect = pygame.Rect(const.bpack_frame_locations[index], (const.sprite_size))
            if self.is_over(item_rect, mouse_pos):
                if item.slot == 'Armor':
                    if player.current_items[item.type] == None:
                        player.current_items[item.type] = item
                        player.back_pack.remove(item)

                elif item.slot == 'Weapon':
                    if player.current_items[item.slot] == None:
                        player.current_items[item.slot] = item
                        player.back_pack.remove(item)
        return