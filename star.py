from pygame.sprite import Sprite
import pygame

class Star(Sprite):
	"""A class to control stars"""
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.image = pygame.image.load("images/star.png").convert_alpha()
		self.image = pygame.transform.scale(self.image,(20,20))
		self.rect = self.image.get_rect()
		self.y = float(self.rect.y)

	def update(self):
		self.y += self.settings.star_speed
		self.rect.y = self.y
