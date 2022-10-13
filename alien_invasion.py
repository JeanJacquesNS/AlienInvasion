import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
	#Inicializa o jogo e cria um objecto para a tela
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Invasão Alien")
	
	#Cria uma instância para armazenar dados estatísticos do jogo
	stats = GameStats(ai_settings)
	
	#Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	#Cria a frota de alienígenas
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			gf.update_screen(ai_settings,screen,ship,aliens,bullets)  

run_game()
