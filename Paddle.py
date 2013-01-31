import sys, pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):
  def __init__(self, startPosition):
		pygame.sprite.Sprite.__init__(self)
		#Color imagem
		self.image = pygame.image.load("images/paddle.gif")
		self.imagerect = self.image.get_rect()
		self.imagerect.centerx = startPosition[0]
		self.imagerect.centery = startPosition[1]

	def update(self):
		if self.imagerect.left < 0:
			self.imagerect.centerx += 5
		elif self.imagerect.right > 600:
			self.imagerect.centerx -= 5
