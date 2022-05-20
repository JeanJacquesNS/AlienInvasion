class Settings():
	
	def __init__(self):
		#Configurações da tela
		self.screen_width =1200
		self.screen_height = 700
		self.bg_color=(0,0,0)
		#Configurações da espaçonave
		self.ship_speed_factor = 1.5
		
		#Configuração dos projéteis
		self.bullet_speed_factor=1
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=255,0,0
		self.bullets_allowed = 4
		
		#Configurações dos alienígenas
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1
		
		
		
