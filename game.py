import pygame
import config
import math
import random
from object import *
from map import Map
from dialog import Dialog
from inventory import Inventory
from profile import Profile
from battlescene import BattleScene

"""
- Setsup, stores and displays the environment (maps, objects, characters) and player.
- Handles player-movement and interactions.
"""

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.maps = []
        self.current_map = None
        self.setup_player()
        self.setup_map()
        self.running = True
        
    def setup_player(self):
        self.player = Player("Peter", "images/sprites/player.png", [9,8],1,30,50,[1,10],10,["Hello"],[0,0],900)
        self.dia = Dialog(self.screen)
        self.bag = Inventory(self.player,self.screen)
        self.prof = Profile(self.player, self.screen)

    def setup_map(self):
        self.current_map = Map(self.screen, "map1.csv", self.player)
        self.current_map.objects.append(self.player)
        self.maps.append(self.current_map)

    def update(self):
        self.handle_events()
        self.current_map.render_map()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                    self.player.direction = "UP"
                elif event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])
                    self.player.direction = "DOWN"
                elif event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])
                    self.player.direction = "LEFT"
                elif event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])
                    self.player.direction = "RIGHT"
                elif event.key == pygame.K_b:
                    self.player.open_inventory(self.screen)
                elif event.key == pygame.K_c:
                    self.prof.profile_update()
                elif event.key == pygame.K_SPACE:
                    self.interact(self.player)

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] >= len(self.current_map.map[0]):
            return
        if new_position[1] >= len(self.current_map.map):
            return

        number_str = str(self.current_map.map[new_position[1]][new_position[0]])
        if int(number_str[1]) > 4:
            return

        if new_position[0] < 0 or new_position[0] > (len(self.current_map.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.current_map.map) - 1):
            return

        if self.current_map.map[new_position[1]][new_position[0]] == "206":
            random_number = random.randint(1, 150)
            if random_number == 15:
                dia = Dialog(self.screen)
                dia.draw_text_dialog("You have been attacked!")
                enemy = Enemy("Demon", "images/portraits/Demon.png", [0,0],3,15,0,[1,5],0,"Hihihi",[0,0],0,None,10,3)
                battle = BattleScene(self.screen, self.player, enemy)
                battle.battle_update()
                
        if(self.current_map.map[new_position[1]][new_position[0]] == "202" or
         self.current_map.map[new_position[1]][new_position[0]] == "204" or
          self.current_map.map[new_position[1]][new_position[0]] == "109" or
           self.current_map.map[new_position[1]][new_position[0]] == "108" or
            self.current_map.map[new_position[1]][new_position[0]] == "107" or
             self.current_map.map[new_position[1]][new_position[0]] == "305" or
              self.current_map.map[new_position[1]][new_position[0]] == "203" or
               self.current_map.map[new_position[1]][new_position[0]] == "300"):
            for exit in self.current_map.exits:
                if(exit[1] == new_position[0] and exit[2] == new_position[1]):
                    for m in self.maps:
                        if m.file_name == exit[0]:
                            self.current_map = m
                            print(exit[3])
                            self.player.update_position(exit[3])
                            return
                    print(exit[3])
                    self.player.update_position(exit[3])
                    second_map = Map(self.screen, exit[0], self.player)
                    second_map.objects.append(self.player)
                    self.current_map = second_map
                    self.maps.append(second_map)
            return
        print(len(self.maps))
        print(new_position)
        unit.update_position(new_position)

    def interact(self, unit):
        if(unit.direction == "LEFT"):
            target_position = [unit.position[0] - 1, unit.position[1]]    
        if(unit.direction == "RIGHT"):
            target_position = [unit.position[0]+1, unit.position[1]]    
        if(unit.direction == "UP"):
            target_position = [unit.position[0], unit.position[1] - 1]    
        if(unit.direction == "DOWN"):
            target_position = [unit.position[0], unit.position[1] + 1]
        print(target_position)


        number_str = str(self.current_map.map[target_position[1]][target_position[0]])
        if int(number_str[0]) == 9:
            for obj in self.current_map.objects:
                if(target_position[1] == obj.start_position[1] and target_position[0] == obj.start_position[0]):
                    if isinstance(obj, Character) or isinstance(obj, Chest):
                        status = obj.interactable(self.player,self.screen)
                        if status == 1:
                            self.current_map.map[obj.start_position[1]][obj.start_position[0]] = str(int(obj.idnr)-750)
                            self.current_map.objects.remove(obj)
                        elif status == 2:
                            for p in obj.positions:
                                self.current_map.map[p[1]][p[0]] = str(int(obj.idnr)-750)
                            self.current_map.objects = [item for item in self.current_map.objects if item.name != obj.name]

                    elif isinstance(obj, Object):
                        obj.interactable(self.player, self.screen)
