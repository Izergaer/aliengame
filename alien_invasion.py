import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from counter import Counter
from alien import Alien 


class AlienInvasion:
	""" Class to manage the game"""
	def __init__(self):
		"""Initialises pygame`s resources"""
		pygame.init()
		self.settings = Settings() # Creates an instance of the class Settings
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption(self.settings.caption)
		self._create_instances()
		self._create_fleet()

	def _create_instances(self):
		"""Method that creates instances of every class we need"""
		self.ship = Ship(self) # Creates an instance of the class Ship
		self.bullets = pygame.sprite.Group() # Creates a group for the bullets 
		self.counter = Counter(self) # Creates an insctance of the ammo counter
		self.aliens = pygame.sprite.Group() # Creates a group for the aliens

	def run_game(self):
		"""Main cycle of the game""" 
		while True:
			self.settings.clock.tick(300) # FPS of the game
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()

	def _create_fleet(self):
		"""Method that controls a fleet of the aliens"""

	def _update_screen(self):
		"""Method that controls everything on the screen"""
		self.screen.fill(self.settings.bg_color_white) # Fills backround with a color
		self.ship.blitme() # Draws the ship
		self.counter.blitme(len(self.bullets)) # Calls the method of the counter to change the digit on the screen
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()	# Draws the bullets on the screen
		pygame.display.flip() # Shows everything on the screen

	def _update_bullets(self):
		self.bullets.update()
		# Deletes unnecesary bullets
		for bullet in self.bullets.copy():
			if bullet.rect.y < 0:
				self.bullets.remove(bullet)
		print(len(self.bullets)) # Debug

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
		# Quit when the player presses the Q button
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		# Stop moving when the key isn`t pressed
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		""" Creates a new bullet"""
		# Checks number of bullets on the screen
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

if __name__ == "__main__":
	ai = AlienInvasion() # Creates an instance of the class AlienInvasion and starts the game
	ai.run_game()
