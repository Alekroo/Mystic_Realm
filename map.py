import pygame
import config
import math
from object import *

"""
- Reads in a map from a csv file.
- Retrives data about objects, characters that are supposed to be
displayed on the map found in the config file 
- Creates the map and objects assosiated with it.
- Determines the camere (what the user sees) when user moves.
"""

class Map():
    def __init__(self, screen, file_name, player):
        self.screen = screen
        self.file_name = file_name
        self.map_name = file_name
        self.objects = []
        self.map = []
        self.exits = []
        self.camera = [0,0]
        self.player = player
        self.objects.append(player)
        self.screen.fill(config.BLACK)
        self.load_map()
        self.load_objects()

    def render_map(self):
        self.determine_camera()
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                self.screen.blit(image, rect)
                x_pos = x_pos + 1
            y_pos = y_pos + 1

        for object in self.objects:
            object.render(self.screen, self.camera)

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

    def load_map(self):
        with open("maps/" + self.file_name) as map_file:
            for line in map_file:
                tiles = line.split(',')
                tiles[-1] = tiles[-1].strip()
                self.map.append(tiles)

        map_config = config.MAP_CONFIG[self.map_name]["exits"]
        for x in map_config:
            self.exits.append(x["info"])

    def load_objects(self):

        map_config_decorations = config.MAP_CONFIG[self.map_name]["decorations"]
        for y in map_config_decorations:
            self.objects.append(Object(y["name"],y["image"],y["position"],y["idnr"]))
            self.map[y["position"][1]][y["position"][0]] = str(y["idnr"])
            #self.map[x["start_position"][0]][x["start_position"][1]] = "C"

        map_config_player = config.MAP_CONFIG[self.map_name]["npcs"]

        map_config = config.MAP_CONFIG[self.map_name]["npcs"]
        for x in map_config:
            loot_drop = self.loot_item(x)
            if x["kind"][0] == 0:            
                self.objects.append(Character(x["name"],x["image"],x["start_position"],x["level"],
                    x["health"],x["mana"],x["damage"],x["crit"],x["dialog"],x["kind"],x["idnr"],loot_drop,x["gold"],x["xp"]))
                self.map[x["start_position"][1]][x["start_position"][0]] = str(x["idnr"])

            elif x["kind"][0] == 1:
                item_list = config.ITEMS_CONFIG["items"]
                if x["kind"][1] == 0:
                    new_merchant = Merchant(x["name"],x["image"],x["start_position"],x["level"],
                        x["health"],x["mana"],x["damage"],x["crit"],x["dialog"],x["kind"],x["idnr"],loot_drop,x["gold"],x["xp"])
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[3])),
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[4])),
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[5])),
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[6]))
                elif x["kind"][1] == 1:
                    new_merchant = Merchant(x["name"],x["image"],x["start_position"],x["level"],
                        x["health"],x["mana"],x["damage"],x["crit"],x["dialog"],x["kind"],x["idnr"],loot_drop,x["gold"],x["xp"])
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[8])),
                    new_merchant.add_item_to_sell(self.loot_item2(item_list[9]))
                self.objects.append(new_merchant)
                self.map[x["start_position"][1]][x["start_position"][0]] = str(x["idnr"])

            elif x["kind"][0] == 3:
                loot_drop = self.loot_item(x)
                new_enemy = Enemy(x["name"],x["image"],x["start_position"],x["level"],
                    x["health"],x["mana"],x["damage"],x["crit"],x["dialog"],x["kind"],x["idnr"],loot_drop,x["gold"],x["xp"])
                self.objects.append(new_enemy)
                self.map[x["start_position"][1]][x["start_position"][0]] = str(x["idnr"])

        map_config_boss = config.MAP_CONFIG[self.map_name]["boss"]
        for b in map_config_boss:
            loot_drop = self.loot_item(b)
            new_boss1 = Boss(b["name"],b["images"][0],b["start_position"][0],b["level"],
                b["health"],b["mana"],b["damage"],b["crit"],b["dialog"],b["kind"],b["idnr"],b["positions"],loot_drop ,b["gold"],b["xp"])
            new_boss2 = Boss(b["name"],b["images"][1],b["start_position"][1],b["level"],
                b["health"],b["mana"],b["damage"],b["crit"],b["dialog"],b["kind"],b["idnr"],b["positions"],loot_drop ,b["gold"],b["xp"])
            self.objects.append(new_boss1)
            self.objects.append(new_boss2)
            self.map[b["start_position"][0][1]][b["start_position"][0][0]] = str(b["idnr"])
            self.map[b["start_position"][1][1]][b["start_position"][1][0]] = str(b["idnr"])

        map_config_chests = config.MAP_CONFIG[self.map_name]["chests"]
        for z in map_config_chests:
            loot = config.ITEMS_CONFIG["items"][z["loot"]]
            loot_drop = Sword(loot["name"],loot["image"],loot["description"],loot["level"],loot["health"],loot["mana"],
                loot["damage"],loot["crit"],loot["value"])

            self.objects.append(Chest(z["name"],z["image"],z["position"],z["idnr"],loot_drop))
            self.map[z["position"][1]][z["position"][0]] = str(z["idnr"])

    def loot_item(self, b):
        loot = config.ITEMS_CONFIG["items"][b["loot"]]
        if loot["category"] == "POTION":
            loot_drop = (Potion(loot["name"],loot["image"],loot["description"],loot["health"],loot["mana"],
                loot["damage"],loot["crit"],loot["value"]))
        elif loot["category"] == "WEAPON":
            loot_drop = Sword(loot["name"],loot["image"],loot["description"],loot["level"],loot["health"],loot["mana"],
                loot["damage"],loot["crit"],loot["value"])
        elif loot["category"] == "KEY":
            loot_drop = (Key(loot["name"],loot["image"],loot["description"],loot["value"],loot["unlock_chest"]))
        return loot_drop

    def loot_item2(self, loot):
        if loot["category"] == "POTION":
            loot_drop = (Potion(loot["name"],loot["image"],loot["description"],loot["health"],loot["mana"],
                loot["damage"],loot["crit"],loot["value"]))
        elif loot["category"] == "WEAPON":
            loot_drop = Sword(loot["name"],loot["image"],loot["description"],loot["level"],loot["health"],loot["mana"],
                loot["damage"],loot["crit"],loot["value"])
        elif loot["category"] == "KEY":
            loot_drop = (Key(loot["name"],loot["image"],loot["description"],loot["value"],loot["unlock_chest"]))
        return loot_drop

