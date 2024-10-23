import pygame
import time
import random

pygame.init()

# Cores usadas
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definição da tela
largura_tela = 1400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Definições da cobra
tamanho_celula = 10
velocidade = 15
clock = pygame.time.Clock()

# Fontes para mensagens e pontuação
fonte = pygame.font.SysFont("bahnschrift", 25)

# Função para mostrar a pontuação
def pontuação(score):
    valor = fonte.render("Pontuação: " + str(score), True, branco)
    tela.blit(valor, [0, 0])

# Função para desenhar a cobra
def cobra(tamanho_celula, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_celula, tamanho_celula])

# Função principal do jogo
def jogo():
    # Posições iniciais da cobra
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    # Movimento inicial
    x_mudanca = 0
    y_mudanca = 0

    # Corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0) * 10.0
    y_comida = round(random.randrange(0, altura_tela - tamanho_celula) / 10.0) * 10.0

    # Variável de controle do Loop
    fim_jogo = False
    perdeu = False

    while not fim_jogo:

        # Verifica se o jogador perdeu
        while perdeu:
            tela.fill(azul)
            mensagem = fonte.render("Você perdeu! Pressione Q-Quit ou C-Continuar", True, vermelho)
            tela.blit(mensagem, [largura_tela / 8, altura_tela / 3])
            pontuação(comprimento_cobra - 1)
            pygame.display.update()

            # Opções após perder
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        perdeu = False
                    if evento.key == pygame.K_c:
                        jogo()  # Reinicia o jogo

        # Eventos de movimento
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    x_mudanca = -tamanho_celula
                    y_mudanca = 0
                elif evento.key == pygame.K_d:
                    x_mudanca = tamanho_celula
                    y_mudanca = 0
                elif evento.key == pygame.K_w:
                    y_mudanca = -tamanho_celula
                    x_mudanca = 0
                elif evento.key == pygame.K_s:
                    y_mudanca = tamanho_celula
                    x_mudanca = 0

        # Atualiza a posição da cobra
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            perdeu = True
        x_cobra += x_mudanca
        y_cobra += y_mudanca

        # Preenche a tela de fundo
        tela.fill(preto)

        # Desenha a comida
        pygame.draw.rect(tela, vermelho, [x_comida, y_comida, tamanho_celula, tamanho_celula])

        # Atualiza o corpo da cobra
        cabeca_cobra = [x_cobra, y_cobra]
        lista_cobra.append(cabeca_cobra)

        # Remove a cauda da cobra, a menos que ela tenha comido comida
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifique se a cobra colidiu consigo mesma
        if cabeca_cobra in lista_cobra[:-1]:
            perdeu = False

        # Desenha a cobra e a pontuação
        cobra(tamanho_celula, lista_cobra)
        pontuação(comprimento_cobra - 1)

        # Atualiza a tela
        pygame.display.update()

        # Cobra come a comida 
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0) * 10.0
            y_comida = round(random.randrange(0, altura_tela - tamanho_celula) / 10.0) * 10.0
            comprimento_cobra += 1

        # Controle a velocidade do jogo
        clock.tick(velocidade)

    # Sai do jogo
    pygame.quit()
    quit()

# Inicia o jogo
jogo()