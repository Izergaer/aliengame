import pygame


class Settings:
	"""Class to manage settings"""
	def __init__(self):
		# Screen settings
		self.screen_width = 1024
		self.screen_height = 768
		self.bg_color_white = (230, 230, 230)
		self.bg_color_blue = (135, 206, 235)
		self.bg_color_black = (0, 0, 0)
		self.caption = "Alien Invasion"
		self.clock = pygame.time.Clock() # FPS of the game
		
		# Ship
		self.ships_amount = 3

		# Bullet
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien	
		self.drop_speed = 10
		self.alien_points = 50

		self.speedup_scale = 1.1

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		self.alien_speed = 0.5
		self.bullet_speed = 1.5
		self.ship_speed = 1.0

		self.fleet_direction = 1

	def increase_speed(self, speedup_scale = 1.1):
		self.alien_speed *= speedup_scale 
		self.bullet_speed *= speedup_scale
		self.ship_speed *= speedup_scale
		self.alien_points *= 1.5  	