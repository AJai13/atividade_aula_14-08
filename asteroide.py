import random
import inimigo


class Asteroide(inimigo.Inimigo):
    def __init__(self, largura, altura, **kwargs):
        cor = kwargs.get("cor", (255, 255, 255))
        raio = 20
        velocidade_range = (1, 8)
        super().__init__(largura, altura, cor, raio, velocidade_range)
        self.tipo = 'comum'

class AsteroideVeloz(Asteroide):
    def __init__(self, largura, altura, **kwargs):
        super().__init__(largura, altura, **kwargs)
        self.velocidade = random.randrange(8, 15)
        self.cor = (255, 100, 100) 
        self.tipo = 'veloz'