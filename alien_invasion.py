import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from counter import Counter


class AlienInvasion:
	""" Class to manage the game"""
	def __init__(self):
		"""Initialises pygame`s resources"""
		pygame.init()
		self.settings = Settings() # Creates an instance of the class Settings
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption(self.settings.caption)
		self._create_creatures()
		

	def _create_creatures(self):
		self.ship = Ship(self) # Creates an instance of the class Ship
		self.bullets = pygame.sprite.Group()
		self.counter = Counter(self)

	def run_game(self):
		# Main loop cycle of the game
		while True:
			self.settings.clock.tick(300) # FPS of the game
			self._check_events()
			self._update_screen()
			self.ship.update()
			self.bullets.update()


			for bullet in self.bullets.copy():
				if bullet.rect.y < 0:
					self.bullets.remove(bullet)
			print(len(self.bullets))


	def _update_screen(self):
		self.screen.fill(self.settings.bg_color_white) # Fills backround with a color
		self.ship.blitme() # Draws the ship
		self._update_bullets()
		self.counter.blitme(len(self.bullets))
		pygame.display.flip() # Shows everything on the screen

def _update_bullets(self):
	for bullet in self.bullets.sprites():
			bullet.draw_bullet()


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
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		# Quit when the player press the Q button
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		""" Creates a new bullet"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

if __name__ == "__main__":
	ai = AlienInvasion() # Creates an instance of the class AlienInvasion and starts the game
	ai.run_game()
