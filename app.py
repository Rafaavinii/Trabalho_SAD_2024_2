import streamlit as st
import pandas as pd
from graficos import grafico, grafico_colunas


df = pd.read_csv('cert_2010-2019.csv', sep=';')

df_2019 = df[df['Ano'] == 2019]
df_2018 = df[df['Ano'] == 2018]

total_incidentes_2019 = df_2019[['Worm', 'Invasao', 'DOS', 'Outros', 'Scan', 'Web', 'Fraude']].sum()
total_incidentes_2018 = df_2018[['Worm', 'Invasao', 'DOS', 'Outros', 'Scan', 'Web', 'Fraude']].sum()

anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
incidentes = [100, 120, 150, 130, 170, 200, 220, 180, 160, 210]

st.markdown ("# Incidentes de Segurança da Informação no Brasil (2010-2019)")

st.markdown ("## Gráficos de Pizza")
grafico(total_incidentes_2019, '2019')
grafico(total_incidentes_2018, '2018')

st.markdown ("## Gráficos de Colunas")
grafico_colunas(anos, incidentes)
