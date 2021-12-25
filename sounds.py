import pygame


class Sounds:
	"""Class to use sounds in the game"""
	def __init__(self):
		self.lose_sound = pygame.mixer.Sound("sounds/lose_sound.wav")
		self.shoot_sound = pygame.mixer.Sound("sounds/biggun1.wav")

	def play_lose_sound(self):
		self.lose_sound.play()

	def play_shoot_sound(self):
		self.shoot_sound.play()