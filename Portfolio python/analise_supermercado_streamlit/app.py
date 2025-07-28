import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial da página
st.set_page_config(layout="wide", page_title="Dashboard")

# Função para carregar dados
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath, sep=";", decimal=",")
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].apply(lambda x: f"{x.month}/{x.year}")
    return df

# Carregar os dados
df = load_data("vendas.csv")

# Título do Dashboard
st.title(":bar_chart: Dashboard - Vendas")

# Sidebar - Filtros
st.sidebar.header("Filtros")
mes_selecionado = st.sidebar.selectbox("Selecione o mês", df["Mes"].unique())
ramo_selecionado = st.sidebar.multiselect(
    "Selecione os canais de venda", df["Ramo"].unique(), default=df["Ramo"].unique()
    )

# Filtrar os dados
df_filtrado = df[(df["Mes"] == mes_selecionado) & (df["Ramo"].isin(ramo_selecionado))]

# Gráficos
st.subheader(f"Dados Filtrados para {mes_selecionado}")

# Gráfico 1: Faturamento por Cidade
fig_cidade = px.bar(
    df_filtrado.groupby("Cidade")[["Total"]].sum().reset_index(),
    x="Cidade",
    y="Total",
    title="Faturamento por Cidade",
    labels={"Total": "Faturamento (R$)", "Cidade": "Filial"},
)
st.plotly_chart(fig_cidade, use_container_width=True)

# Gráfico 2: Faturamento por Forma de Pagamento
fig_pagamento = px.pie(
    df_filtrado,
    values="Total",
    names="Forma de pagamento",
    title="Faturamento por Forma de Pagamento",
)
st.plotly_chart(fig_pagamento, use_container_width=True)

