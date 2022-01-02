class GameStats:
	def __init__(self, ai_game):
		self.settings = ai_game.settings 
		self.reset_stats()
		self.score = 0
		self.high_score = ai_game.highscore.get_highscore()
		self.level = 1 

	def reset_stats(self):
		self.ships_left = self.settings.ships_amount
		self.score = 0
		self.level = 1
