""" 
- Configuration settings, constants, and other variables that are used across different parts of your program.
- Contains data of items and characters stored in JSON format
"""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLU = (255, 0, 255)
GRAY = (130, 130, 130)

SCALE = 37

SCREEN_HEIGHT = 540
SCREEN_WIDTH = 740

MAP_CONFIG = {
    "map1.csv" : {
        "start_position" : [0,0],
        "npcs" : [
            {
                "name" : "Peasant",
                "image" : "images/sprites/peasant.png",
                "start_position" : [3,10],
                "level" : 1,
                "health" : 10,
                "mana" : 0,
                "damage" : [1,3],
                "crit" : 10,
                "dialog" : ["Hello! Have you heard the news?", ["Tell me about them", "Attack", "Leave"], "Warlocks have taken over the cave and are summoning powerful monsters","Please no!","Bye!"],
                "kind" : [0,0],
                "idnr" : 951,
                "loot" : 2,
                "gold" : 10,
                "xp" : 2
            },
            {
                "name" : "Druid",
                "image" : "images/sprites/druid.png",
                "start_position" : [14,10],
                "level" : 2,
                "health" : 20,
                "mana" : 30,
                "damage" : [1,5],
                "crit" : 10,
                "dialog" : ["I found this other/chest here, but I can't open it! Try to open it yourself.", ["I will take a look", "Attack", "Leave"], "Maybe a key is needed?","Very well......","Have a good one!"],
                "kind" : [0,0],
                "idnr" : 951,
                "loot" : 2,
                "gold" : 10,
                "xp" : 2
            },
            {
                "name" : "Knight",
                "image" : "images/sprites/champion_left.png",
                "start_position" : [7,3],
                "level" : 5,
                "health" : 35,
                "mana" : 0,
                "damage" : [4,7],
                "crit" : 10,
                "dialog" : ["Well met! The King wants to see you.", ["Where can I find him?", "Attack", "Leave"], "Inside the castle walls, behind me.","What the...?","See you around!"],
                "kind" : [0,0],
                "idnr" : 950,
                "loot" : 1,
                "gold" : 10,
                "xp" : 5
            },
            {
                "name" : "Knight",
                "image" : "images/sprites/champion_right.png",
                "start_position" : [12,3],
                "level" : 5,
                "health" : 35,
                "mana" : 0,
                "damage" : [4,7],
                "crit" : 10,
                "dialog" : ["Well met! The King wants to see you.", ["Where can I find him?", "Attack", "Leave"], "Inside the castle walls, behind me.","You bastard!","Later!"],
                "kind" : [0,0],
                "idnr" : 950,
                "loot" : 1,
                "gold" : 10,
                "xp" : 5
            }
        ],
                "decorations" : [
                {
                    "name" : "Moooo",
                    "image" : "images/tiles/Map1/cow.png",
                    "position" : [3,17],
                    "idnr" : 951
                },
                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_top.png",
                    "position" : [15,8],
                    "idnr" : 951
                },                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_bottom.png",
                    "position" : [15,9],
                    "idnr" : 951
                },
                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_top.png",
                    "position" : [17,9],
                    "idnr" : 951
                },                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_bottom.png",
                    "position" : [17,10],
                    "idnr" : 951
                },
                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_top.png",
                    "position" : [13,9],
                    "idnr" : 951
                },                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_bottom.png",
                    "position" : [13,10],
                    "idnr" : 951
                },
                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_top.png",
                    "position" : [17,16],
                    "idnr" : 272
                },                {
                    "name" : "Tree",
                    "image" : "images/tiles/Map1/tree_bottom.png",
                    "position" : [17,17],
                    "idnr" : 951
                },                             
                {
                    "name" : "Well",
                    "image" : "images/tiles/Map1/well_top.png",
                    "position" : [4,9],
                    "idnr" : 951
                },                
                {
                    "name" : "Well",
                    "image" : "images/tiles/Map1/well_bottom.png",
                    "position" : [4,10],
                    "idnr" : 951
                },                
                {
                    "name" : "Barrel",
                    "image" : "images/other/barrel.png",
                    "position" : [5,10],
                    "idnr" : 951
                }],
        "exits" : [
        {
            "info" : ["map2.csv",8, 2,[7,14]]
        },
        {
            "info" : ["map2.csv",9, 2,[8,14]]
        },
        {
            "info" : ["map2.csv",10, 2,[9,14]]
        },
        {
            "info" : ["map2.csv",11, 2,[11,14]]
        },
        {
            "info" : ["cave.csv",9, 19,[9,3]]
        },
        {
            "info" : ["cave.csv",10, 19,[9,3]]
        },
        {
            "info" : ["room1.csv",4, 15,[9,11]]
        },
        {
            "info" : ["room2.csv",15, 16,[11,11]]
        }
    ],
        "boss" : [],
        "chests" : [
            {
                "name" : "Bronze Chest",
                "image" : "images/other/chest.png",
                "position" : [15,10],
                "idnr" : 951,
                "loot" : 2
            },   
        ]},
    "map2.csv" : {
            "start_position" : [10,13],
            "npcs" : [
                {
                    "name" : "Crusader",
                    "image" : "images/sprites/crusader.png",
                    "start_position" : [8,7],
                    "level" : 9,
                    "health" : 80,
                    "mana" : 0,
                    "damage" : [10,20],
                    "crit" : 10,
                    "dialog" : ["Do as the King says or perish!", ["Yes sir!", "Attack", "Leave"], "Go forth to victory!","Haha an amateur like you have no chance.","Go forth to victory!"],
                    "kind" : [0,0],
                    "idnr" : 959,
                    "loot" : 5,
                    "gold" : 10,
                    "xp" : 15
                },
                {
                    "name" : "King",
                    "image" : "images/sprites/king.png",
                    "start_position" : [9,7],
                    "level" : 10,
                    "health" : 100,
                    "mana" : 100,
                    "damage" : [40,60],
                    "crit" : 10,
                    "dialog" : ["Our people are in grave danger, you need to help us!", ["How may I serve you?","Attack", "Leave"], "Go to the cave, far south, where the monsters are and kill them all!","This is the biggest mistake in your life.","Go to the cave, far south, where the monsters are and kill them all!"],
                    "kind" : [0,0],
                    "idnr" : 959,
                    "loot" : 7,
                    "gold" : 10000,
                    "xp" : 100
                },
                {
                    "name" : "Knight",
                    "image" : "images/sprites/knight_left.png",
                    "start_position" : [7,11],
                    "level" : 6,
                    "health" : 40,
                    "mana" : 0,
                    "damage" : [5,10],
                    "crit" : 10,
                    "dialog" : ["Speak to the King.", ["What does he want from me?", "Attack", "Leave"], "No idea, but it is urgent!","What the...?","Bye"],
                    "kind" : [0,0],
                    "idnr" : 957,
                    "loot" : 1,
                    "gold" : 50,
                    "xp" : 5
                },
                {
                    "name" : "Knight",
                    "image" : "images/sprites/knight_right.png",
                    "start_position" : [11,11],
                    "level" : 6,
                    "health" : 40,
                    "mana" : 0,
                    "damage" : [5,10],
                    "crit" : 10,
                    "dialog" : ["The King is waiting for you.", ["What does he want from me?", "Attack", "Leave"], "He has some special task for you I assume...","What the...?","Bye"],
                    "kind" : [0,0],
                    "idnr" : 958,
                    "loot" : 1,
                    "gold" : 50,
                    "xp" : 5
                }
            ],
                "decorations" : [],
            "exits" : [
            {
                "info" : ["map1.csv",7, 15,[8,3]]
            },
            {
                "info" : ["map1.csv",8, 15,[9,3]]
            },
            {
                "info" : ["map1.csv",9, 15,[10,3]]
            },
            {
                "info" : ["map1.csv",10, 15,[10,3]]
            },
            {
                "info" : ["map1.csv",11, 15,[11,3]]
            }],
                "boss" : [],
                "chests" : []
        },
    "cave.csv" : {
            "start_position" : [10,13],
            "npcs" : [
                {
                    "name" : "Warlock",
                    "image" : "images/sprites/warlock2.png",
                    "start_position" : [9,17],
                    "level" : 10,
                    "health" : 20,
                    "mana" : 100,
                    "damage" : [50,100],
                    "crit" : 10,
                    "dialog" : "You dare disturb the master? Prepare yourself for death!",
                    "kind" : [3,0],
                    "idnr" : 956,
                    "loot" : 2,
                    "gold" : 100,
                    "xp" : 20
                },
                {
                    "name" : "Shadow",
                    "image" : "images/sprites/corruptedtree.png",
                    "start_position" : [1,18],
                    "level" : 7,
                    "health" : 20,
                    "mana" : 100,
                    "damage" : [5,10],
                    "crit" : 10,
                    "dialog" : "No one may enter!",
                    "kind" : [3,0],
                    "idnr" : 956,
                    "loot" : 2,
                    "gold" : 50,
                    "xp" : 5
                },
                {
                    "name" : "Shadow",
                    "image" : "images/sprites/corruptedtree.png",
                    "start_position" : [2,19],
                    "level" : 7,
                    "health" : 20,
                    "mana" : 100,
                    "damage" : [5,10],
                    "crit" : 10,
                    "dialog" : "No one may enter!",
                    "kind" : [3,0],
                    "idnr" : 956,
                    "loot" : 2,
                    "gold" : 50,
                    "xp" : 5
                }

            ],
                "decorations" : [               
                {
                    "name" : "Marik",
                    "image" : "images/tiles/Cave/warlock1_top_right.png",
                    "position" : [8,13],
                    "idnr" : 956

                },                {
                    "name" : "Marik",
                    "image" : "images/tiles/Cave/warlock1_top_left.png",
                    "position" : [9,13],
                    "idnr" : 956
                },
                {
                    "name" : "Chimera",
                    "image" : "images/tiles/Cave/chimera_top_left.png",
                    "position" : [5,24],
                    "idnr" : 956
                },
                {
                    "name" : "Chimera",
                    "image" : "images/tiles/Cave/chimera_top_right.png",
                    "position" : [6,24],
                    "idnr" : 956
                }],
            "exits" : [
            {
                "info" : ["map1.csv",8, 2,[9,18]]
            },
                        {
                "info" : ["map1.csv",9, 2,[9,18]]
            },
                        {
                "info" : ["map1.csv",10, 2,[10,18]]
            }],
            "boss" : [
                    {
                        "name" : "Chimera",
                        "images" : ["images/tiles/Cave/chimera_bottom_left.png","images/tiles/Cave/chimera_bottom_right.png"],
                        "start_position" : [[5,25],[6,25]],
                        "level" : 20,
                        "health" : 100,
                        "mana" : 100,
                        "damage" : [10,20],
                        "crit" : 10,
                        "dialog" : "RAWWWWWWWWWWR",
                        "kind" : [1,1],
                        "idnr" : 956,
                        "positions" : [[5,25],[6,25],[5,24],[6,24]],
                        "loot" : 12,
                        "gold" : 200,
                        "xp" : 50
                    },
                    {
                        "name" : "Marik",
                        "images" : ["images/tiles/Cave/warlock1_bottom_left.png","images/tiles/Cave/warlock1_bottom_right.png"],
                        "start_position" : [[9,14],[8,14]],
                        "level" : 20,
                        "health" : 50,
                        "mana" : 100,
                        "damage" : [50,100],
                        "crit" : 10,
                        "dialog" : "Hahahaha",
                        "kind" : [1,1],
                        "idnr" : 956,
                        "positions" : [[9,14],[8,14],[8,13],[8,13]],
                        "loot" : 11,
                        "gold" : 200,
                        "xp" : 50
                    }
                ],
            "chests" : [                
                {
                    "name" : "Golden Chest",
                    "image" : "images/other/chest.png",
                    "position" : [10,14],
                    "idnr" : 956,
                    "loot" : 7
                },
                {
                    "name" : "Diamond Chest",
                    "image" : "images/other/chest.png",
                    "position" : [12,27],
                    "idnr" : 956,
                    "loot" : 6
                },

            ]
        },
    "room1.csv" : {
                "start_position" : [6,6],
                "npcs" : [
                    {
                        "name" : "David",
                        "image" : "images/sprites/merchant1.png",
                        "start_position" : [10,5],
                        "level" : 5,
                        "health" : 30,
                        "mana" : 100,
                        "damage" : [4,6],
                        "crit" : 10,
                        "dialog" : ["Welcome to my shop, do you need anything?", ["Browse Shop", "Sell Items","Attack", "Leave"], "Anything else?"],
                        "kind" : [1,0],
                        "idnr" : 955,
                        "loot" : 2,
                        "gold" : 500,
                        "xp" : 5
                    },
                    {
                        "name" : "Rogue",
                        "image" : "images/sprites/rogue.png",
                        "start_position" : [14,7],
                        "level" : 3,
                        "health" : 10,
                        "mana" : 100,
                        "damage" : [1,5],
                        "crit" : 10,
                        "dialog" : "You will never get my treasure!",
                        "kind" : [3,0],
                        "idnr" : 955,
                        "loot" : 10,
                        "gold" : 50,
                        "xp" : 5
                    }
                ],
                "decorations" : [
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_left.png",
                    "position" : [4,4],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_right.png",
                    "position" : [5,4],
                    "idnr" : 955
                },
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_left.png",
                    "position" : [4,5],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_right.png",
                    "position" : [5,5],
                    "idnr" : 955
                },
                                {
                    "name" : "chair",
                    "image" : "images/tiles/Room01/chair_left.png",
                    "position" : [4,10],
                    "idnr" : 205
                },                {
                    "name" : "chair",
                    "image" : "images/tiles/Room01/chair_right.png",
                    "position" : [7,10],
                    "idnr" : 205
                },
                {
                    "name" : "table",
                    "image" : "images/tiles/Room01/table_2_left.png",
                    "position" : [5,10],
                    "idnr" : 955
                },                {
                    "name" : "table",
                    "image" : "images/tiles/Room01/table_2_right.png",
                    "position" : [6,10],
                    "idnr" : 955
                },
                {
                    "name" : "armor",
                    "image" : "images/tiles/Room01/armor_bottom.png",
                    "position" : [13,5],
                    "idnr" : 955
                },                {
                    "name" : "armor",
                    "image" : "images/tiles/Room01/armor_top.png",
                    "position" : [13,4],
                    "idnr" : 955
                },                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_top_left.png",
                    "position" : [12,9],
                    "idnr" : 205
                }
                ,                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_top_center.png",
                    "position" : [13,9],
                    "idnr" : 205
                },                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_top_right.png",
                    "position" : [14,9],
                    "idnr" : 205
                },                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_bottom_left.png",
                    "position" : [12,10],
                    "idnr" : 205
                },                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_bottom_center.png",
                    "position" : [13,10],
                    "idnr" : 205
                },                
                {
                    "name" : "carpet",
                    "image" : "images/tiles/Room01/carpet_bottom_right.png",
                    "position" : [14,10],
                    "idnr" : 205
                }],
                "exits" : [
                {
                    "info" : ["map1.csv",9,12,[4,16]]
                },
                {
                    "info" : ["map1.csv",10,12,[4,16]]
                }],
                "boss" : [],
                "chests" : []
            },
    "room2.csv" : {
                "start_position" : [6,6],
                "npcs" : [
                    {
                        "name" : "Peasant",
                        "image" : "images/Sprites/merchant3.png",
                        "start_position" : [5,5],
                        "level" : 3,
                        "health" : 10,
                        "mana" : 100,
                        "damage" : [1,3],
                        "crit" : 10,
                        "dialog" : ["Zzzzzz...", ["Hello?", "Attack", "Leave"], "ZzzzzZZZZZzzzzzz","Huh?","ZZZZZZZZzzzzzzzzzz"],
                        "kind" : [0,0],
                        "idnr" : 955,
                        "loot" : 0,
                        "gold" : 100,
                        "xp" : 2
                    },{
                        "name" : "Mage",
                        "image" : "images/Sprites/merchant4.png",
                        "start_position" : [13,6],
                        "level" : 6,
                        "health" : 40,
                        "mana" : 100,
                        "damage" : [5,10],
                        "crit" : 10,
                        "dialog" : ["Hello, would you like to buy some potions?", ["Browse Shop", "Sell Items","Attack", "Leave"], "Anything else?"],
                        "kind" : [1,1],
                        "idnr" : 955,
                        "loot" : 3,
                        "gold" : 50,
                        "xp" : 10
                    }
                ],
                "decorations" : [
                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_top_left.png",
                    "position" : [4,8],
                    "idnr" : 205
                },                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_top_center.png",
                    "position" : [5,8],
                    "idnr" : 205
                },                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_top_right.png",
                    "position" : [6,8],
                    "idnr" : 205
                },                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_bottom_left.png",
                    "position" : [4,9],
                    "idnr" : 205
                },                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_bottom_center.png",
                    "position" : [5,9],
                    "idnr" : 205
                },                {
                    "name" : "Carpet",
                    "image" : "images/tiles/Room02/carpet2_bottom_right.png",
                    "position" : [6,9],
                    "idnr" : 205
                },
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_left.png",
                    "position" : [13,4],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_right.png",
                    "position" : [14,4],
                    "idnr" : 955
                },
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_left.png",
                    "position" : [13,5],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_right.png",
                    "position" : [14,5],
                    "idnr" : 955
                },
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_left.png",
                    "position" : [15,4],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_top_right.png",
                    "position" : [16,4],
                    "idnr" : 955
                },
                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_left.png",
                    "position" : [15,5],
                    "idnr" : 955
                },                {
                    "name" : "bookshelf",
                    "image" : "images/tiles/Room01/bookshelf_bottom_right.png",
                    "position" : [16,5],
                    "idnr" : 955
                }],
                "exits" : [
                {
                    "info" : ["map1.csv",11, 12,[15,17]]
                },
                {
                    "info" : ["map1.csv",12, 12,[15,17]]
                }],
                "boss" : [],
                "chests" : []
            }
}

