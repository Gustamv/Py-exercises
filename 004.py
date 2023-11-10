#testando algumas funcoes que retornam informacoes sobre o valor digitado

palavra = input('Digite algo: ')
print('O tipo primitivo do que foi digitado eh: ', type(palavra))
print('So tem espaços? ', palavra.isspace())
print('É um numero? ', palavra.isnumeric())
print('É alfabetico? ', palavra.isalpha())
print('É alfanumerico? ', palavra.isalnum())
print('Esta em maiusculas? ', palavra.isupper())
print('Esta em minusculas? ', palavra.islower())
print('Esta capitalizada? ', palavra.istitle())



