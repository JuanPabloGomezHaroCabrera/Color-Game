import pygame

class Fonts:
    def __init__(self):
        pygame.font.init()
        self.fuente1 = pygame.font.Font(None, 60)
        self.fuente2 = pygame.font.Font(None, 30)
        self.fuente3 = pygame.font.Font(None, 20)