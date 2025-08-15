import pygame
import random

class Inimigo:
    def __init__(self, largura, altura, cor, raio, velocidade_range):
        self.rect = pygame.Rect(0, 0, raio * 2, raio * 2)
        self.rect.x = random.randrange(0, largura - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.raio = raio
        self.cor = cor
        self.velocidade = random.randrange(*velocidade_range)

    def mover(self):
        self.rect.y += self.velocidade

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, self.rect.center, self.raio)
