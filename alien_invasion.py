import sys, pygame
from time import sleep
from random import randint
from game_stats import GameStats
from sounds import Sounds
from settings import Settings
from ship import Ship
from bullet import Bullet
from counter import Counter
from alien import Alien 
from star import Star
from button import Button
from scoreboard import ScoreBoard


class AlienInvasion:
	""" Class to manage the game"""
	def __init__(self):
		"""Initialises pygame`s resources"""
		pygame.init()
		self.settings = Settings() # Creates an instance of the class Settings
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption(self.settings.caption)
		self._create_instances() # Create instances of the classes we need
		self._create_fleet() # Create the first fleet
		self._create_star() # Create stars
		self.game_active = False # Create game with the True game_active flag 
		# pygame.mouse.set_visible(False)

	def _create_instances(self):
		"""Method that creates instances of every class we need"""
		self.stats = GameStats(self) # Stats
		self.bullets = pygame.sprite.Group() # Creates a group for the bullets 
		self.aliens = pygame.sprite.Group() # Creates a group for the aliens
		self.stars = pygame.sprite.Group() # Creates a group for the stars
		self.counter_bullets = Counter(self, "topright") # Creates an insctance of the ammo counter
		self.counter_ships = Counter(self, "topleft")
		self.ship = Ship(self) # Creates an instance of the class Ship
		self.sounds = Sounds()
		
		# Buttons
		self.play_button = Button(self, "Play", "play_button")
		self.easy_button = Button(self, "Easy", "easy_button")
		self.hard_button = Button(self, "Hard", "hard_button")

		self.scoreboard = ScoreBoard(self)

	def run_game(self):
		"""Main cycle of the game""" 
		while True:
			pygame.time.Clock().tick(500) # FPS of the game
			if self.game_active:
				self.ship.update() # Update the ship
				self.aliens.update() # Update aliens
			self._check_events() # Check user`s events
			self._check_aliens_position() # See the method commentary
			self._check_borders() # See the method commentary
			self._check_bottom() # See the method commentary
			self._update_bullets() # Update bullets
			self._update_screen() # Update image on the screen
			
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

	def _check_aliens_position(self):
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

	def _ship_hit(self):
		if self.stats.ships_left:
			self.stats.ships_left -= 1
			# Delete aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Center the ship
			self.ship.center_ship()

			# Play the lose music
			self.sounds.play_lose_sound()

			self._create_fleet()

			# Pause the game
			sleep(0.5)
		else:
			self.game_active = False
			pygame.mouse.set_visible(True)

	def _check_borders(self):
		# Check whether an alien touches a border of the screen
		for alien in self.aliens:
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _check_bottom(self):
		screen_rect = self.screen.get_rect()
		# Check whether an alien touches the bottom of the screen
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _change_fleet_direction(self):
		# Change fleet`s direction when an alien touches a border of the screen
		for alien in self.aliens:
			alien.rect.y += self.settings.drop_speed
		self.settings.fleet_direction *= -1	

	def _create_alien(self, alien_number, row_number):
		# Creates aliens
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
			star.rect.x = randint(0, 1024) # Gets random coordinates of the stars
			star.rect.y = randint(0, 768) 
			self.stars.add(star)

	def _update_screen(self):
		"""Method that controls everything on the screen"""
		self.screen.fill(self.settings.bg_color_white) # Fills backround with a color
		self.stars.draw(self.screen)
		self.ship.blitme() # Draws the ship
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()	# Draws the bullets on the screen
		self.aliens.draw(self.screen)
		self.counter_bullets.blitme(len(self.bullets)) # Calls the method of the counter to change the digit on the screen
		self.counter_ships.blitme(self.stats.ships_left)
		if self.game_active:
			self.scoreboard.show_score()
		if not self.game_active:
			self.easy_button.draw_button()
			self.hard_button.draw_button()
		pygame.display.flip() # Shows everything on the screen

	def _update_bullets(self):
		self.bullets.update()
		# Deletes unnecesary bullets
		for bullet in self.bullets.copy():
			if bullet.rect.y < 0:
				self.bullets.remove(bullet)
		self._check_bullets_and_aliens_collisions()

	def _check_bullets_and_aliens_collisions(self):
		# Checks whether a bullet hits an alien
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, 
			True, True)
		if collisions:
			for aliens in collisions.values():
				"""Add score for every killed alien"""
				self.stats.score += self.settings.alien_points * len(aliens)
			"""Change score"""
			self.scoreboard.prep_score()
			
		if not self.aliens:
			"""If all aliens are dead"""
			self.settings.increase_speed()
			self.bullets.empty()
			self.ship.center_ship()
			self._create_fleet()
			self.stats.level += 1
			self.scoreboard.prep_level()
			self.scoreboard.check_high_score()

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
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_easy_and_hard_buttons(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		# Quit when the player presses the Q button
		elif event.key == pygame.K_q:
			sys.exit()
		# Debug button
		elif event.key == pygame.K_F12:
			self._ship_hit()
		# Restart game if the player presses the P button
		elif event.key == pygame.K_p:
			if not self.game_active:
				self._restart_game()
		if self.game_active:
			if event.key == pygame.K_SPACE:
				self._fire_bullet()

	def _check_play_button(self, mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active: # Let click the Play button if only the game isn`t currently active
			self._restart_game()

	def _check_easy_and_hard_buttons(self, mouse_pos):
		if self.easy_button.rect.collidepoint(mouse_pos) and not self.game_active:
			self._restart_game()
		elif self.hard_button.rect.collidepoint(mouse_pos) and not self.game_active:
			self._restart_game(True)

	def _restart_game(self, hard = False):
		self.stats.reset_stats()
		self.aliens.empty() # Delete unneseccary aliens
		self.bullets.empty() # Delete unneseccary bullets
		self._create_fleet()
		self.ship.center_ship()
		self.settings.initialise_dynamic_settings()
		# Prepare scoreboard
		self.scoreboard.prep_score()
		self.scoreboard.prep_high_score()
		self.scoreboard.prep_level()

		if hard:
			self.settings.increase_speed(2)
		pygame.mouse.set_visible(False)
		self.game_active = True

	def _change_(self):
		pass

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
			self.sounds.play_shoot_sound()

if __name__ == "__main__":
	ai = AlienInvasion() # Creates an instance of the class AlienInvasion and starts the game
	ai.run_game()
