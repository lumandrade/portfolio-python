def pedir_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"Você digitou o número {numero}")
            break
        except ValueError:
            print("Erro: você deve digitar um número inteiro. Tente novamente.")
        finally:
            print("Tentativa concluída.\n")
    print("Processo finalizado.")

pedir_numero()