MERCHANT_CONFIG = {
    "1" : {
        "items" : [
            {
                "category" : "WEAPON",
                "image" : "images/Items/basic_sword.png",
                "name" : "Mace",
                "description" : "Low quality mace for a good price",
                "level" : 1,
                "health" : 0,
                "mana" : 0,
                "damage" : [1,20],
                "crit" : 10,
                "value" : 10
            },
            {
                "category" : "WEAPON",
                "image" : "images/Items/basic_sword.png",
                "name" : "Dagger",
                "description" : "Most likely stolen",
                "level" : 1,
                "health" : 0,
                "mana" : 0,
                "damage" : [5,7],
                "crit" : 10,
                "value" : 10
            },
            {
                "category" : "WEAPON",
                "image" : "images/Items/basic_sword.png",
                "name" : "Dagger",
                "description" : "Most likely stolen",
                "level" : 1,
                "health" : 0,
                "mana" : 0,
                "damage" : [5,7],
                "crit" : 10,
                "value" : 10            
            },
            {
                "category" : "ITEM",
                "image" : "images/Items/basic_sword.png",
                "name" : "Necklace",
                "description" : "Shiny thing",
                "value" : 100,
            },
            {
                "category" : "ITEM",
                "image" : "images/Items/basic_sword.png",
                "name" : "Gem",
                "description" : "Blue and big",
                "value" : 100,
        }]
    },
    "2": {
        "items" : [
            {
                "category" : "POTION",
                "image" : "images/Items/basic_sword.png",
                "name" : "Health Potion",
                "description" : "Red and smells nice",
                "health" : 50,
                "mana" : 0,
                "damage" : [0,0],
                "crit" : 0,
                "value" : 25
            },
            {
                "category" : "POTION",
                "image" : "images/Items/basic_sword.png",
                "name" : "Mana Potion",
                "description" : "Red and smells nice",
                "health" : 0,
                "mana" : 25,
                "damage" : [0,0],
                "crit" : 0,
                "value" : 25
            }
        ]
    }
}

