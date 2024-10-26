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
