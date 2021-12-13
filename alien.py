import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to control alien`s behavior"""
	def __init__(self, ai_game): # Initialise things we need
		super().__init__()
		self.screen = ai_game.screen #
		self.settings = ai_game.settings
		self.image = pygame.load("images/alien.bmp") # Loads the image of aliens
		self.rect = self.image.get_rect() # Gets rect of the image

		# Start each new alien near top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)