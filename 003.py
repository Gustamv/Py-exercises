#programa que le 2 valores e imprime a soma

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma = valor1 + valor2
#print('A soma de', valor1,'+', valor2,'é igual a ', soma)

#utilizando print formatado
print('A soma entre {} e {} é igual a {}'.format(valor1, valor2, soma))