from random import randint
from time import sleep

game = randint(0,5)
print('¨¨'*25)
print('I will think of a number from 0 to 5')
print('\n')
print('¨¨'*25)
player = int(input('What a number did i think ? '))
sleep(3)
print('¨¨'*25)
if player == game:
    print('Congratulations, you got it!')
else:
    print('You fail! I think in {}'.format(game))  