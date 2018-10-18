
import pygame
from pygame.locals import *
import sys

def main():
      pygame.init() # 初期化
      screen = pygame.display.set_mode((600, 400))
      pygame.display.set_caption("Pygame Test")

      while True:
          pygame.display.update()

          for event in pygame.event.get():
                if event.type == QUIT:
                      pygame.quit()
                      sys.exit()

if __name__ == "__main__":
      main()
