import pygame

class Ship():
	
	def __init__(self,ai_settings,screen):
		#Incializa a espaçonave e define a sua posição inicial
		self.screen = screen
		self.ai_settings= ai_settings
		#Carrega a imagem da espaçonave e obtém seu rect
		self.image= pygame.image.load('images/ship.bmp')
		self.rect= self.image.get_rect()
		self.screen_rect= screen.get_rect()
		
		#Inicia cada nova espaçonave na parte inferior central da tela
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Armazena um valor decimal para o centro da espaçonave
		self.center= float(self.rect.centerx)
		
		#Flag de movimento
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right:
			self.rect.centerx +=self.ai_settings.ship_speed_factor
		elif self.moving_left:
			self.rect.centerx -=self.ai_settings.ship_speed_factor
			
		#Actualiza o objecto rect de acordo com o self.center
		#self.rect.centerx = self.center
		 
		#Actualiza o valor do centro da espaçonave, e não o rectângulo
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#Actualiza o objecto rect de acordo com self.center
		self.rect.centerx = self.center
	def blitme(self):
		#Desenha a espaçonave em sua posição atual
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		#Centraliza a espaçonave na tela.
		self.center=self.screen_rect.centerx
