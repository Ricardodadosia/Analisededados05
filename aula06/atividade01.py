for i in range(5):
    print(f'\n:{i + 4}:(vendas:'))
    valor_venda = float(input('digite o valor da venda: '))
     
if valor_venda < 200:
    print('valor da venda sem desconto')
    print(f'valor da {i + 1}: {valor_venda:.2f}')
    somatorio_vendas = valor_venda

else:    
    print('valor da venda com desconto')
    print(f'valor da {i + 1}: {valor_venda:.2f}')
    somatorio_vendas = valor_venda * 10
    