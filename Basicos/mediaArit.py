#Media aritimetica

n = float(input('Digite a primeira nota : '))
m = float(input('Digite a segunda nota: '))

s = (n+m)/2

if(s < 5):
    print('Sua média é {:.1f} ! Você está Reprovado'.format(s))
else:
    print('Parabens sua média é {:.1f} você está aprovado!'.format(s))