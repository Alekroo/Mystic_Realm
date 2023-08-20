import config
import pygame

"""
Contains a variety of different text boxes (dialogues) to display.
"""

class Dialog():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.desc_font = pygame.font.Font(None, 28)
        self.selected_option = 0
        self.first_visible_option = 0
        self.visible_options = 3  # Number of options visible at a time
        self.dialog_area_height = 100  # Height of the dialog area from the bottom
        self.window_size = (config.SCREEN_WIDTH,config.SCREEN_HEIGHT)

    def dialog_loop(self,dialog_options):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.selected_option = max(0, self.selected_option - 1)
                        if self.selected_option < self.first_visible_option:
                            self.first_visible_option = self.selected_option
                    elif event.key == pygame.K_s:
                        self.selected_option = min(len(dialog_options) - 1, self.selected_option + 1)
                        if self.selected_option >= self.first_visible_option + self.visible_options:
                            self.first_visible_option = self.selected_option - self.visible_options + 1
                    elif event.key == pygame.K_SPACE:
                        print("Selected option:", dialog_options[self.selected_option])
                        return self.selected_option
            self.draw_dialog(dialog_options)

    def draw_dialog(self,dialog_options):
        dialog_height = 100
        dialog_width = config.SCREEN_WIDTH
        dialog_x = 0
        dialog_y = config.SCREEN_HEIGHT-100

        pygame.draw.rect(self.screen, config.WHITE, (dialog_x, dialog_y, dialog_width, dialog_height))

        # Calculate the height of each option box to evenly distribute them in the dialog area
        option_height = self.dialog_area_height // self.visible_options

        # Calculate the top position of the dialog area
        dialog_area_top = self.window_size[1] - self.dialog_area_height

        # Calculate the visible options
        last_visible_option = min(self.first_visible_option + self.visible_options, len(dialog_options))

        # Display the dialog options
        for i in range(self.first_visible_option, last_visible_option):
            option = dialog_options[i]
            text = self.font.render(option, True, config.BLACK)
            text_rect = text.get_rect(center=(self.window_size[0] // 2, dialog_area_top + (i - self.first_visible_option + 0.5) * option_height))
            if i == self.selected_option:
                pygame.draw.rect(self.screen, config.BLU, (text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        

    def dialog_loop2(self, dialog_options):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.selected_option = (self.selected_option + 2) % len(dialog_options)
                    elif event.key == pygame.K_w:
                        self.selected_option = (self.selected_option - 2) % len(dialog_options)
                    if event.key == pygame.K_a:
                        self.selected_option = (self.selected_option - 1) % len(dialog_options)
                    elif event.key == pygame.K_d:
                        self.selected_option = (self.selected_option + 1) % len(dialog_options)
                    elif event.key == pygame.K_SPACE:
                        print("Selected option:", str(self.selected_option))
                        return self.selected_option

            self.draw_dialog2(dialog_options)

    def draw_dialog2(self, dialog_options):
        # Calculate the height of each option box to evenly distribute them in the dialog area
        option_height = 100 // 2  # Half of the dialog area height for each option box

        # Calculate the y-coordinate for the top of the dialog area
        dialog_top = self.window_size[1] - 100

        # Calculate the position of the dialog square
        dialog_rect = pygame.Rect(20, dialog_top, self.window_size[0] - 40, 100)

        # Draw the dialog square
        pygame.draw.rect(self.screen, config.WHITE, dialog_rect)

        # Display the dialog options at specific corners of the dialog square
        top_left_rect = pygame.Rect(dialog_rect.left + 10, dialog_top + 10, dialog_rect.width // 2 - 20, option_height - 20)
        top_right_rect = pygame.Rect(dialog_rect.centerx + 10, dialog_top + 10, dialog_rect.width // 2 - 20, option_height - 20)
        bottom_left_rect = pygame.Rect(dialog_rect.left + 10, dialog_rect.centery + 10, dialog_rect.width // 2 - 20, option_height - 20)
        bottom_right_rect = pygame.Rect(dialog_rect.centerx + 10, dialog_rect.centery + 10, dialog_rect.width // 2 - 20, option_height - 20)

        for i, option in enumerate(dialog_options):
            text = self.font.render(option, True, config.BLACK)
            if i == 0:  # Top-left
                self.screen.blit(text, text.get_rect(center=top_left_rect.center))
                if self.selected_option == i:
                    pygame.draw.rect(self.screen, config.BLU, top_left_rect, 3)
            elif i == 1:  # Top-right
                self.screen.blit(text, text.get_rect(center=top_right_rect.center))
                if self.selected_option == i:
                    pygame.draw.rect(self.screen, config.BLU, top_right_rect, 3)
            elif i == 2:  # Bottom-left
                self.screen.blit(text, text.get_rect(center=bottom_left_rect.center))
                if self.selected_option == i:
                    pygame.draw.rect(self.screen, config.BLU, bottom_left_rect, 3)
            elif i == 3:  # Bottom-right
                self.screen.blit(text, text.get_rect(center=bottom_right_rect.center))
                if self.selected_option == i:
                    pygame.draw.rect(self.screen, config.BLU, bottom_right_rect, 3)

        pygame.display.flip()

    def draw_text_dialog(self, dialog_header):
        dialog_height = 500
        dialog_width = config.SCREEN_WIDTH
        dialog_x = 0
        dialog_y = config.SCREEN_HEIGHT-100

        pygame.draw.rect(self.screen, config.WHITE, (dialog_x, dialog_y, dialog_width, dialog_height))

        header_text_surface = self.font.render(dialog_header, True, config.BLACK)
        header_text_rect = header_text_surface.get_rect(center=(dialog_x + dialog_width // 2, dialog_y + 50))
        self.screen.blit(header_text_surface, header_text_rect)
        pygame.display.flip()

        nxt = True
        while nxt:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        nxt = False

    def draw_action_dialog(self, dialog_options):
        dialog_height = 100
        dialog_width = config.SCREEN_WIDTH
        dialog_x = 0
        dialog_y = config.SCREEN_HEIGHT-100

        pygame.draw.rect(self.screen, config.WHITE, (dialog_x, dialog_y, dialog_width, dialog_height))
        total_text_width = sum(self.font.size(option)[0] for option in dialog_options) + (len(dialog_options) - 1) * 10
        x_offset = (dialog_width - total_text_width) // 2  # Center horizontally in the dialog window

        for option in dialog_options:
            text_surface = self.font.render(option, True, config.BLACK)
            text_rect = text_surface.get_rect(left=(dialog_x + x_offset), centery=(dialog_y + dialog_height // 2))
            self.screen.blit(text_surface, text_rect)
            x_offset += self.font.size(option)[0] + 10

        pygame.display.flip()

        nxt = True
        while nxt:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2
                    if event.key == pygame.K_3:
                        nxt = False
                    if event.key == pygame.K_4:
                        return 4

    def update_menu(self,dialog_options,option_descriptions,header_txt,bottom_txt):
        selected_option = 0
        first_visible_option = 0
        visible_options = 5  # Number of options visible at a time
        current_category = 0

        nxt = True
        while nxt:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        selected_option = max(0, selected_option - 1)
                        if selected_option < first_visible_option:
                            first_visible_option = selected_option
                    elif event.key == pygame.K_s:
                        selected_option = min(len(dialog_options) - 1, selected_option + 1)
                        if selected_option >= first_visible_option + visible_options:
                            first_visible_option = selected_option - visible_options + 1
                    elif event.key == pygame.K_SPACE:
                        print("Selected option:", dialog_options[selected_option])
                        return selected_option
                    elif event.key == pygame.K_b:
                        return -1
            self.draw_menu(selected_option,first_visible_option,visible_options,current_category,dialog_options,option_descriptions,header_txt,bottom_txt)

    def draw_menu(self,selected_option,first_visible_option,visible_options,current_category,dialog_options,option_descriptions,header_txt,bottom_txt):
        self.screen.fill(config.WHITE)
        gray = (150, 150, 150)

        rect_width = config.SCREEN_WIDTH
        rect_height = 100

        # Calculate rectangle position to center it vertically
        rect_x = 0
        rect_y = 0

        pygame.draw.rect(self.screen, gray, (rect_x, rect_y, rect_width, rect_height))
        pygame.draw.rect(self.screen, gray, (rect_x, config.SCREEN_HEIGHT-100, rect_width, rect_height))


        dialog_height = 500
        dialog_width = 400
        dialog_x = 0
        dialog_y = 10

        self.draw_header(header_txt)
        self.draw_bottom(bottom_txt)

        # Calculate the visible options based on the current category
        if current_category == 0:  # All options
            last_visible_option = min(first_visible_option + visible_options, len(dialog_options))
        elif current_category == 1:  # Odd number options
            last_visible_option = min(first_visible_option + visible_options, len(dialog_options) // 2 + len(dialog_options) % 2)
        elif current_category == 2:  # Even number options
            last_visible_option = min(first_visible_option + visible_options, len(dialog_options) // 2)

        # Display the dialog options
        for i in range(first_visible_option, last_visible_option):
            option = dialog_options[i]
            text = self.font.render(option, True, config.BLACK)
            text_rect = text.get_rect(center=(self.window_size[0] // 6, 100 + (i - first_visible_option + 1) * 50))
            if i == selected_option:
                pygame.draw.rect(self.screen, config.BLU, (text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10))
                desc_text = self.desc_font.render(option_descriptions[i], True, config.BLACK)
                
                desc_rect = desc_text.get_rect(topright=(self.window_size[0]-200 , text_rect.centery))
                pygame.draw.rect(self.screen, config.WHITE, desc_rect)
                self.screen.blit(desc_text, desc_rect)
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def draw_header(self, txt):
        header_text_surface = self.font.render(txt, True, config.BLACK)
        header_text_rect = header_text_surface.get_rect(center=(self.window_size[0]/2, 50))
        self.screen.blit(header_text_surface, header_text_rect)


    def draw_bottom(self,txt):
        header_text_surface = self.font.render(txt, True, config.BLACK)
        header_text_rect = header_text_surface.get_rect(center=(self.window_size[0]/2, self.window_size[1]-50))
        self.screen.blit(header_text_surface, header_text_rect)