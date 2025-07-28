#lista de classificacoes
classificacao = ["SUSPEITO","CÚMPLICE","ASSASSINO", "INOCENTE"]
print("classificacões:", classificacao)
#lista de perguntas
perguntas = [
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
    "Telefonou para a vítima?"
]
#entrada do nome
nome = input("Digite seu nome completo:")
print("Digite 1 para SIM e 2 para NÃO:")

#contador de respostas SIM
respostas_sim = 0

#fazendo as perguntas
for pergunta in perguntas:
    while True:
        resposta = input(pergunta+"").strip()
        if resposta =="1":
            break
            respostas_sim += 1
        elif resposta =="2":            
             break
        else:
                print("Resposta inválida! Digite 1 para SIM ou 2 para NÃO:")

#classificação com base no número
if respostas_sim == 2:
    print(f"{nome} é {classificacao[0]}.")
elif respostas_sim == 3 or respostas_sim == 4:
    print(f"{nome} é {classificacao[1]}.")
elif respostas_sim == 5:
    print(f"{nome} é {classificacao[2]}.")
else:
    print(f"{nome} é {classificacao[3]}.")