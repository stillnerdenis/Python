ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort() 

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
#print (ativos[0])
#print (ativos[1])
#print (ativos[0])

for elemento in ativos:
    print(elemento)
    