import pygame
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
  def __init__(self, startPosition):
            pygame.sprite.Sprite.__init__(self)
            self.speed = [2,2]
            self.image = pygame.image.load("images/bolinha.png")
            self.imagerect = self.image.get_rect()
            self.imagerect.centerx = startPosition[0]
            self.imagerect.centery = startPosition[1]
            self.init_pos = startPosition
    
        def update(self):
            self.imagerect.move_ip(self.speed)
            if self.imagerect.left < 0 or self.imagerect.right > 600:
                self.speed[0] = -self.speed[0]
            if self.imagerect.top < 0: 
                self.speed[1] = -self.speed[1]
            if self.imagerect.bottom > 400:
                self.imagerect.centerx = self.init_pos[0]
                self.imagerect.centery = self.init_pos[1]
