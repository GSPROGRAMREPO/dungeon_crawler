import sys, pygame
from game_code import constants as const, item_generator
from game_code.player import Player
from pygame.locals import *
from game_code.player_ui import PlayerUI
from game_code.backpack_ui import BackpackUI
from game_code.dungeon import Dungeon


class Engine:
    pygame.init()
    player = Player()
    screen = pygame.display.set_mode(const.screen_size)
    player_ui = PlayerUI(screen)
    player_backpack_ui = BackpackUI(screen)


    def __init__(self):

        return

    def game_loop(self):
        self.give_player_random_item(self.player.level)

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_i:
                        self.backpack_loop()

                    if event.key == K_k:
                        self.dungeon_loop()

                    if event.key == K_ESCAPE:
                        self.pause_loop()

            self.screen.fill(const.black)
            self.player_ui.update_player_ui(self.player)
            pygame.display.flip()

    def dungeon_loop(self):
        dungeon_ui = Dungeon(self.screen, self.player)

        in_dungeon = True
        while in_dungeon:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_i:
                        self.backpack_loop()

                    if event.key == K_k:
                        in_dungeon = False

                    if event.key == K_ESCAPE:
                        self.pause_loop()

            self.screen.fill(const.black)
            self.player_ui.update_player_ui(self.player)
            dungeon_ui.update_dungeon_ui()
            pygame.display.flip()

    def backpack_loop(self):
        backpack_open = True
        while backpack_open:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_i:
                        backpack_open = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.player_backpack_ui.handle_right_click(self.player)

            self.screen.fill(const.black)
            self.player_backpack_ui.update_backpack_ui(self.player)
            self.player_ui.update_player_ui(self.player)

            pygame.display.flip()

    def pause_loop(self):

        paused = True
        while paused:
            screen = pygame.display.set_mode(const.screen_size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        paused = False

            font = pygame.font.SysFont("comicsansms", 64)
            font.set_bold(True)
            item_text = font.render("PAUSED", True, const.red)

            screen.fill(const.tan)
            screen.blit(item_text, (220, 100))

            pygame.display.flip()

    def give_player_random_item(self, player_level):

        for i in range(20):

            test_item = item_generator.item_generator(player_level)

            # Handle if weapon
            if test_item.slot == 'Weapon':
                if self.player.current_items[test_item.slot] is None:
                    self.player.current_items[test_item.slot] = test_item
                    continue
                else:
                    self.player.back_pack.append(test_item)
                    continue
            # Handle if armor
            if self.player.current_items[test_item.type] is None:
                self.player.current_items[test_item.type] = test_item
                continue

            else:
                self.player.back_pack.append(test_item)
                continue