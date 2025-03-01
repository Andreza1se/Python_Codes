#Quantos litros de tinta serão precisos para pintar a parede

l = float(input('Informe a largura em metros: '))
a = float(input('Informa a altura em metros: '))

area = l * a
tinta = area/2

print('Para pintar a parede vai ser necessario {}L de tinta.'.format(tinta))