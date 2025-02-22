# Você foi ao mercado e viu que os produtos estavam com 75% de desconto

preco = float(input('Preço do produto sem desconto :'))

d = preco - (preco*75/100)

print('O valor desconto é de R${}'.format(d))