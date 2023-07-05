import streamlit as st
import pandas as pd
import requests
# libraries imported

url_CL_ITTER107 = 'https://raw.githubusercontent.com/ondata/guida-api-istat/master/processing/DCIS_POPRES1/3_Dimension_CL_ITTER107.csv'
CL_ITTER107 = pd.read_csv(url_CL_ITTER107)
# take data of ITTER107 and read it as csv

chosen_ITTER107 = st.selectbox('Comune', options=list(CL_ITTER107['dimensionValueDescription']))
id_ITTER107 = CL_ITTER107.loc[CL_ITTER107 ['dimensionValueDescription'] == chosen_ITTER107,'dimensionValueID'].iloc[0]
#choose a ITTER107 from streamlit frontend and take the ID

FREQ = "A"
ETA = "TOTAL"
ITTER107 = id_ITTER107
SESSO = 9
STACIVX = 99
TIPO_INDDEM = "JAN"
#declare API varibles

st.write(f"tutto bene")
st.write(FREQ)

api_url = "https://sdmx.istat.it/SDMXWS/rest/data/22_289/{}.{}.{}.{}.{}.{}/"
url = api_url.format (FREQ,ETA,ITTER107,SESSO,STACIVX,TIPO_INDDEM)
st.write(url)
response = requests.get(url)
st.write(response.text)
