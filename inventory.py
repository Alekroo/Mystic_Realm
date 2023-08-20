import pygame
import config

"""
Setsup players inventory.
Displays and handles it. 
"""

class Inventory():
    def __init__(self, player, screen):
        self.screen = screen
        self.player = player
        self.selected_item_index = 0
        self.font = pygame.font.Font(None, 24)
        self.nxt = True

    def show_inventory(self):
        # Calculate the position to center the inventory
        inventory_width = 300
        inventory_height = 300
        inventory_x = (self.screen.get_width() - inventory_width) // 2
        inventory_y = (self.screen.get_height() - inventory_height) // 2

        # Draw the inventory square
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(inventory_x, inventory_y, inventory_width, inventory_height))

        # Display the inventory title
        title_text = self.font.render("Inventory", True, (0, 0, 0))
        title_x = inventory_x + (inventory_width - title_text.get_width()) // 2
        title_y = inventory_y + 10
        self.screen.blit(title_text, (title_x, title_y))

        item_x = 0
        item_y = 0

        # Display each item in the inventory
        for index, item in enumerate(self.player.inventory):
            item_text = self.font.render(f"{item.name}", True, (0, 0, 0))
            item_x = inventory_x + 10
            item_y = inventory_y + 40 + index * 30
            self.screen.blit(item_text, (item_x, item_y))

        # Highlight the selected item
        selected_item_rect = pygame.Rect(item_x - 5, inventory_y + 32 + self.selected_item_index * 30, inventory_width - 20, 30)
        pygame.draw.rect(self.screen, (0, 0, 0), selected_item_rect, 2)
        pygame.display.flip()

    def inventory_update(self):
        self.show_inventory()
        self.nxt = True
        while self.nxt:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        self.nxt = False
                    elif event.key == pygame.K_w:
                        self.selected_item_index = max(0, self.selected_item_index - 1)
                        self.show_inventory()
                    elif event.key == pygame.K_s:
                        self.selected_item_index = min(len(self.player.inventory) - 1, self.selected_item_index + 1)
                        self.show_inventory()
                    elif event.key == pygame.K_SPACE:
                        self.player.use_item(self.player.inventory[self.selected_item_index])
                        self.selected_item_index = self.selected_item_index - 1
                        self.show_inventory()
        self.nxt = True
