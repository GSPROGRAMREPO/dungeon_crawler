import pygame

class CombatEngine():

    screen = None
    player = None
    enemy = None


    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

        return

    def resolve_player_attack(self):
        if self.enemy.is_alive() and self.player.is_alive():
            damage = self.player.get_player_attack_damage()
            self.enemy.health = self.enemy.health - damage

    def resolve_enemy_attack(self):
        if self.player.is_alive() and self.enemy.is_alive():
            damage = self.enemy.get_attack_damage()
            self.player.current_health = self.player.current_health - damage