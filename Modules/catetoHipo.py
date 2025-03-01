#triangulo retangulo valor da hipotenusa
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente '))

hi = math.sqrt(co*co + ca*ca) #ele tem a propria funcao math.hypot que calcula a hipotenusa

print('O valor da sua hipotenusa é {:.2f}'.format(hi))