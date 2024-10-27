from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

frota = { "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [] }

lista_navios = [("porta-aviões", 4, 1), ("navio-tanque", 3, 2), ("contratorpedeiro", 2, 3), ("submarino", 1, 4)]

for nome, tamanho, quantidade in lista_navios:
    for i in range(quantidade):
        while True:
            linha = int(input("Digite a linha desejada: "))
            coluna = int(input("Digite a coluna desejada: "))
            if nome == "submarino":
                orientacao = None
            else:
                orientacao1=int(input('Qual orientação deseja? ===> Vertical (1) , Horizontal (2)')) 
                if orientacao1==1:
                    orientacao='vertical'
                if orientacao==2:
                    orientacao='horizontal'
            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if valida == True:
                posicao_do_navio = define_posicoes(linha, coluna, orientacao, tamanho)
                preenche_frota(frota, nome, posicao_do_navio)
                break
            else:
                print("Esta posição não está válida!")
    print(frota)
    