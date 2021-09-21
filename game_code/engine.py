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
    dungeon = Dungeon(screen, player)


    def __init__(self):

        return

    def game_loop(self):
        self.give_player_random_item(self.player.level)
        self.dungeon = Dungeon(self.screen, self.player)

        paused = False
        running = True

        while running:
            self.screen.fill(const.black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_i:
                        self.player_backpack_ui.toggle()
                    if event.key == K_k:
                        self.dungeon.toggle()
                    if event.key == K_ESCAPE:
                        if paused:
                            paused = False
                        else:
                            paused = True
                    if event.key == K_h:
                        self.player.current_health = self.player.get_player_max_health()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.player_backpack_ui.handle_right_click(self.player)
                        self.dungeon.combat_UI.right_click_handler()
                    if event.button == 1:
                        self.dungeon.combat_UI.left_click_handler(pygame.mouse.get_pos())

            if paused:
                font = pygame.font.SysFont("comicsansms", 64)
                font.set_bold(True)
                item_text = font.render("PAUSED", True, const.red)
                self.screen.blit(item_text, (220, 100))


            self.dungeon.handle_dungeon_ui()
            self.player_backpack_ui.handle_backpack_ui(self.player)
            self.player_ui.handle_player_ui(self.player)

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