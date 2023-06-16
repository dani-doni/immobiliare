import streamlit as st
import pandas as pd
# libraries imported

url_data_imm = 'https://raw.githubusercontent.com/dani-doni/immobiliare/main/Foglio%20per%20generare%20csv%20-%20Brescia.csv'
data_imm = pd.read_csv(url_data_imm)
# get data about country and dataset in Pandas Dataframe

st.title("STATISTICHE IMMOBILIARI PROVINCIA DI BRESCIA")
st.header("Seleziona una paese per visualizzare un riepilogo dei dati")
comune = st.selectbox('PAESE', options=list(data_imm['nome_comune']))
data_imm_comune = data_imm[data_imm['nome_comune'] == comune]
# select the country

st.write(f"Abitanti 2022: {data_imm_comune['POP_TOT_2022'].values[0]}")
st.write(f"Variazione abitanti 2001-2011: {data_imm_comune['var_POP_TOT_2001_2011'].values[0]}")
st.write(f"Variazione abitanti 2011-2022: {data_imm_comune['var_POP_TOT_2011_2022'].values[0]}")
st.write(f"Valore medio al m2: {data_imm_comune['Max di 2021_1_Compr_media'].values[0]}")
st.write(f"Numero transazioni ogni 1000 abitanti: {data_imm_comune['TRS_IMM/TOT_POP*1000'].values[0]}")
st.write(f"Totale transazioni 2011-2021: {data_imm_comune['CUM_2011_2021_TOT_TRS_IMM'].values[0]}")
# write the main country data
