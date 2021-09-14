class Item():
    #Item has a name
    #Item has a sprite
    #Item has stats
    slot = ''
    type = ''
    tier = ''
    sprite_path = ''

    # Stats given to player
    hp = 0
    defence = 0
    weight = 0
    physical_damage = 0


    def __init__(self):
        return

    def __init__(self, slot, type, tier):
        self.slot = slot
        self.type = type
        self.tier = tier
        self.sprite_path = ('sprites/' + slot + '/' + type + '/' + tier + '/' + '1.png')
        return

    def item_description(self):
        description = (self.tier + ' ' + self.type)

        return description

