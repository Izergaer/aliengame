import pygame

class Ship:
	"""Class to manage the ship"""
	def __init__(self, ai_game):
		"""Initialise the ship"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect() # Gets rect of game screen
		self.image = pygame.image.load("images/ship.png") # Loads ship`s image
		self.ships_left = ai_game.stats.ships_left
		self.image = pygame.transform.scale(self.image,(60, 48)) 
		self.rect = self.image.get_rect() # Gets rect of ship`s image
		self.rect.midbottom = self.screen_rect.midbottom # Gets starting pos of ship
		self.x = float(self.rect.x)
		# Movement states

		self.moving_right = False # State of moving
		self.moving_left = False

	def update(self):
		"""Moves the ship"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

        # Update rect object from self.x.
		self.rect.x = self.x

	def blitme(self):
		"""Draws the ship on the game screen"""
		self.screen.blit(self.image, self.rect)	

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
