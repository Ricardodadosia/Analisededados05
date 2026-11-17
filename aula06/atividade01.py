
for venda in range(5):
    valor = float(input('valor da venda: '))

    if valor >= 200 :
        desconto = valor * 0.10

    else: desconto = 0

    valor_final = valor - desconto 

    print(f'desconto de R$ {desconto:.2f}')
    print(f'valor final de R$ {valor_final:.2f}')  