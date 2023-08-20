import random
import pygame
import config
import math
import sys


"""
Creates, displays, and handles the Menu of the game.
"""

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.menu_image = pygame.image.load("images/other/Menu.png")
        self.image = pygame.transform.scale(self.menu_image, (800, config.SCREEN_WIDTH))
        self.title_font = pygame.font.Font(None, 150)
        self.font = pygame.font.Font(None, 50) 
        self.font2 = pygame.font.Font(None, 30) 
        self.window_size = (config.SCREEN_WIDTH,config.SCREEN_HEIGHT)
        self.title_text = self.title_font.render("Mystic Realm", True, (255, 255, 255))  # White color
        self.desc_font = pygame.font.Font(None, 28)
        self.selected_option = 0
        self.first_visible_option = 0
        self.visible_options = 3  
        self.dialog_area_height = 100  
        self.dialog_options = ["Play","Controls","Exit"]
        self.title_x = (config.SCREEN_WIDTH - self.title_text.get_width()) // 2
        self.title_y = 60  
        self.running = True

    def update(self):
        self.handle_events()
        self.display_menu()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_w:
                    self.select_previous_option()
                elif event.key == pygame.K_s:
                    self.select_next_option()
                elif event.key == pygame.K_SPACE:
                    self.handle_selected_option()

    def select_previous_option(self):
        self.selected_option = max(0, self.selected_option - 1)
        if self.selected_option < self.first_visible_option:
            self.first_visible_option = self.selected_option

    def select_next_option(self):
        self.selected_option = min(len(self.dialog_options) - 1, self.selected_option + 1)
        if self.selected_option >= self.first_visible_option + self.visible_options:
            self.first_visible_option = self.selected_option - self.visible_options + 1

    def handle_selected_option(self):
        if self.selected_option == 0:
            self.running = False
        elif self.selected_option == 1:
            self.controls()
        elif self.selected_option == 2:
            pygame.quit()
            sys.exit()

    def display_menu(self):
        self.screen.fill(config.BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.image, rect)
        self.screen.blit(self.title_text, (self.title_x, self.title_y))

        dialog_height = config.SCREEN_HEIGHT/2
        dialog_width = 200
        dialog_x = config.SCREEN_WIDTH/2-100
        dialog_y = config.SCREEN_HEIGHT/3

        #pygame.draw.rect(self.screen, (101, 47, 0), (dialog_x, dialog_y, dialog_width, dialog_height))

        # Calculate the height of each option box to evenly distribute them in the dialog area
        option_height = self.dialog_area_height // self.visible_options + 40

        # Calculate the top position of the dialog area
        dialog_area_top = self.window_size[1] - self.dialog_area_height 

        # Calculate the visible options
        last_visible_option = min(self.first_visible_option + self.visible_options, len(self.dialog_options))

        # Display the dialog options
        for i in range(self.first_visible_option, last_visible_option):
            option = self.dialog_options[i]
            text = self.font.render(option, True, config.WHITE)
            text_rect = text.get_rect(center=(self.window_size[0] // 2, dialog_area_top + (i - self.first_visible_option - 3) * option_height))
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (181, 101, 29), (text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10))
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def display_controls(self):
        profile_width = 500
        profile_height = 500
        profile_x = (self.screen.get_width() - profile_width) // 2
        profile_y = (self.screen.get_height() - profile_height) // 2

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(profile_x, profile_y, profile_width, profile_height))

        title_text = self.font.render("Controls", True, (0, 0, 0))
        title_x = profile_x + (profile_width - title_text.get_width()) // 2
        title_y = profile_y + 10

        up_text = self.font2.render("Move up - W", True, (0, 0, 0))
        down_text = self.font2.render("Move down - S", True, (0, 0, 0))
        left_text = self.font2.render("Move left - A", True, (0, 0, 0))
        right_text = self.font2.render("Move right - D", True, (0, 0, 0))
        select_text = self.font2.render("Select / Use - SPACE", True, (0, 0, 0))
        profile_text = self.font2.render("Profile - C", True, (0, 0, 0))
        inventory_text = self.font2.render("Inventory - B", True, (0, 0, 0))
        exit_text = self.font2.render("Exit - ESC", True, (0, 0, 0))

        self.screen.blit(title_text, (title_x, title_y+25))
        self.screen.blit(up_text, (profile_x + 30, title_y+90))
        self.screen.blit(down_text, (profile_x + 30, title_y+140))
        self.screen.blit(left_text, (profile_x + 30, title_y+190))
        self.screen.blit(right_text, (profile_x + 30, title_y+240))
        self.screen.blit(select_text, (profile_x + 30, title_y+290))
        self.screen.blit(profile_text, (profile_x + 30, title_y+340))
        self.screen.blit(inventory_text, (profile_x + 30, title_y+390))
        self.screen.blit(exit_text, (profile_x + 30, title_y+440))
        pygame.display.flip()

    def controls(self):
        self.display_controls()
        self.displaying_profile = True
        while self.displaying_profile:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.displaying_profile = False