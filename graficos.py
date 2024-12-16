import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def grafico(total_incidentes, ano):

    incidente_dado = pd.DataFrame({
        'Incidente': total_incidentes.index,
        'Quantidade': total_incidentes.values
    })
    # Criar o gráfico de pizza com Matplotlib
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(incidente_dado['Quantidade'], labels=incidente_dado['Incidente'], autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)

    # Adicionar título
    ax.set_title(f'Distribuição de Incidentes de Segurança - {ano}', fontsize=16)

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

def grafico_colunas(anos, incidentes):
    # Criar o DataFrame
    dados = pd.DataFrame({
        'Ano': anos,
        'Incidentes': incidentes
    })

    # Criar o gráfico de colunas
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dados['Ano'], dados['Incidentes'], color='skyblue', edgecolor='black')

    # Personalizar o gráfico
    ax.set_title('Quantidade de Incidentes por Ano (2010-2019)', fontsize=16)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Quantidade de Incidentes', fontsize=12)
    ax.set_xticks(dados['Ano'])
    ax.set_xticklabels(dados['Ano'], rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)