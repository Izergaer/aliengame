import pygame.font


class Button:
	"""Class to manage button"""
	def __init__(self, ai_game, msg, pos):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		# Initialise the preferences of the button
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		# Create the button`s rect
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		

		self.pos = pos
		self._prep_pos()
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _prep_pos(self):
		if self.pos == "play_button":
			self.rect.center = self.screen_rect.center
		elif self.pos == "easy_button":
			self.rect.center = ((866, 584))
		elif self.pos == "hard_button":
			self.rect.center = ((158, 584))

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)