#le um numero e imprime sua tabuada com um laço for

n = int(input('Digite um numero para ver sua tabuada: '))

for i in range(1, 11):
    tabuada = n * i
    #metodo mais simples de usar o print formatado
    print(f"{n} x {i} = {tabuada}")