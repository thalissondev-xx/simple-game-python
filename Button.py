import pygame, sys
from pygame.locals import *

class Button(pygame.sprite.Sprite):
	def __init__(self, startPosition):
		pygame.sprite.Sprite.__init__(self)
		self.btn = pygame.image.load("images/start.png")
		self.btnrect = self.btn.get_rect()
		self.btnrect.centerx = startPosition[0]
		self.btnrect.centery = startPosition[1]

	def pressed(self, mouse):
		if mouse[0] > self.btnrect.topleft[0]:
			if mouse[1] > self.btnrect.topleft[1]:
				if mouse[0] < self.btnrect.bottomright[0]:
					if mouse[1] < self.btnrect.bottomright[1]:
						return True
					else:return False
				else:return False
			else:return False
		else:return False