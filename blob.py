import pygame

class Blob:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect() # Gets rect of game screen
		self.image = pygame.image.load("images/blob.bmp") # Loads blob`s texture
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Draws the blob on the game screen"""
		self.screen.blit(self.image, self.rect)