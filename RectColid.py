import sys, pygame
from pygame.locals import *

class RectColid(pygame.sprite.Sprite):
  def __init__(self, startPosition):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/paddle.gif")
		self.imagerect = self.image.get_rect()
		self.imagerect.centerx = startPosition[0]
		self.imagerect.centery = startPosition[1]
