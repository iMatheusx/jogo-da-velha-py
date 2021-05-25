from termcolor import cprint, colored
from random import randint

u = " "

def pedir_nome(id):
    return input(colored(f'Informe o nome do jogador {id}: ', 'yellow'))


def criar_jogador(id):
    nome = pedir_nome(id)
    return {
        'id': id,
        'nome': nome,
        'pontos': 0,
        'vez': False,
        'token': None
    }


def criar_jogadores():
    cprint('=-' * 75, 'blue')
    player1 = criar_jogador(1)
    cprint('=-' * 75, 'blue')
    player2 = criar_jogador(2)
    cprint('=-' * 75, 'blue')
    return player1, player2


def criartabuleiro():
    tabuleiro = [
        [u, u, u],
        [u, u, u],
        [u, u, u],
    ]
    return tabuleiro


def sortear_vez(player1, player2):
    players = player1, player2
    numero_vez = randint(0,1)
    players[numero_vez]['vez'] = True
    if player1.get('vez'):
        cprint(f'{player1.get("nome")} começa!', 'green')
    else:
        cprint(f'{player2.get("nome")} começa!', 'green')
    return players


def trocar_vez(player1, player2):
    if player1['vez']:
        player2['vez'] = True
        player1['vez'] = False
    else:
        player2['vez'] = False
        player1['vez'] = True


def mostrar_tabuleiro(tabuleiro):
    for i in range(3):
        cprint(("  |  ".join(tabuleiro[i])), 'yellow')
        if (i < 2):
            cprint("-------------", 'red')


def pedir_jogada(texto):
    try:
        n = int(input(texto))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("O número informado precisa estar entre 1 e 3")
            return pedir_jogada(texto)
    except:
        print("Valor informado não é válido")
        return pedir_jogada(texto)


def validacao_da_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == u:
        return True
    else:
        return False

def posicionar_token_no_tabuleiro(tabuleiro, linha, coluna, jogadores):
    for jogador in jogadores:
        if jogador['vez']:
            tabuleiro[linha][coluna] = jogador['token']




def verificar_vitória(tabuleiro, player1, player2):

    # linhas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == 'X'):
            player1['pontos'] += 1
            return tabuleiro[i][0]

    # coluna
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == 'X'):
            player1['pontos'] += 1
            return tabuleiro[0][i]


    # diagonal principal
    if (tabuleiro[0][0] == 'X' and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        player1['pontos'] += 1
        return tabuleiro[0][0]

    # diagonal secundaria
    if (tabuleiro[0][2] == 'X' and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        player1['pontos'] += 1
        return tabuleiro[0][2]

    #Jogador 2

    # linhas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == 'O'):
            player2['pontos'] += 1
            return tabuleiro[i][0]


    # coluna
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == 'O'):
            player2['pontos'] += 1
            return tabuleiro[0][i]


    # diagonal principal
    if (tabuleiro[0][0] == 'O' and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        player2['pontos'] += 1
        return tabuleiro[0][0]

    # diagonal secundaria
    if (tabuleiro[0][2] == 'O' and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        player2['pontos'] += 1
        return tabuleiro[0][2]


    for i in range(3):
        for j in range(3):
            if (tabuleiro[i][j] == u):
                return False

    return "EMPATE"

def mostrar_vez(player1, player2):
    if player1.get('vez'):
        cprint(f'Vez de {player1.get("nome")}', 'green')
    else:
        cprint(f'Vez de {player2.get("nome")}', 'green')

player1 = None
player2 = None

def anunciar_vencedor(player1, player2):
    if player1['pontos'] != 0:
        cprint('=-' * 75, 'blue')
        cprint(f'{player1["nome"]} VENCEU!', 'green')
        cprint('=-' * 75, 'blue')
    if player2['pontos'] != 0:
        cprint('=-' * 75, 'blue')
        cprint(f'{player2["nome"]} VENCEU!', 'green')
        cprint('=-' * 75, 'blue')
    if player2['pontos'] == 0 and player1['pontos'] == 0:
        cprint('=-' * 75, 'blue')
        cprint('DEU EMPATE!')
        cprint('=-' * 75, 'blue')
def rodar_game():
    tabuleiro = criartabuleiro()
    player1, player2 = criar_jogadores()
    player1['token'] = "X"
    player2['token'] = "O"
    verificar_vitória(tabuleiro, player1, player2)
    sortear_vez(player1, player2)
    while not verificar_vitória(tabuleiro, player1, player2):
        mostrar_tabuleiro(tabuleiro)
        mostrar_vez(player1, player2)
        linha = pedir_jogada('Informe o valor da linha: ')
        coluna = pedir_jogada('Informe o valor da coluna: ')
        if validacao_da_jogada(tabuleiro, linha, coluna):
            posicionar_token_no_tabuleiro(tabuleiro, linha, coluna, (player1, player2))
            trocar_vez(player1, player2)
    anunciar_vencedor(player1, player2)
    mostrar_tabuleiro(tabuleiro)

rodar_game()




