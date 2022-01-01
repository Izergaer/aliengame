import pygame.font


class ScoreBoard:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# The font settings
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prepare the initial score

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)

	def prep_score(self):
		rounded_score = round(self.stats.score, -1) # Use the rounded value of the score
		score_str = f"{rounded_score:,}"
		self.score_image = self.font.render(f"{score_str} score", True, self.text_color,)
		self.score_rect = self.score_image.get_rect()
		
		# The coords of the button
		self.score_rect.right = self.screen_rect.right - 40
		self.score_rect.top = 20

	def prep_high_score(self):
		high_score = round(self.stats.high_score, -1)
		high_score_str = f"{high_score:,}"
		self.high_score_image = self.font.render(f"{high_score_str} high score", True, 
			self.text_color,)
		
		# The coords of the button
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(f"{level_str} level", True,
				self.text_color,)
	
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
