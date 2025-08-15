import pygame
import random
import nave as n
from asteroide import Asteroide, AsteroideVeloz

def game():
    pygame.init()

    ALTURA, LARGURA = 600, 800
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 36)

    def aumentar_velocidade(inimigo):
        inimigo.velocidade += 1
        return inimigo

    def reset_game():
        nonlocal nave, asteroides, pontuacao, game_over
        nave = n.Nave(50, 50, LARGURA, cor=(255, 0, 255))
        asteroides = []
        pontuacao = 0
        game_over = False

    nave = n.Nave(50, 50, LARGURA, cor=(255, 0, 255))
    asteroides = []
    pontuacao = 0
    game_over = False

    ADD_INIMIGO = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_INIMIGO, 500)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if not game_over:
                if evento.type == ADD_INIMIGO:
                    
                    if random.choice([True, False]):
                        novo_inimigo = Asteroide(LARGURA, ALTURA)
                    else:
                        novo_inimigo = AsteroideVeloz(LARGURA, ALTURA, cor=(255, 100, 100))
                    asteroides.append(novo_inimigo)
                
                if evento.type == pygame.KEYDOWN:
                    
                    if evento.key == pygame.K_DOWN:
                        asteroides = list(map(aumentar_velocidade, asteroides))
            else:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    reset_game()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False


        if not game_over:
            nave.mover()

            for ast in asteroides[:]:
                ast.mover()
                if ast.rect.top > ALTURA:
                    asteroides.remove(ast)

            for tiro in nave.tiros[:]:
                for ast in asteroides[:]:
                    if tiro.rect.colliderect(ast.rect):
                        
                        if ast.tipo == 'veloz':
                            pontuacao += 10
                        else: 
                            pontuacao += 5
                        
                        asteroides.remove(ast)
                        nave.tiros.remove(tiro)
                        break

            for ast in asteroides:
                if nave.nave.colliderect(ast.rect):
                    game_over = True

        tela.fill((0, 0, 0))
        nave.desenhar(tela)
        for ast in asteroides:
            ast.desenhar(tela)

        texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
        tela.blit(texto_pontuacao, (10, 10))

        if game_over:
            texto_game_over = fonte.render("GAME OVER", True, (255, 0, 0))
            texto_restart = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
            texto_sair = fonte.render("Pressione ESC para sair", True, (255, 255, 255))
            tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - 50))
            tela.blit(texto_restart, (LARGURA // 2 - texto_restart.get_width() // 2, ALTURA // 2))
            tela.blit(texto_sair, (LARGURA // 2 - texto_sair.get_width() // 2, ALTURA // 2 + 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game()