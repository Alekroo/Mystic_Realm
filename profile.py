import pygame
import config	

"""
Used to create and display players profile.
"""

class Profile:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.nxt = True

    def display_profile(self):
        profile_width = 500
        profile_height = 500
        profile_x = (self.screen.get_width() - profile_width) // 2
        profile_y = (self.screen.get_height() - profile_height) // 2


        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(profile_x, profile_y, profile_width, profile_height))

        title_text = self.font.render(f"Name: {self.player.name}", True, (0, 0, 0))
        title_x = profile_x + (profile_width - title_text.get_width()) // 2
        title_y = profile_y + 10
        self.screen.blit(title_text, (title_x + 40, title_y+30))

        level_text = self.font.render(f"Level: {self.player.level}", True, (0, 0, 0))
        self.screen.blit(level_text, (title_x + 40, title_y + 60))


        self.player.update_experience()
        experience_text = self.font.render(f"Experience: {self.player.experience} / {self.player.req_xp}", True, (0, 0, 0))
        self.screen.blit(experience_text, (title_x + 40, title_y + 90))

        gold_text = self.font.render(f"Gold: {self.player.gold}", True, (0, 0, 0))
        self.screen.blit(gold_text, (title_x + 40, title_y + 120))

        pp = self.player.portrait
        pp = pygame.transform.scale(pp, (config.SCALE*5, config.SCALE*5))
        rect = pygame.Rect(profile_x+30,profile_y+20,pp.get_width()-100,pp.get_height())
        self.screen.blit(pp, rect)

        sword_text = self.font.render(f"Health Points: {self.player.health} / {self.player.max_health}", True, (0, 0, 0))
        self.screen.blit(sword_text, (profile_x + 30, pp.get_height() + 90))

        sword_text = self.font.render(f"Mana Points: {self.player.mana} / {self.player.max_mana}", True, (0, 0, 0))
        self.screen.blit(sword_text, (profile_x + 30, pp.get_height() + 120))

        sword_text = self.font.render(f"Damage: {str(self.player.sword.damage[0])}" + " - " + f"{str(self.player.sword.damage[1])}", True, config.BLACK)
        self.screen.blit(sword_text, (profile_x + 30, pp.get_height() + 150))

        sword_text = self.font.render(f"Weapon Equipped: {self.player.sword.name}", True, (0, 0, 0))
        self.screen.blit(sword_text, (profile_x + 30, pp.get_height() + 180))

        pygame.display.flip()

    def profile_update(self):
    	self.display_profile()
    	self.nxt = True
    	while self.nxt:
    		for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                pygame.quit()
	                sys.exit()
	            elif event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_c:
	                    self.nxt = False
    	self.nxt = True