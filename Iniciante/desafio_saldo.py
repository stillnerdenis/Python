saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

def calcula_saldo(saldo, deposito, saque):
    novo_saldo = (saldo + deposito) - saque
    return novo_saldo


#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
saldo_atualizado = calcula_saldo(saldo_atual,valor_deposito,valor_retirada)
print(f"Saldo atualizado na conta: {saldo_atualizado}")

