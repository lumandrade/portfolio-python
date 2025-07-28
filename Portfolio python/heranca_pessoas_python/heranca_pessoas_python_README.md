# Herança em Python - Pessoa, Pessoa Física e Jurídica

Exemplo de herança com uma classe base `Pessoa` e duas subclasses `PessoaFisica` e `PessoaJuridica`. Cada uma exibe informações específicas.

## Funcionalidades
- Classe base com atributos comuns
- Subclasses com atributos e métodos específicos
- Uso de `super()`

## Exemplo de uso
```python
pf = PessoaFisica("Maria da Silva", "123.456.789-00")
pf.exibir_informacoes()
```