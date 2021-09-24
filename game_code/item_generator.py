from game_code.item import Item
import random


def item_generator(player_level):

    fns = [armor_generator(player_level), weapon_generator(player_level), accessory_generator(player_level)]
    generated_item = random.choice(fns)

    return generated_item

def armor_generator(player_level):
    tier_dict = {1:'Regular'}
    slot = ('Armor')
    possible_types = ('Boots', 'Chest', 'Gloves', 'Helmet', 'Legs')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot,type,tier)

    generated_item.health_multiplier = add_item_health_multi(player_level)
    generated_item.weight = add_item_weight()
    generated_item.defence = add_item_defence(generated_item.weight)


    return generated_item

def weapon_generator(player_level):
    tier_dict = {1: 'Regular'}
    slot = ('Weapon')
    possible_types = ('Sword', 'Axe', 'Dagger')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot, type, tier)

    generated_item.weight = add_item_weight()
    generated_item.physical_damage = add_weapon_physical_damage()

    return generated_item

def accessory_generator(player_level):
    tier_dict = {1: 'Regular'}
    slot = ('Armor')
    possible_types = ('Amulet', 'Ring')
    type = random.choice(possible_types)
    tier = tier_dict[1]
    generated_item = Item(slot, type, tier)

    return generated_item

def add_item_health_multi(player_level):
    multiplier = (random.randint(0,25)/100)*player_level
    return multiplier

def add_item_weight():
    weight = (random.randint(1, 10))
    return weight

def add_item_defence(weight):
    defence = (random.randint(1, 10)*weight)
    return defence

def add_weapon_physical_damage():
    damage = (random.randint(20, 40))
    return damage
