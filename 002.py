#programa que captura o nome digitado e imprime uma mensagem de bem vindo

nome = input('Digite seu nome: ')
#print('Bem vindo,',nome)
print('Bem vindo, {}'.format(nome))