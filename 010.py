#conversor de dolar para real levando em consideracao que o 1 USD = 3,27 R$

real = float(input('Digite a quanditide de reais (R$): '))
print(f'Com R${real} voce pode comprar US${real * 3.27:.2f}')