ITEMS_CONFIG = {
    "items" : [
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Basic Mace",
            "description" : "Damage: 1 - 10 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [1,10],
            "crit" : 10,
            "value" : 10
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Basic Sword",
            "description" : "Damage: 4 - 6 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [4,6],
            "crit" : 10,
            "value" : 10
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Dagger",
            "description" : "Damage: 1 - 15 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [1,15],
            "crit" : 10,
            "value" : 25
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Shadow Blade",
            "description" : "Damage: 8 - 12 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [1,15],
            "crit" : 10,
            "value" : 100
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Golden Mace",
            "description" : "Damage: 1 - 20 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [1,20],
            "crit" : 10,
            "value" : 100
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Starforged Sword",
            "description" : "Damage: 20 - 25 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [20,25],
            "crit" : 10,
            "value" : 250
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Deathcleaver",
            "description" : "Damage: 1 - 50 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [1,50],
            "crit" : 10,
            "value" : 250
        },
        {
            "category" : "WEAPON",
            "image" : "images/Items/basic_sword.png",
            "name" : "Thor's Hammer",
            "description" : "Damage: 50 - 100 damage.",
            "level" : 1,
            "health" : 0,
            "mana" : 0,
            "damage" : [50,100],
            "crit" : 10,
            "value" : 1000
        },
        {
            "category" : "POTION",
            "image" : "images/Items/basic_sword.png",
            "name" : "Health Potion",
            "description" : "Restores 40 health.",
            "health" : 40,
            "mana" : 0,
            "damage" : [0,0],
            "crit" : 0,
            "value" : 25
        },
        {
            "category" : "POTION",
            "image" : "images/Items/basic_sword.png",
            "name" : "Mana Potion",
            "description" : "Restores 25 mana.",
            "health" : 0,
            "mana" : 25,
            "damage" : [0,0],
            "crit" : 0,
            "value" : 25
        },
        {
            "category" : "KEY",
            "image" : "images/Items/basic_sword.png",
            "name" : "Bronze Key",
            "description" : "Opens the Bronze Chest.",
            "value" : 20,
            "unlock_chest" : [15,10]
        },
        {
            "category" : "KEY",
            "image" : "images/Items/basic_sword.png",
            "name" : "Golden Key",
            "description" : "Opens the Golden Chest.",
            "value" : 50,
            "unlock_chest" : [10,14]
        },
        {
            "category" : "KEY",
            "image" : "images/Items/basic_sword.png",
            "name" : "Diamond Key",
            "description" : "Opens the Diamond Chest.",
            "value" : 200,
            "unlock_chest" : [12,27]
        }
    ]}



