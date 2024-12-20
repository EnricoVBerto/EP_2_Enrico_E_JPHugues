from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

frota = { "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [] }

lista_navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for nome, tamanho, quantidade in lista_navios:
    for i in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Escolha a linha que deseja: "))
            coluna = int(input("Escolha a coluna que deseja: "))

            if nome == "submarino":
                orientacao = None
            else:
                orientacao1 = int(input("[1] Vertical [2] Horizontal > "))
                if orientacao1==1:
                    orientacao='vertical'
                else:
                    orientacao='horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")

print(frota)

    