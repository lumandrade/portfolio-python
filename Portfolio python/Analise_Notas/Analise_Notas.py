#criando lista vazia
notas = []
n1 = float(input("Adicione a 1ª nota:"))
n2 = float(input("Adicione a 2ª nota:"))
n3 = float(input("Adicione a 3ª nota:"))

#colocando uma por uma no final da lista
notas.append(n1)
notas.append(n2)
notas.append(n3)

#imprimindo todas as notas citadas
print("Notas", notas)

#maior nota
maior_nota = max(notas)
print("A maior nota é:", maior_nota)

#menor nota
menor_nota = min(notas)
print("A menor nota é:", menor_nota)

#soma das notas
soma_notas = sum(notas)
print("A soma de todas as notas é:", soma_notas)

#media notas
media_notas = sum(notas)/ len(notas)
print("A média é:", media_notas)
