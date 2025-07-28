produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco = float(input("Digite o preço do produto: "))
total = quantidade * preco

print("-------------------------------")
print("--------Lista de compra--------")
print("-------------------------------")
print("Produto:--------->", produto)
print("Quantidade:------>", quantidade)
print("Preço unitário:-->", preco)
print("Total:----------->", total)
print("-------------------------------")