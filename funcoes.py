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
    tabuleiro=[[0] * 10 for _ in range(10)]
    for posicoes in frota.values():
        for posicao_navio in posicoes:
            for x, y in posicao_navio:
                tabuleiro[x][y] = 1
    return tabuleiro


def afundados(frota,tabuleiro):
    total=0
    for posicoes in frota.values():
        for posicao_navio in posicoes:
            navio_afundado = True
            for x, y in posicao_navio:
                if tabuleiro[x][y] != 'X':
                    navio_afundado = False
                    break
            if navio_afundado:
                total += 1
    return total

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes_navio=define_posicoes(linha,coluna,orientacao,tamanho)
    for x, y in posicoes_navio:
        if x < 0 or x >= 10 or y < 0 or y >= 10:
            return False
    for posicoes in frota.values():
        for posicao_navio in posicoes:
            for posicao in posicao_navio:
                if posicao in posicoes_navio:
                    return False
    return True