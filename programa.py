from funcoes import *

frota = { "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [] }

lista_navios = [("porta-aviões", 4), ("navio-tanque", 3), ("contratorpedeiro", 2), ("submarino", 1)]

for nome, tamanho in lista_navios:
    while True:
        linha = int(input("Digite a linha desejada: "))
        coluna = int(input("Digite a coluna desejada: "))
        if nome == "submarino":
            orientacao = None
        else:
            orientacao = 'vertical'