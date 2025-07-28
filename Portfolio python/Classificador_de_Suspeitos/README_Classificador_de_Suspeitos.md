# Classificador de Suspeitos

Simula um sistema simples de investigação que faz 5 perguntas a uma pessoa e classifica seu nível de envolvimento com base nas respostas.

## Perguntas usadas

- Esteve no local do crime?
- Mora perto da vítima?
- Devia para a vítima?
- Já trabalhou com a vítima?
- Telefonou para a vítima?

## Classificação

- 2 respostas SIM → Suspeito
- 3 ou 4 respostas SIM → Cúmplice
- 5 respostas SIM → Assassino
- Menos de 2 → Inocente

## Exemplo

```
Digite seu nome completo: Maria
Digite 1 para SIM e 2 para NÃO:
...
Maria é Cúmplice
```