import pygame
import config

"""
Represents items found in the game.
"""

class Item:
    def __init__(self, name,image, description, value):
        self.description = description
        #self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.name = name
        self.value = value
        #self.image = pygame.image.load("test.png" )
        #self.image = pygame.transform.scale(self.image, (16*2, 16*2))

class Sword(Item):
    def __init__(self, name,image, description, level, health, mana, damage, crit,value):
        super().__init__(name,image, description,value)
        self.level = level
        self.health = health
        self.mana = mana
        self.damage = damage
        self.crit = crit

class Potion(Item):
    def __init__(self, name,image, description, health, mana, damage, crit, value):
        super().__init__(name,image, description,value)
        self.health = health
        self.mana = mana
        self.damage = damage
        self.crit = crit

class Key(Item):
    def __init__(self, name,image, description, value,unlock_chest):
        super().__init__(name,image, description,value)
        self.unlock_chest = unlock_chest