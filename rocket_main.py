import sys
import pygame
from rocket import Rocket

class RocketGame:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("Rocket Game")
		self._create_creatures()

	def _create_creatures(self):
		self.rocket = Rocket(self)

	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()
			self.rocket.update()

	def _update_screen(self):
		self.screen.fill((230, 230, 230) # Fills backround with a color
		 # Draws the rocket
		pygame.display.flip() # Shows everything on the screen

	def _check_events(self):
		""" Looking for special events from user input"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				
				# Moving events
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = True
		# Quit when the player press the Q button
		elif event.key == pygame.K_q:
			sys.exit()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = False
		if event.key == pygame.K_LEFT:
			self.rocket.moving_left = False
		if event.key == pygame.K_UP:
			self.rocket.moving_forward = False
		if event.key == pygame.K_DOWN:
			self.rocket.moving_backward = False


if __name__ == "__main__":
	ai = RocketGame() # Creates an instance of the class AlienInvasion and starts the game
	ai.run_game()