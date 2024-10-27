def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao=[]
    i=0
    while i!=tamanho:
        if orientacao=='vertical':
            posicao.append([linha+i,coluna])
        if orientacao=='horizontal':
            posicao.append([linha,coluna+i])
        i+=1
    return posicao


def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    posicoes_novas = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_do_navio in frota:
        frota[nome_do_navio].append(posicoes_novas)
    else:
        frota[nome_do_navio] = [posicoes_novas]

    return frota

def faz_jogada(tabuleiro,linha,coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota(frota):
    tabuleiro= []
    for i in range(10):
        tabuleiro[i]=[0]*10
    for posicoes in frota.values():
        for posicao_navio in posicoes:
            for x, y in posicao_navio:
                tabuleiro[x][y] = 1
    return tabuleiro

