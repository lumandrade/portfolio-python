import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial da página
st.set_page_config(layout="wide", page_title="Dashboard Simplificado")

# Função para carregar dados com cache
@st.cache_data
def load_data(filepath):
    # Lê o CSV com separador correto e decimal brasileiro
    df = pd.read_csv(filepath, sep=";", decimal=",")

    # Verificação: garantir que a coluna 'Data' exista
    if "Data" not in df.columns:
        st.error("Coluna 'Data' não encontrada no arquivo CSV.")
        st.stop()

    # Conversão de datas (assumindo formato brasileiro DD/MM/AAAA)
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True, errors="coerce")

    # Remover linhas onde a data não foi interpretada corretamente
    df = df.dropna(subset=["Data"])

    # Criar coluna Mês com formato MM/AAAA
    df["Mes"] = df["Data"].dt.strftime("%m/%Y")

    return df

# Carregar os dados
df = load_data(r"Z:\Luma Andrade\Python\Visu_Dados\vendas_supermercado.csv")

# Título do Dashboard
st.title(":bar_chart: Dashboard - Vendas")

# Sidebar - Filtros
st.sidebar.header("Filtros")
meses_disponiveis = df["Mes"].unique()
mes_selecionado = st.sidebar.selectbox("Selecione o mês", sorted(meses_disponiveis, reverse=True))

ramos_disponiveis = df["Ramo"].unique()
ramo_selecionado = st.sidebar.multiselect(
    "Selecione os canais de venda", ramos_disponiveis, default=list(ramos_disponiveis)
)

# Filtrar os dados
df_filtrado = df[(df["Mes"] == mes_selecionado) & (df["Ramo"].isin(ramo_selecionado))]

# Título de seção com filtro aplicado
st.subheader(f"Dados Filtrados para: {mes_selecionado}")

# Exemplo de gráfico (pode ser ajustado conforme sua necessidade)
if not df_filtrado.empty:
    grafico_vendas = px.bar(
        df_filtrado,
        x="Linha de produtos",
        y="Total",
        color="Ramo",
        title="Total de Vendas por Linha de Produto",
        labels={"Total": "Valor Total (R$)", "Linha de produtos": "Produto"},
        template="plotly_white"
    )
    st.plotly_chart(grafico_vendas, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")


# Gráfico1: Faturamento por cidade
fig_cidade = px.bar(
    df_filtrado.groupby("Cidade")[["Total"]].sum().reset_index(),
    x="Cidade",
    y="Total",
    title="Faturamento por Cidade",
    labels= {"Total": "Faturamento (R$)", "Cidade": "Filial"},
)
st.plotly_chart(fig_cidade, use_container_width=True)

# Gráfico 2: Faturamento por forma de pagamento
fig_pagamento = px.pie(
    df_filtrado,
    values="Total",
    names="Forma de pagamento",
    title="Faturamento por forma de pagamento",
)
st.plotly_chart(fig_pagamento, use_container_width=True)