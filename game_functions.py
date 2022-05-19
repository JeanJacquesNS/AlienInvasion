import sys
import pygame
from bullet import Bullet

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
			
				
def update_screen(ai_settings,screen,ship,bullets):
	#Redesenha a tela a cada passagem pelo laco
	screen.fill(ai_settings.bg_color)
	#Redesenha todos o projéteis atrás da espaçonave e dos alienígenas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
		
	#Deixa a tela mais recente visível
	pygame.display.flip()

def update_bullets(bullets):
	#Livra-se dos projéteis que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
