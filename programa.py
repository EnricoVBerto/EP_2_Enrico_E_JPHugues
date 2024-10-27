from funcoes import *

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
                orientacao1=int(input('Qual orientação deseja?')) 
                if orientacao1==1:
                    orientacao='vertical'
                if orientacao==2:
                    orientacao='horizontal'