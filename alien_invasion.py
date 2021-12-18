import sys, pygame
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from counter import Counter
from alien import Alien 
from star import Star


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
		self._create_star()

	def _create_instances(self):
		"""Method that creates instances of every class we need"""
		self.bullets = pygame.sprite.Group() # Creates a group for the bullets 
		self.aliens = pygame.sprite.Group() # Creates a group for the aliens
		self.stars = pygame.sprite.Group() # Creates a group for the stars
		self.counter = Counter(self) # Creates an insctance of the ammo counter
		self.ship = Ship(self) # Creates an instance of the class Ship

	def run_game(self):
		"""Main cycle of the game""" 
		while True:
			self.settings.clock.tick(300) # FPS of the game
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
			self.aliens.update()
			self._check_borders()
			print("FPS:", int(self.settings.clock.get_fps()))
			print(self.stars)

	def _create_fleet(self):
		"""Method that controls a fleet of the aliens"""
		# Make an alien
		alien = Alien(self)
		self.aliens.add(alien)
		# Alien`s settings
		alien_width, alien_height = alien.rect.size	
		# Space that we can use
		available_space_x = self.settings.screen_width - (2 * alien_width)
		# Number of aliens that can fit on the screen
		number_aliens_x = available_space_x // (2 * alien_width)
		# Number of rows
		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
		number_rows = available_space_y // (2 * alien_width)
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)	

	def _check_borders(self):
		for alien in self.aliens:
			if alien.check_edges():
				for alien in self.aliens:
					alien.rect.y += self.settings.drop_speed
				self.settings.fleet_direction *= -1
				break

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)


	def _create_star(self):
		"""Method that creates the stars"""
		for star in range(randint(20, 25)): # Gets random number of the stars
			star = Star(self)
			star.rect.x = randint(0, 640) # Gets random coordinates of the stars
			star.rect.y = randint(0, 470) 
			self.stars.add(star)

	def _update_screen(self):
		"""Method that controls everything on the screen"""
		self.screen.fill(self.settings.bg_color_white) # Fills backround with a color
		self.stars.draw(self.screen)
		self.ship.blitme() # Draws the ship
		self.counter.blitme(len(self.bullets)) # Calls the method of the counter to change the digit on the screen
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()	# Draws the bullets on the screen
		self.aliens.draw(self.screen)
		pygame.display.flip() # Shows everything on the screen

	def _update_stars(self):
		"""Method that updates stars"""
		self.stars.update()
		for star in self.stars.copy():
			if star.rect.y > 480:
				self.bullets.remove(star)
				if randint(0, 5) == 5:
					self._create_star(1)
				else:
					pass

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
