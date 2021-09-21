import pygame
class Enemy():


    def __init__(self, player_level):
        return

    name = "Enemy"
    level = 1
    health = 100
    base_damage = 10

    def get_enemy_sprite(self):
        sprite = pygame.image.load('sprites/Enemies/Skeleton1.png')
        return sprite

    def get_attack_damage(self):
        damage = self.base_damage

        return damage

    def get_enemy_health(self):
        health = self.health
        return health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False