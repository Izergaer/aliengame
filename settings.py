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
		self.ship_speed = 1 
		self.ships_amount = 3

		# Bullet
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Star
		self.star_speed = 0.1

		# Alien
		self.alien_speed = 0.5
		self.drop_speed = 10
		self.fleet_direction = 1