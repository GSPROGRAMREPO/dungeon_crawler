from game_code.item import Item
import random


def item_generator(difficulty_tier):

    fns = [armor_generator(1), weapon_generator(1)]
    generated_item = random.choice(fns)
    generated_item.health_multiplier = add_item_health_multi(difficulty_tier)

    return generated_item

def armor_generator(difficulty_level):
    tier_dict = {1:'Copper', 2: 'Iron', 3: 'Steel'}
    slot = ('Armor')
    possible_types = ('Boots', 'Chest', 'Gloves', 'Helmet', 'Legs')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot,type,tier)
    return generated_item

def weapon_generator(difficulty_level):
    tier_dict = {1: 'Copper', 2: 'Iron', 3: 'Steel'}
    slot = ('Weapon')
    possible_types = ('Sword', 'Axe', 'Dagger')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot, type, tier)
    return generated_item

def add_item_health_multi(diff_lev):
    multiplier = (random.randint(0,25)/100)*diff_lev
    return multiplier

