class Pessoa:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Documento: {self.documento}")

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.cpf = cpf

    def exibir_informacoes(self):
        print("Pessoa física:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome, cnpj)
        self.cnpj = cnpj

    def exibir_informacoes(self):
        print("Pessoa jurídica:")
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")

pf = PessoaFisica("Maria da Silva", "123.456.789-00")
pf.exibir_informacoes()