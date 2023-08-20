import pygame
import config
from Item import *
from spell import Spell
from dialog import Dialog
from battlescene import BattleScene
import random

"""
- Represents characters, players, enemies, and other interactive elements within the game world.
"""

class Object():
    def __init__(self, name, image, start_position, idnr):
        self.name = name
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.start_position = start_position
        self.idnr = idnr

    def interactable(self,player,screen):
        dia = Dialog(screen)
        dia.draw_text_dialog(self.name)

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.start_position[0] * config.SCALE, self.start_position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)


class Character(Object):
    def __init__(self, name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot,gold,xp):
        super().__init__(name, image, start_position,idnr)
        self.level = level
        self.health = health
        self.mana = mana
        self.damage = damage
        self.crit = crit
        self.rect = pygame.Rect(self.start_position[0] * config.SCALE, self.start_position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.dialog = dialog
        self.portrait = pygame.image.load("images/portraits/" + self.name + ".png" )
        self.kind = kind
        self.loot = loot
        self.gold = gold 
        self.xp = xp

    def get_experience(self):
        return 3

    def get_loot(self):
        return self.loot 

    def get_gold(self):
        return self.gold 

    def interactable(self,player,screen):
        dia = Dialog(screen)
        dia.draw_text_dialog(self.dialog[0])
        ui = dia.dialog_loop(self.dialog[1])
        if(ui == 0):
            dia.draw_text_dialog(self.dialog[2])
        elif(ui == 1):
            dia.draw_text_dialog(self.dialog[3])
            battle = BattleScene(screen, player, self)
            battle.battle_update()
            return 1
        elif(ui == 2):
            dia.draw_text_dialog(self.dialog[4])

class Enemy(Character):
    def __init__(self, name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot,gold,xp):
        super().__init__(name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot,gold,xp)

    def get_gold(self):
        return self.gold

    def get_loot(self):
        return self.loot

    def interactable(self, player, screen):
        dia = Dialog(screen)
        dia.draw_text_dialog(self.dialog)
        battle = BattleScene(screen, player, self)
        battle.battle_update()
        return 1

class Player(Object):
    def __init__(self, name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr):
        super().__init__(name, image, start_position,idnr)
        self.max_mana = 30
        self.max_health = 10
        self.direction = "DOWN"
        self.experience = 0
        self.inventory = []
        self.equipped = []
        self.sword = Sword("Empty", "imgs/Items/basic_sword.png" ,"Golden", 0, 0, 0, [1,5], 0,0)
        self.position = self.start_position
        self.add_item(Sword("Staff","imgs/Items/basic_sword.png", "2 - 6 attack damage", 1, 0, 0, [2,6], 2,10))
        self.add_item(Sword("Sword","imgs/Items/basic_sword.png", "1 - 9 attack damage", 1, 0, 0, [1,5], 2,5))
        self.spellbook = []
        self.spellbook_names = []
        self.add_spell(Spell("Fireball",20,10,None))
        self.add_spell(Spell("Frost Blast",50,50,None))
        self.gold = 50
        self.portrait = pygame.image.load("images/portraits/" + self.name + ".png" )
        self.enemies_defeated = 0
        self.level = level
        self.health = health
        self.mana = mana
        self.damage = self.sword.damage
        self.crit = crit
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.start_position[0] * config.SCALE, self.start_position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.req_xp = 1

    def open_inventory(self,screen):
        dia = Dialog(screen)
        
        str_items = []
        str_description = []
        for item in self.inventory:
            str_items.append(item.name)
            str_description.append(item.description + " - " + str(item.value) + "g")
        txt = f"Inventory                                                 {self.name}'s gold: {self.gold}"
        txt2 = "B - Back                  SPACE - Equip/Use"    
        i = dia.update_menu(str_items,str_description,txt,txt2)
        if(i == -1):
            return 
        else:
            item = self.inventory[i]
            self.use_item(item,dia)

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item,dia):
        if isinstance(item, Potion):
            self.inventory.remove(item)
            if(item.health + self.health > self.max_health):
                self.health = self.max_health
            elif(item.health + self.health <= self.max_health):
                self.health = self.health + item.health
            if(item.mana + self.mana > self.max_mana):
                self.mana = self.max_mana
            elif(item.mana + self.mana <= self.max_mana):
                self.mana = self.mana + item.mana
            dia.draw_text_dialog(f"{item.name} has been used.")
        else:
            self.sword = item
            self.damage = self.sword.damage
            dia.draw_text_dialog(f"{item.name} has been equipped.")

    def update_experience(self):
        if(self.experience >= self.req_xp):
            self.level = self.level + 1
            self.experience = 0
            self.max_health = self.max_health + 10
            self.max_mana = self.max_mana + 5
            self.req_xp = self.req_xp * 2
            return 1

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def add_spell(self, spell):
        self.spellbook.append(spell)
        self.spellbook_names.append(spell.name)

