import math

a = float(input('Digite o ângulo :'))

seno = math.sin(math.radians(a))

print('O angulo tem o seno de {:.2f}'.format(seno))

cos = math.cos(math.radians(a))

print('O angulo tem o cosseno de {:.2f}'.format(cos))

tan = math.tan(math.radians(a))

print('O angulo tem a tangente de {:.2f}'.format(tan))