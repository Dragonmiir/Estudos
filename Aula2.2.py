# Condicionais, parte 3
# if, elif e else
# Encontre o maior entre 2 números

'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
    print o primeiro valor é maior
else
    print o segundo valor é maior
'''

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if int(primeiro_valor) > int(segundo_valor):
    print('Primeiro valor é maior que o segundo')
else:
    print('Segundo valor é maior que o primeiro')