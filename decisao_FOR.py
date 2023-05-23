tabuada = int(input('Descubra a tabuada do número: '))
print('Tabuada do número ', tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + 'X' + str(valor) + '=' + str((tabuada*valor)))
