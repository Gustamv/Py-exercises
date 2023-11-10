#le os km rodados, os dias alugados e imprime o valor a ser pago pelo aluguel

d = int(input('Dias alugados: '))
km = int(input('km rodados: '))
total = d*60 + 0.15*km
print(f'Valor toal a pagar: R${total:.2f}')
