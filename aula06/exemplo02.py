valor = float (input('valor da venda: '))

print('''
[1] - pix (12% de desconto)
[2] - debito (8% de desconto)
[3] - credito (5% de desconto)
[4] - dinheiro (15% de desconto)

''')

operacao = True
desconto = 0 
opcao = int(input(' informe a opcao escolhida: '))

match opcao:
    case 1:
        print('pix')
        desconto = valor * 0.12

    case 2:
        print('debito')
        desconto = valor * 0.08

    case 3:
        print('credito')
        desconto = valor * 0.05

    case 4:
        print('dinheiro')
        desconto = valor * 0.15

    case _: 
        operacao = False
        print('opcao invalida')

if opcao in [1, 2, 3, 4]:
# if operacao: == True:      
# if desconto != 0:
    valor_final = valor - desconto
    print(f'\npreco: {valor:.2f}')
    print(f'valor final: {valor_final:.2f}')
    print(f'desconto: {desconto:.2f}')

else:
    print('escolha uma opcao valida')