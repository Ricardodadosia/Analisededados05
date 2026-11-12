
valor = float(input('valor do ingresso: '))

print('''
[1] - Inteira (sem desconto)
[2] - meia entrada (50% de desconto)
[3] - promoção (30% de desconto)

''')

desconto = 0 
opcao = int(input(' informe a opcao escolhida: '))

match opcao:
    case 1:
        print('Inteira')
        desconto = 0

    case 2:
        print('Meia entrada')
        desconto = valor * 0.50

    case 3:
        print('Promoção')
        desconto = valor * 0.30

    case _:
        print('opcao invalida')

if opcao in [1, 2, 3,]:
    valor_final = valor - desconto
    print(f'\npreco: {valor:.2f}')
    print(f'valor final: {valor_final:.2f}')
    print(f'desconto: {desconto:.2f}')

else:
    print('escolha uma opcao valida')
        