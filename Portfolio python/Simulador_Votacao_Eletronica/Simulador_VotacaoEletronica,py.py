#iniciando os contadores do zero
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

total_eleitores = int(input("Digite o número total de eleitores: "))

#repetir o voto para cada eleitor
for i in range(1, total_eleitores + 1):
    print(f"\nEleitor {i}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do seu candidato (1, 2 ou 3):"))
    
#registrar o voto
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else: print("Voto inválido! Seu voto não será contado.")

#mostrar resultado final
print("RESULTADO DA ELEIÇÃO:\n")
print(f"votos candidato 1: {votos_candidato1} votos.")
print(f"votos candidato 2: {votos_candidato2} votos.")
print(f"votos candidato 3: {votos_candidato3} votos.")