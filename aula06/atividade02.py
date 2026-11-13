numero = float (input('valor do numero: '))

dobro = numero * 2
triplo = numero * 3 
quadrado = numero ** 2

print(f'dobro: {dobro:.2f}')
print(f'triplo: {triplo:.2f}')
print(f'quadrado: {quadrado:.2f}')

opcao = int(input(' informe a opcao escolhida: '))

match opcao:
    case 1:
        print('dobro')
        resultado = numero * 2

    case 2:
        print('triplo')
        resultado = numero * 3

    case 3:
        print('quadrado')
        resultado = numero ** 2


if opcao in [1, 2, 3]:
    print(f'\nresultado: {resultado}')

    valor_final = numero - resultado
    print(f'\nvalor final: {valor_final:.2f}')