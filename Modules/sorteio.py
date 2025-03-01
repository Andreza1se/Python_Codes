#temos que sortear um tipo de chocolate e usar lista 
import random

print('Olá vamos sortear um chocolate. Digite o seu favorito!')

n1 = str(input(' Nome :'))
n2 = str(input(' Nome :'))
n3 = str(input(' Nome :'))
n4 = str(input(' Nome :'))

lista = [ n1, n2, n3, n4]

sorteio = random.choice(lista)

print('O chocolate escolhido foi {}'.format(sorteio))