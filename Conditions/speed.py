speed = float(input('Speed: '))

if speed > 80:
    print('Fined ! You are over the allowed speed')
    fined = speed*7
    print('You have to pay a fine of U$ {:.2f}'.format(fined))
else:
    print('Have a great day!')