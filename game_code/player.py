class Player():
    name = "Gavin"

    #Inventory Stuff
    current_items = {'Helmet': None, 'Weapon': None,
                     'Chest': None, 'Gloves': None,
                     'Legs': None, 'Boots': None}

    back_pack = []

    #Stat Stuff
    health = 100
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