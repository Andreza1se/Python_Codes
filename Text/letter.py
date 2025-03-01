sentence = str(input('Enter a phrase: ')).upper()

print('The letter A appear {} times on phrase.'.format(sentence.count('A')))
print('The first letter A appear in position {}'.format(sentence.find('A')+1))
print('The last letter A appear in position {}'.format(sentence.rfind('A')+1))