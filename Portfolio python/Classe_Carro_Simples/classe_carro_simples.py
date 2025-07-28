class Carro:
    def __init__(self, marca, modelo, ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def get_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Quilometragem: {self.km} km.")

    def atualizar_km(self, nova_km):
        if nova_km > self.km:
            self.km = nova_km
            print(f"Quilometragem atualizada para {self.km} km.")
        else:
            print("Erro: não é possível reduzir a quilometragem!")

    def ligar(self):
        print("O carro está ligado.")

    def desligar(self):
        print("O carro está desligado.")

meu_carro = Carro("Chevrolet", "Zafira", 2012, 0)
meu_carro.get_informacoes()