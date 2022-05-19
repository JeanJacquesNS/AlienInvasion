import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self,ai_settings,screen,ship):
		#Cria um object para o projétil na posição actual da espaçonave
		super(Bullet,self).__init__()
		self.screen=screen
		
		#Cria um rectângulo para o projétil em (0,0) e, em seguida, define a posição correcta
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#Armazena a posição do projétil como um valor decimal
		self.y=float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
			#Actualiza a posição decimal do projétil
			self.y -= self.speed_factor
			#Actualiza a posição de rect
			self.rect.y= self.y 
		
	def draw_bullet(self):
		#Desenha o projétil na tela
		pygame.draw.rect(self.screen,self.color,self.rect)
