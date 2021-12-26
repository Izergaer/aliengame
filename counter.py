import pygame

class Counter:
	def __init__(self, ai_game, pos):
		self.pos = pos

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.image_3 = pygame.image.load("images/3.bmp")
		self.image_2 = pygame.image.load("images/2.bmp")
		self.image_1 = pygame.image.load("images/1.bmp")
		self.image_0 = pygame.image.load("images/0.bmp")
		self.rect = self.image_0.get_rect()		
		self._define_pos()

	def blitme(self, length):
		if length == 3:
			self.screen.blit(self.image_0, self.rect)
		if length == 2:
			self.screen.blit(self.image_1, self.rect)
		if length == 1:
			self.screen.blit(self.image_2, self.rect)
		if length == 0:
			self.screen.blit(self.image_3, self.rect)

	def _define_pos(self):
		if self.pos == "topright":
			self.rect.topright = self.screen_rect.topright
		elif self.pos == "topleft":
			self.rect.topleft = self.screen_rect.topleft