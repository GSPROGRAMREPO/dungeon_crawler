from game_code.item import Item
import random

'''
    slot = ''
    type = ''
    tier = ''
    sprite_path = ''

    # Stats given to player
    hp = 0
    defence = 0
    weight = 0
    physical_damage = 0
    
'''


def item_generator(difficulty_tier):

    fns = [armor_generator(1), weapon_generator(1)]
    generated_item = random.choice(fns)

    return generated_item

def armor_generator(difficulty_tier):
    tier_dict = {1:'Copper', 2: 'Iron', 3: 'Steel'}
    slot = ('Armor')
    possible_types = ('Boots', 'Chest', 'Gloves', 'Helmet', 'Legs')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot,type,tier)
    return generated_item

def weapon_generator(difficulty_tier):
    tier_dict = {1: 'Copper', 2: 'Iron', 3: 'Steel'}

    slot = ('Weapon')
    possible_types = ('Sword', 'Axe', 'Dagger')
    type = random.choice(possible_types)
    tier = tier_dict[1]

    generated_item = Item(slot, type, tier)


    return generated_item