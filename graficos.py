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