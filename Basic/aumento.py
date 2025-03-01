#Voce recebeu um aumento de 40% do seu salario

salario = float(input('Qual seu salário atual? '))

aumento = salario + (salario*40/100)

print('O seu novo salário é de R${}'.format(aumento))