import random
#vai colocar uma lista e sortear a ordem de quem vai 

n1 = str(input(' Nome :'))
n2 = str(input(' Nome :'))
n3 = str(input(' Nome :'))
n4 = str(input(' Nome :'))
n5 = str(input(' Nome :'))

lista = [n1,n2,n3,n4,n5]

random.shuffle(lista)

print(lista)