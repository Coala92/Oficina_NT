from pathlib import Path
from PIL import Image

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title='Sistema MAV')


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.sidebar.markdown('Desemvolvido por SI-Norte tech', unsafe_allow_html=True)

st.markdown('# Sistema MAV - Controle & Gestão de Oficina Mecânica')

st.divider()

st.markdown(
    '''
    Bem-vindo ao Sistema MAV.
    '''
)