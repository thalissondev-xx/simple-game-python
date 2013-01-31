import sys, pygame, os
from Ball import Ball
from Paddle import Paddle
from RectColid import RectColid
from pygame.locals import *
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255, 255, 255

class Game(object):

  def loopGame(self):
		clock = pygame.time.Clock()
		ball = Ball([100,100])
		paddle = Paddle([width/2,395])
		font = pygame.font.Font(None, 25)
		sound_collision = pygame.mixer.Sound("music/tick.mp3")
		vector = []
		posRectx = 90
		posRecty = 60
		score = 0
		for i in range(0, 50):
			if(i%5==0):
				posRecty = posRecty + 20
				posRectx = 80
			else:
				posRectx = posRectx + 80
				rectColid = RectColid([posRectx,posRecty])
				vector.append(rectColid)

		running_game = True
		while running_game:
			clock.tick(120)

			textoScore = font.render("Score: %d" % score, True, white)

			for event in pygame.event.get():
				if event.type==QUIT:
					running_game = False

			keys = pygame.key.get_pressed()

			if keys[K_a]:
				paddle.imagerect.centerx -= 5
			if keys[K_d]:
				paddle.imagerect.centerx += 5

			if paddle.imagerect.colliderect(ball.imagerect):
				if ball.speed[1] > 0:
					ball.speed[1] = -ball.speed[1]

			for rect in vector:
				if rect.imagerect.colliderect(ball.imagerect):
					vector.remove(rect)
					ball.speed[1] = -ball.speed[1]
					sound_collision.play(1)
					score += 1

			ball.update()
			paddle.update()

			screen.fill(black)
			screen.blit(ball.image, ball.imagerect)
			screen.blit(paddle.image, paddle.imagerect)
			#Coloca os objetos na tela
			for rect in vector:
				screen.blit(rect.image, rect.imagerect)
			screen.blit(textoScore, [10, 10])

			pygame.display.flip()

if __name__ == "__main__":
	Game().loopGame()
