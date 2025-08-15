import pygame

class Tiro:
    def __init__(self, pos_x, pos_y, cor=(255, 255, 0)):
        self.rect = pygame.Rect(pos_x, pos_y, 5, 15)
        self.cor = cor

    def mover(self):
        self.rect.y -= 10