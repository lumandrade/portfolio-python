def calcular_juros_compostos(p, r, t):
    montante = p * (1 + r) ** t
    return montante

p = float(input("Digite o valor inicial: "))
r = float(input("Digite a taxa de juros anual: "))
t = float(input("Digite o número de anos: "))

montante_total = calcular_juros_compostos(p, r, t)
print("O montante total é:", montante_total)