class Merchant(Character):
    def __init__(self, name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot,gold,xp):
        super().__init__(name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot,gold,xp)
        self.items_to_sell = []
        self.screen = 0
        self.font = pygame.font.Font(None, 24)
        self.player = 0
        self.selected_option = 0
        self.nxt = True
        self.dialog_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6"]
        self.selected_option = 0
        self.first_visible_option = 0
        self.visible_options = 5

    def add_item_to_sell(self, item):
        self.items_to_sell.append(item)

    def interactable(self, player, screen):
        self.screen = screen
        self.player = player
        dia = Dialog(screen)

        dia.draw_text_dialog(self.dialog[0])
        ui = dia.dialog_loop(self.dialog[1])
        if ui == 0:
            print("BOOM")
            str_items = []
            str_description = []
            for item in self.items_to_sell:
                str_items.append(item.name)
                str_description.append(item.description + " - " + str(item.value) + "g")
            txt = f"Buy Items                                                 {self.player.name}'s gold: {self.player.gold}"
            txt2 = "B - Back                  SPACE - Buy"
            selected_item = dia.update_menu(str_items,str_description,txt,txt2)
            if(selected_item == -1):
                return 
            elif(self.items_to_sell[selected_item].value  > self.player.gold):
                dia.draw_text_dialog("You dont have enough gold for that!")
                
            elif(self.items_to_sell[selected_item].value <= self.player.gold):
                self.player.gold = self.player.gold - self.items_to_sell[selected_item].value
                self.player.add_item(self.items_to_sell[selected_item])
                dia.draw_text_dialog(f"{self.items_to_sell[selected_item].name} is yours!")
                print(str(self.player.gold))
        elif ui == 1:
            print("BOOM2")
            str_items = []
            str_description = []
            for item in self.player.inventory:
                str_items.append(item.name)
                str_description.append(item.description + " - " + str(item.value) + "g")
            txt = f"Sell Items                                                 {self.player.name}'s gold: {self.player.gold}"
            txt2 = "B - Back                  SPACE - Sell"
            selected_item = dia.update_menu(str_items,str_description,txt,txt2)
            if(selected_item == -1):
                return 
            else:
                self.player.gold = self.player.gold + self.player.inventory[selected_item].value
                dia.draw_text_dialog(f"{self.player.inventory[selected_item].name} sold for {self.player.inventory[selected_item].value}g!")
                self.player.inventory.remove(self.player.inventory[selected_item])
        elif ui == 2:
            print("BOOM3")
            dia.draw_text_dialog("Bring it on thief!")
            battle = BattleScene(screen, player, self)
            battle.battle_update()
            return 1
        elif(ui == 3):
            dia.draw_text_dialog("Farewell!")

class Boss(Enemy):
    def __init__(self, name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,positions, loot, gold,xp):
        super().__init__(name, image, start_position,level,health,mana,damage,crit,dialog,kind,idnr,loot, gold,xp)
        self.positions = positions
        self.loot = loot
        self.gold = gold
        self.xp = xp

    def get_gold(self):
        return self.gold 

    def get_loot(self):
        return self.loot

    def interactable(self, player, screen):
        dia = Dialog(screen)
        dia.draw_text_dialog(self.dialog)
        battle = BattleScene(screen, player, self)
        battle.battle_update()
        return 2

class Chest(Object):
    def __init__(self, name, image, start_position,idnr, loot):
        super().__init__(name, image, start_position,idnr)
        self.loot = loot

    def interactable(self, player, screen):
        dia = Dialog(screen)
        for item in player.inventory:
            if isinstance(item, Key):
                if item.unlock_chest == self.start_position:
                    dia.draw_text_dialog("The " + self.name + " got unlocked using the " + item.name)
                    dia.draw_text_dialog(player.name + " picked up " + self.loot.name)
                    player.inventory.append(self.loot)
                    return 1
        dia.draw_text_dialog(self.name + " is locked")

