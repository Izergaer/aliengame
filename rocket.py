import sys
import pygame

class Rocket:
	"""Class to manage the rocket"""
	def __init__(self, ai_game):
		"""Initialise the rocket"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect() # Gets rect of game screen
		self.image = pygame.image.load("images/rocket.png").convert_alpha() # Loads rocket`s image 
		self.rect = self.image.get_rect() # Gets rect of rocket`s image
		self.rect.midbottom = self.screen_rect.midbottom # Gets starting pos of rocket
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement states

		self.moving_right = False # State of moving right
		self.moving_left = False # State of moving left
		self.moving_forward = False
		self.moving_backward = False

	def update(self):
		"""Moves the rocket"""
		# Check if the rocket on the edge of the screen
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += 1
		if self.moving_left and self.rect.left > 0:
			self.x -= 1
		if self.moving_backward and self.rect.bottom > self.screen_rect.bottom:
			self.y += 1
		if self.moving_forward and self.rect.top < self.screen_rect.top:
			self.y -= 1
	
		self.rect.x = self.x
		self.rect.y = self.y
		
	def blitme(self):
		"""Draws the rocket on the game screen"""
		self.screen.blit(self.image, self.rect)