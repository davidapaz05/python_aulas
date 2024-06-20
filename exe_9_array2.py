'''
autor: Davi Paz
Data: 17/06/2024
versão: 1.0
descrição: estudo do tipo de dado array(vetor)
'''
carros = ['vw']

carros.append('gm') #adiciona na ultima posição o valor indicado
carros.append('ford')
carros.append('fiat')
carros.append('renault')

print(carros)

carros.remove('ford')#remove item indicando o valor
print(carros)

carros.pop(3)#remove item indicando o index
print(carros)

print(len(carros))#tamanho do vetor atual
carros.pop(len(carros) - 1) #deleta sempre a ultima
print(carros)
carros.pop(len(carros) - 1) 
carros.pop(len(carros) - 1) 
print(carros)
