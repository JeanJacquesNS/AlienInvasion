import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#Inicializa o jogo e cria um objecto para a tela
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Invasão Alien")
	
	#Cria uma espaçonave
	ship = Ship(ai_settings,screen)
	
	#Cria um grupo no qual serão armazenados os projéteis
	bullets = Group()
	
	#Cria um alienígena
	alien = Alien(ai_settings,screen)
	
	#Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,alien,bullets)  

run_game()
