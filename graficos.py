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
    
def grafico_linhas(df_ano, tipos_incidentes):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    # Ordenar o DataFrame pelos meses 
    df_ano = df_ano.copy()
    df_ano['Mes'] = pd.Categorical(df_ano['Mes'], categories=meses, ordered=True)
    df_ano = df_ano.sort_values('Mes')
    
    plt.figure(figsize=(15, 8))
    
    # Plotar cada tipo de incidente
    for incidente in tipos_incidentes:
        if incidente in df_ano.columns:
            plt.plot(df_ano['Mes'], df_ano[incidente], 
                    marker='o', 
                    linewidth=2, 
                    markersize=8, 
                    label=incidente)
    
    plt.title('Distribuição de Incidentes de Segurança por Mês (2019)', 
             fontsize=16, pad=20)
    plt.xlabel('Mês', fontsize=12, labelpad=10)
    plt.ylabel('Quantidade de Incidentes', fontsize=12, labelpad=10)
    
    plt.xticks(rotation=45, ha='right')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Legenda do gráfico
    plt.legend(bbox_to_anchor=(1.05, 1), 
              loc='upper left', 
              title='Tipos de Incidentes',
              title_fontsize=12)
    
    plt.tight_layout()
    
    st.pyplot(plt)