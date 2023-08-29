# Condicionais, parte 2
# if, elif e else

'''
Eu chegue atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão
'''
numero_de_atrasos = 3
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém, caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, mas se tomar mais uma falta, será suspenso')
 # Codigo usado para se caso ele não tiver nenhuma falta
else:
    print('Pode entrar') 