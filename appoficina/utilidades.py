from pathlib import Path
from openpyxl import Workbook

import streamlit as st
import pandas as pd

def leitura_dados():
    if not 'dados' in st.session_state:
        dataset_oficina = Path(__file__).parents[1] / 'dataset_oficina'
        df_ofi_inicio = pd.read_excel(dataset_oficina / 'base_oficina_inicio.xlsx', decimal=',', index_col=0,  parse_dates=True)
        df_ofi_fim = pd.read_excel(dataset_oficina / 'base_oficina_fim.xlsx', decimal=',', index_col=0,  parse_dates=True)
        dados = {'df_ofi_inicio': df_ofi_inicio,
                 'df_ofi_fim': df_ofi_fim,}
        st.session_state['caminho_datasets'] = dataset_oficina
        st.session_state['dados'] = dados