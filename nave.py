import pygame
import tiro as t


class Nave:
    def __init__(self, pos_x, pos_y, largura_tela, **kwargs):
        self.nave = pygame.Rect(pos_x, pos_y, 50, 50)
        self.nave.centerx = largura_tela // 2
        self.nave.bottom = 550
        self.cor = kwargs.get("cor", (255, 255, 0))
        self.largura_tela = largura_tela
        self.tiros = []
        self.cooldown = 0

    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and self.nave.left > 0:
            self.nave.x -= 5
        if teclas[pygame.K_RIGHT] and self.nave.right < self.largura_tela:
            self.nave.x += 5

        self.atirar()
        self.mover_tiros()

    def atirar(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            tiro = t.Tiro(self.nave.centerx - 2, self.nave.top)
            self.tiros.append(tiro)
            self.cooldown = 20

    def mover_tiros(self):
        for tiro in self.tiros:
            tiro.mover()
            if tiro.rect.bottom < 0:
                self.tiros.remove(tiro)

    def desenhar(self, tela):
        posicao_triangulo = [
            (self.nave.centerx, self.nave.top),
            (self.nave.left, self.nave.bottom),
            (self.nave.right, self.nave.bottom),
        ]
        pygame.draw.polygon(tela, self.cor, posicao_triangulo)

        for tiro in self.tiros:
            pygame.draw.rect(tela, tiro.cor, tiro.rect)