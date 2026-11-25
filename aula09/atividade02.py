def dobro(x):
    r = x * 2
    return r

def triplo(x):    
    r = x * 3
    return r

def quadrado(x):    
    r = x * x
    return r

numero = int(input('Informe o numero: '))
resultado1 = dobro (numero)
resultado2 = triplo (numero)
resultado3 = quadrado (numero)
print(f'O Dobro é: {resultado1}')
print(f'O Triplo é: {resultado2}')
print(f'O Quadrado é: {resultado3}')
