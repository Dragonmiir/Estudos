# Estudo sobre variáveis

#Tipos de dados que podem ser armazenados na memória do computador

#Números

velocidade_internet = 10
print(velocidade_internet)

Nota_filme = 8.5 #Exemplo de float

#valores boleanos

esta_aberto = True #False para se estiver fechado e true para estiver aberta, geralmente usado para os sistemas verificar se algo está disponível ou não por exemplo

#Strings

nome_do_curso = 'Lógica da programação' #Strings é usado quando você quer trabalhar com textos, podendo usar o '' para criar estes strings

#Como variáveis são usadas em programas reais?
#Problema 1 - Valor por hora
#Escreva um programa que retorna o valor por hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

'''
input salario_mensal
input horas_trabalhadas_por_mes
Valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
#os ''' podem ser usados para fazer com que a frase não seja interpretado pelo interpretador de código

salario_mensal = input('Qual é o seu salario mensal? ')
horas_trabalhadas_por_mes = input('Quantas horas você trabalha mensalmente? ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print (valor_hora)