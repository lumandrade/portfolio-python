def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(soma_numeros(1, 2, 3))