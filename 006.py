#proigrama que le um numero e imprime o seu dobro, triplo e sua raiz quadrada

n = int(input('Digite um numero: '))
print(' O dobro de {} vale {}'.format(n, n * 2))
print(' O triplo de {} vale {}'.format(n, n * 3))
print(' a raiz quadrada de {} vale {}'.format(n, pow(n, 1/2)))