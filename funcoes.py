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

    if tabuleiro[linha] == 1 and tabuleiro[coluna] == 1:
        tabuleiro[linha] = 'X' and tabuleiro[coluna] = 'X'
    else:
        tabuleiro[linha] = '-' and tabuleiro[coluna] = '-'

    return tabuleiro