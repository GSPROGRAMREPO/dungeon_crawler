import pygame
class Player():
    name = "Gavin"
    level = 1

    #Inventory Stuff
    current_items = {'Helmet': None, 'Weapon': None,
                     'Chest': None, 'Gloves': None,
                     'Legs': None, 'Boots': None}

    back_pack = []

    #Stat Stuff
    base_health = 100
    total_health = 100

    defence = 0
    mana = 100
    speed = 0


    def get_current_items(self):
        # Structured list needed in order to keep certain item types in certain slots
        list_of_items = (self.current_items['Helmet'], self.current_items['Weapon'],
                        self.current_items['Chest'], self.current_items['Gloves'],
                        self.current_items['Legs'], self.current_items['Boots'])
        return list_of_items

    def get_backpack_items(self):
        list_to_return = self.back_pack
        return list_to_return

    def get_player_health_multiplier(self):
        total_multiplier_value = 1
        for i in self.current_items:
            if self.current_items[i] == None:
                continue
            else:
                total_multiplier_value = total_multiplier_value + self.current_items[i].health_multiplier

        return round(total_multiplier_value, 2)

    def get_player_health(self):
        self.total_health = round(self.base_health * self.get_player_health_multiplier())

        return self.total_health

    def get_player_defence(self):
        total_defence_value = 0
        for i in self.current_items:
            if self.current_items[i] == None:
                continue
            else:
                total_defence_value = total_defence_value + self.current_items[i].defence

        return total_defence_value

    def get_player_sprite(self):
        sprite = pygame.image.load('sprites/Dungeon/hero.png')
        return sprite
