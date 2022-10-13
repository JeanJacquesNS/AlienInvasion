import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		#Move a espaçonave para a direita
		ship.moving_right=True
	elif event.key == pygame.K_LEFT:
		#Move a espaçonave para a esquerda
		ship.moving_left=True
	elif event.key == pygame.K_SPACE:
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(ai_settings,screen,ship,bullets)
		
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
						
def check_keyup_events(event,ship):
	if event.key== pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key==pygame.K_LEFT:
		ship.moving_left = False
		
def check_events(ai_settings, screen,ship,bullets):
	#Observa eventos de teclado e de mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
				
def update_screen(ai_settings,screen,ship,aliens,bullets):
	#Redesenha a tela a cada passagem pelo laco
	screen.fill(ai_settings.bg_color)
	#Redesenha todos o projéteis atrás da espaçonave e dos alienígenas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
		
	#Deixa a tela mais recente visível
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	#Livra-se dos projéteis que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#Verifica se algum projétil atingiu os aliens
	#Em caso afirmativo, livra-se do projétil e do alien
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	
	if len(aliens)==0:
		#Destrói os projéteis existentes e cria uma frota
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)
		

def get_number_aliens_x(ai_settings,alien_width):
	#Determina o número de aliens que cabem em uma linha.
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x/(2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	#Determina o número de linhas com aliens que cabem na tela
	available_space_y= (ai_settings.screen_height - (2 * alien_height)-ship_height)
	number_rows = int(available_space_y / (3 * alien_height))
	return number_rows
		
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	#Cria um alien e o posiciona na linha
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number 
	alien.rect.x = alien.x
	alien.rect.y= alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def update_aliens(aliens):
	#Actualiza as posições de todos os alienígenas da frota
	aliens.update()
	
def create_fleet(ai_settings,screen,ship,aliens):
	#Cria um alien e calcula o número de aliens em uma linha
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	#Cria a primeira linha de alienígenas
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#Cria um alienígena e o posiciona na linha
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges (ai_settings,aliens):
	#Responde apropriadamente se algum alien atingir uma borda
	
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
			
def change_fleet_direction(ai_settings,aliens):
	#Faz toda a frota descer e muda a sua direção
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	
def update_aliens(ai_settings,ship,aliens):
	#Verifica se a frota está em uma das bordas e então actualiza as posições de todos aliens da frota
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	#Verifica se houve colisões entre alienígenas e a espaçonave
	if pygame.sprite.spritecollideany(ship,aliens):
		print("BOOOOM!!!")
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	#Responde ao fato de a espaçonave ter sido atingida por um alienígena.
	#Decrementa ships_left
	stats.ships_left -=1
	
	#esvazia a lista de alienígenas e de projéteis
	aliens.empty()
	bullets.empty()
	
	#cria uma nova frota e centraliza a espaçonave
	create_fleet(ai_settings,screen,ship,aliens)
	ship.center_ship()
	
	#Faz uma pausa
	sleep(0.5)
	
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	#Verifica se a frota está em uma das bordas e então actualiza as posições de todos aliens da frota
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	#Verifica se houve colisões entre alienígenas e a espaçonave
	if pygame.sprite.spritecollideany(ship,aliens):
		print("BOOOOM!!!")
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
