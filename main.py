#!/usr/bin/python3

import pygame
from pygame.locals import *
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption("PygameTest")
	Fujita = Charactor( 20,20 )
	while True:
		screen.fill((0,0,0,))
		Fujita.draw(screen)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

class Charactor:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.width = 50
	def draw(self,screen):
		pygame.draw.rect(screen,(0,255,0),Rect( self.x, self.y, self.width, self.width ))

if __name__ == "__main__":
	main()
