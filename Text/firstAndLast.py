n = str(input('Enter with your full name: ')).strip()
name = n.split()

print('Nice too meet you {}!'.format(n))
print('Your first name is {}'.format(name[0]))
print('Your Last name is {}'.format(name[len(name)-1]))