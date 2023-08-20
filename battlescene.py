import pygame
import sys
import config
import random
import time
from dialog import Dialog
import random

"""
Setsup, displays, handles and carries out a battle between player and enemy.
"""

class BattleScene:
    def __init__(self, screen, player, enemy):
        self.player = player
        self.enemy = enemy
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.player_image = player.portrait
        self.player_image = pygame.transform.scale(self.player_image, (config.SCALE*5, config.SCALE*5))
        self.enemy_image = enemy.portrait
        self.enemy_image = pygame.transform.scale(self.enemy_image, (config.SCALE*5, config.SCALE*5))
        self.swords = pygame.transform.scale(pygame.image.load("images/other/swords.png"), (config.SCALE*5, config.SCALE*5))
        self.turn = 1
        self.player_turn = True
        self.user_input = 0


    def draw_battle_scene(self):
        self.screen.fill(config.BLACK)  

        self.rect3 = pygame.Rect(config.SCREEN_WIDTH/2-self.swords.get_width()/2,150,self.swords.get_width(),self.swords.get_height())
        self.screen.blit(self.swords, self.rect3)

        self.rect = pygame.Rect(30,65,self.player_image.get_width(),self.player_image.get_height())
        self.screen.blit(self.player_image, self.rect)

        dia = Dialog(self.screen)

        health_text = self.font.render(f"Health: {self.player.health}", True, config.WHITE)
        mana_text = self.font.render(f"Mana: {self.player.mana}", True, config.WHITE)
        damage_text = self.font.render(f"Damage: {str(self.player.sword.damage[0])}" + " - " + f"{str(self.player.sword.damage[1])}", True, config.WHITE)
        name_text = self.font.render(f"{self.player.name}   (lvl {self.player.level})", True, config.WHITE)

        self.screen.blit(name_text, (self.rect.x+self.rect.x+10, 20))
        self.screen.blit(health_text, (self.rect.x+self.rect.x, self.rect.y + self.rect.height + 50 ))
        self.screen.blit(mana_text, (self.rect.x+self.rect.x, self.rect.y + self.rect.height + 80))
        self.screen.blit(damage_text, (self.rect.x+self.rect.x, self.rect.y + self.rect.height + 110))

        self.rect2 = pygame.Rect(config.SCREEN_WIDTH-self.enemy_image.get_width()-30,65,self.enemy_image.get_width(),self.enemy_image.get_height())
        self.screen.blit(self.enemy_image, self.rect2)

        health_text2 = self.font.render(f"Health: {self.enemy.health}", True, config.WHITE)
        mana_text2 = self.font.render(f"Mana: {self.enemy.mana}", True, config.WHITE)
        damage_text2 = self.font.render(f"Damage: {str(self.enemy.damage[0])}" + " - " + f"{str(self.enemy.damage[1])}", True, config.WHITE)
        name_text2 = self.font.render(f"{self.enemy.name}   (lvl {self.enemy.level})", True, config.WHITE)

        self.screen.blit(name_text2, (self.rect2.x + 45, 20))
        self.screen.blit(health_text2, (self.rect2.x + 40, self.rect2.y + self.rect2.height + 50 ))
        self.screen.blit(mana_text2, (self.rect2.x+ 40, self.rect2.y + self.rect2.height + 80))
        self.screen.blit(damage_text2, (self.rect2.x+ 40, self.rect2.y + self.rect2.height + 110))

        pygame.display.flip()

    def battle_update(self):
        dia = Dialog(self.screen) 
        self.player_turn = True
        while self.player_turn:    
            self.draw_battle_scene()
            if(self.turn == 1):
                user_input = dia.dialog_loop2(["Attack", "Spells", "Items", "Escape"])
                print(user_input)
                if user_input == 0:
                    self.attack(self.player,self.enemy,1,None)
                    self.turn = 2
                elif user_input == 1:
                    self.spell()
                    self.turn = 2
                elif user_input == 2:
                    dia.draw_text_dialog("You don't have any items to use")
                elif user_input == 3:
                    if(self.player.level > self.enemy.level):
                        dia.draw_text_dialog("You escaped successfully!")
                        self.player_turn = False
                        return
                    else:
                        dia.draw_text_dialog("Escape failed!")
                        self.turn = 2
            elif(self.turn == 2):
                self.attack(self.enemy,self.player,1,None)
                self.turn = 1

        
    def attack(self, character, target, type, spell):
        dia = Dialog(self.screen)
        total_dmg = 0
        if(type == 1):
            total_dmg = random.randint(character.damage[0], character.damage[1])
            target.health = target.health - total_dmg
            dia.draw_text_dialog(character.name + " attacked " + target.name + f" dealing {total_dmg} damage")
        elif(type == 2):
            total_dmg = spell.damage
            character.mana = character.mana - spell.mana
            target.health = target.health - total_dmg
            dia.draw_text_dialog(character.name + " cast " + spell.name + " on " + target.name + ", dealing "+f" {total_dmg} damage")
        if(target.health < 1):
            self.draw_battle_scene()
            self.victory(character, target)

    def spell(self):
        dia = Dialog(self.screen)
        user_input = dia.dialog_loop2(self.player.spellbook_names)        
        print(user_input)
        if user_input == 0 and self.player.mana >= self.player.spellbook[0].mana:
            self.attack(self.player,self.enemy,2,self.player.spellbook[0])
            self.turn = 2
        elif user_input == 1 and self.player.mana >= self.player.spellbook[1].mana:
            self.attack(self.player,self.enemy,2,self.player.spellbook[1])
            self.turn = 2
        elif user_input == 3:
            self.player_turn = False


    def victory(self, victor, loser):
        dia = Dialog(self.screen)
        dia.draw_text_dialog(victor.name + " has defeated " + loser.name+"!")
        if victor == self.enemy:
            self.screen.fill(config.WHITE)
            self.screen.blit(self.font.render("Game Over", True, config.BLACK), (config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()  
        else:

            victor.experience = victor.experience + loser.get_experience()
            dia.draw_text_dialog(victor.name + " gained " + str(loser.get_experience()) + " experience")
            status = victor.update_experience()
            if status == 1:
                dia.draw_text_dialog(victor.name + " leveled up! Your maximum health is increased by 10 and mana by 5")

            loot_recieved = loser.get_loot()
            if loot_recieved != None:
                victor.add_item(loot_recieved)
                dia.draw_text_dialog(victor.name +  " looted "  + loot_recieved.name)
            gold_recieved = loser.get_gold()
            if gold_recieved > 0:
                victor.gold = victor.gold + gold_recieved
                dia.draw_text_dialog(victor.name +  " found "  + str(gold_recieved) + " gold")
                
            self.player_turn = False
