# Dashboard de Vendas Validado

Versão aprimorada do dashboard de vendas, com validações adicionais. Verifica se a coluna `Data` existe e trata problemas no formato das datas. Ideal para dados com formatação brasileira (decimal vírgula, data dia/mês/ano).

## Funcionalidades

- Verificação da existência da coluna `Data`
- Conversão segura de datas com tratamento de erros
- Filtros por mês e ramo
- Gráficos interativos

## Requisitos

- Python 3.x
- streamlit
- pandas
- plotly

## Executando

```bash
pip install streamlit pandas plotly
streamlit run app.py
```