map_tile_image = {
    "100" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/stone_ground.png"), (config.SCALE, config.SCALE)),
    "101" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/left_stairs.png"), (config.SCALE, config.SCALE)),
    "102" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/center_stairs.png"), (config.SCALE, config.SCALE)),
    "103" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/right_stairs.png"), (config.SCALE, config.SCALE)),
    "104" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/lb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "105" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/rb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "106" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/cb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "107" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/cb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "108" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/lb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "109" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/rb_red_carpet.png"), (config.SCALE, config.SCALE)),

    "150" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/center_column.png"), (config.SCALE, config.SCALE)),
    "151" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/bottom_column.png"), (config.SCALE, config.SCALE)),
    "152" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/top_red.png"), (config.SCALE, config.SCALE)),
    "153" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/bottom_red.png"), (config.SCALE, config.SCALE)),

    "200" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/stone_ground.png"), (config.SCALE, config.SCALE)),
    "201" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/grass3.png"), (config.SCALE, config.SCALE)),
    "202" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/black.png"), (config.SCALE, config.SCALE)),
    "203" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/black_entrence.png"), (config.SCALE, config.SCALE)),
    "204" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/stone_ground.png"), (config.SCALE, config.SCALE)),
    "205" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/floor_wood.png"), (config.SCALE, config.SCALE)),
    "206" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ground.png"), (config.SCALE, config.SCALE)),
    "207" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/lb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "208" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/rb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "209" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/center_stairs.png"), (config.SCALE, config.SCALE)),

    "250" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/water.png"), (config.SCALE, config.SCALE)),
    "251" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/upper_cw_c.png"), (config.SCALE, config.SCALE)),
    "252" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/upper_ct_c.png"), (config.SCALE, config.SCALE)),
    "253" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/upper_tw_l.png"), (config.SCALE, config.SCALE)),
    "254" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/upper_tw_r.png"), (config.SCALE, config.SCALE)),
    "255" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/center_tw_l.png"), (config.SCALE, config.SCALE)),
    "256" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/center_tw_r.png"), (config.SCALE, config.SCALE)),
    "257" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_tw_l.png"), (config.SCALE, config.SCALE)),
    "258" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_tw_r.png"), (config.SCALE, config.SCALE)),
    "259" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/center_cw_l.png"), (config.SCALE, config.SCALE)),
    "260" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/center_cw_c.png"), (config.SCALE, config.SCALE)),
    "261" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/center_cw_r.png"), (config.SCALE, config.SCALE)),
    "262" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_cw_l.png"), (config.SCALE, config.SCALE)),
    "263" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_cw_c.png"), (config.SCALE, config.SCALE)),
    "264" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_cw_r.png"), (config.SCALE, config.SCALE)),
    "265" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wh_left.png"), (config.SCALE, config.SCALE)),
    "266" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wh_center.png"), (config.SCALE, config.SCALE)),
    "267" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wh_right.png"), (config.SCALE, config.SCALE)),
    "268" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_wh_left.png"), (config.SCALE, config.SCALE)),
    "269" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_wh_right.png"), (config.SCALE, config.SCALE)),
    "270" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/roof_wh.png"), (config.SCALE, config.SCALE)),
    "271" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/roof_red.png"), (config.SCALE, config.SCALE)),
    "272" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_wd_right.png"), (config.SCALE, config.SCALE)),
    "273" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_wd_center.png"), (config.SCALE, config.SCALE)),
    "274" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/bottom_wd_left.png"), (config.SCALE, config.SCALE)),
    "275" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wd_right.png"), (config.SCALE, config.SCALE)),
    "276" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wd_center.png"), (config.SCALE, config.SCALE)),
    "277" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/top_wd_left.png"), (config.SCALE, config.SCALE)),
    "278" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/tree_top.png"), (config.SCALE, config.SCALE)),
    "279" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/tree_bottom.png"), (config.SCALE, config.SCALE)),
    
    "1" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/chair.png"), (config.SCALE, config.SCALE)),



    "300" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_black.png"), (config.SCALE, config.SCALE)),
    "301" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_water.png"), (config.SCALE, config.SCALE)),

    "304" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_l_entrance.png"), (config.SCALE, config.SCALE)),
    "305" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_c_entrance.png"), (config.SCALE, config.SCALE)),
    "306" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_r_entrance.png"), (config.SCALE, config.SCALE)),
    "307" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_bl_entrance.png"), (config.SCALE, config.SCALE)),
    "308" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_bc_entrance.png"), (config.SCALE, config.SCALE)),
    "309" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_br_entrance.png"), (config.SCALE, config.SCALE)),


    "350" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ufl_entrance.png"), (config.SCALE, config.SCALE)),
    "351" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ul_entrance.png"), (config.SCALE, config.SCALE)),
    "352" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_uc_entrance.png"), (config.SCALE, config.SCALE)),
    "353" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ur_entrance.png"), (config.SCALE, config.SCALE)),
    "354" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ufr_entrance.png"), (config.SCALE, config.SCALE)),
    "355" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_lv_wall.png"), (config.SCALE, config.SCALE)),
    "356" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_cl_entrance.png"), (config.SCALE, config.SCALE)),
    "357" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_cc_entrance.png"), (config.SCALE, config.SCALE)),
    "358" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_cr_entrance.png"), (config.SCALE, config.SCALE)),
    "359" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_rv_wall.png"), (config.SCALE, config.SCALE)),

    "366" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_h1_wall.png"), (config.SCALE, config.SCALE)),
    "367" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_h2_wall.png"), (config.SCALE, config.SCALE)),
    "368" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vur_wall.png"), (config.SCALE, config.SCALE)),
    "369" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vul_wall.png"), (config.SCALE, config.SCALE)),
    "370" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hu1_wall.png"), (config.SCALE, config.SCALE)),
    "371" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vul_wall.png"), (config.SCALE, config.SCALE)),
    "372" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vcl_water.png"), (config.SCALE, config.SCALE)),
    "373" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vul_water.png"), (config.SCALE, config.SCALE)),
    "374" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hc_water.png"), (config.SCALE, config.SCALE)),
    "375" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hr_water.png"), (config.SCALE, config.SCALE)),
    "376" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vcr_water.png"), (config.SCALE, config.SCALE)),
    "377" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vcr_water.png"), (config.SCALE, config.SCALE)),
    "378" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vul_water.png"), (config.SCALE, config.SCALE)),
    "379" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_uc_water.png"), (config.SCALE, config.SCALE)),
    "380" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vur_water.png"), (config.SCALE, config.SCALE)),
    "381" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hr1_water.png"), (config.SCALE, config.SCALE)),
    "382" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hfl_water.png"), (config.SCALE, config.SCALE)),
    "383" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vl_water.png"), (config.SCALE, config.SCALE)),
    "384" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vlc_water.png"), (config.SCALE, config.SCALE)),
    "385" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vr_water.png"), (config.SCALE, config.SCALE)),
    "386" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hbr_water.png"), (config.SCALE, config.SCALE)),
    "387" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_vru_water.png"), (config.SCALE, config.SCALE)),
    "388" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_hul_water.png"), (config.SCALE, config.SCALE)),
    "400" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/floor_wood.png"), (config.SCALE, config.SCALE)),
    "401" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/rc_left.png"), (config.SCALE, config.SCALE)),
    "402" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/rc_center.png"), (config.SCALE, config.SCALE)),
    "403" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/rc_right.png"), (config.SCALE, config.SCALE)),
    "454" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/table_1_left.png"), (config.SCALE, config.SCALE)),
    "455" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/table_1_center.png"), (config.SCALE, config.SCALE)),
    "456" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/table_1_right.png"), (config.SCALE, config.SCALE)),
    "501" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_top_left.png"), (config.SCALE, config.SCALE)),
    "502" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_top_center.png"), (config.SCALE, config.SCALE)),
    "503" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_top_right.png"), (config.SCALE, config.SCALE)),
    "504" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_bottom_left.png"), (config.SCALE, config.SCALE)),
    "505" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_bottom_center.png"), (config.SCALE, config.SCALE)),
    "506" : pygame.transform.scale(pygame.image.load("images/tiles/Room02/carpet2_bottom_right.png"), (config.SCALE, config.SCALE)),

    "950" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/stone_ground.png"), (config.SCALE, config.SCALE)),
    "951" : pygame.transform.scale(pygame.image.load("images/tiles/Map1/grass3.png"), (config.SCALE, config.SCALE)),
    "955" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/floor_wood.png"), (config.SCALE, config.SCALE)),
    "956" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ground.png"), (config.SCALE, config.SCALE)),
    "957" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/lb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "958" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/rb_red_carpet.png"), (config.SCALE, config.SCALE)),
    "959" : pygame.transform.scale(pygame.image.load("images/tiles/Map2/center_stairs.png"), (config.SCALE, config.SCALE)),
    "980" : pygame.transform.scale(pygame.image.load("images/tiles/Cave/cave_ground.png"), (config.SCALE, config.SCALE)),
    "901" : pygame.transform.scale(pygame.image.load("images/tiles/Room01/floor_wood.png"), (config.SCALE, config.SCALE)),
}