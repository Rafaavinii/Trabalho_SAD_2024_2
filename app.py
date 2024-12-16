import streamlit as st
import pandas as pd
from graficos import grafico

df = pd.read_csv('cert_2010-2019.csv', sep=';')

df_2019 = df[df['Ano'] == 2019]
df_2018 = df[df['Ano'] == 2018]

total_incidentes_2019 = df_2019[['Worm', 'Invasao', 'DOS', 'Outros', 'Scan', 'Web', 'Fraude']].sum()
total_incidentes_2018 = df_2018[['Worm', 'Invasao', 'DOS', 'Outros', 'Scan', 'Web', 'Fraude']].sum()

st.markdown ("# Gráficos de Pizza")
grafico(total_incidentes_2019, '2019')
grafico(total_incidentes_2018, '2018')
