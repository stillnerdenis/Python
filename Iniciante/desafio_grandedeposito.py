valor = float(input())


if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    mensagem = (f"""Deposito realizado com sucesso!\nSaldo atual: R$ {valor:.2f}""" )
elif valor == 0:
    mensagem = ("Encerrar programa...")
else:  
    mensagem = ("Valor invalido! Digite um valor maior que zero.")

print (mensagem)