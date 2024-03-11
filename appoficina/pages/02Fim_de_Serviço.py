from pathlib import Path
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd

from utilidades import leitura_dados

leitura_dados()

df_ofi_inicio = st.session_state['dados']['df_ofi_inicio']
df_ofi_fim = st.session_state['dados']['df_ofi_fim']

nome_mecanico = list(df_ofi_fim['Mecanico'].unique())
nome_mecanico_selecionado = st.sidebar.selectbox('Selecionar Mecânico:', nome_mecanico)

tipo_de_servico = list(df_ofi_fim['Tipo de Servico'].unique())
tipo_de_servico_selecionado = st.sidebar.selectbox('Selecionar Tipo de Serviço:', tipo_de_servico)

tempo_estimado = list(df_ofi_fim['Tempo Estimado'].unique())
tempo_estimado_selecionado = st.sidebar.selectbox('Selecionar Tempo Estimado:', tempo_estimado)


iniciar_servico = st.sidebar.button('Finalizar Serviço')
if iniciar_servico:
    lista_adicionar = [df_ofi_fim['N° Serviço'].max() +1,
                       nome_mecanico_selecionado,
                       tipo_de_servico_selecionado,
                       tempo_estimado_selecionado,
                        ]
    hora_adicionar = datetime.now()
    df_ofi_fim.loc[hora_adicionar] = lista_adicionar
    caminho_datasets = st.session_state['caminho_datasets']
    df_ofi_fim.to_csv(caminho_datasets / 'df_ofi_fim.csv', decimal=',', sep=';')

st.dataframe(df_ofi_fim, hide_index=False, height=800)