#le a altura e a largura para calcular a area e imprimir a quantidade de latas de tinta necessarias

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print(f'Sua parede tem dimensao {largura}x{altura} e sua area é {area}m². \n'
      f'Para pintar essa parede, serão necessarios {area/2}l de tinta')