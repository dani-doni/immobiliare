import streamlit as st
import pandas as pd
import requests
from time import sleep
# libraries imported

def fetch(session, url):
    try:
        result = session.get(url)
        time.sleep(5.0)
        return result.json()
        time.sleep(5.0)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

session = requests.Session()
# def function to get API data

url_CL_ITTER107 = 'https://raw.githubusercontent.com/ondata/guida-api-istat/master/processing/DCIS_POPRES1/3_Dimension_CL_ITTER107.csv'
CL_ITTER107 = pd.read_csv(url_CL_ITTER107)
# take data of ITTER107 and read it as csv

with st.form("my_form"):
    chosen_ITTER107 = st.selectbox('Comune', options=list(CL_ITTER107['dimensionValueDescription']))
    id_ITTER107 = CL_ITTER107.loc[CL_ITTER107 ['dimensionValueDescription'] == chosen_ITTER107,'dimensionValueID'].iloc[0]
    submitted = st.form_submit_button("Submit")
#choose a ITTER107 from streamlit frontend and take the ID

FREQ = "A"
ETA = "TOTAL"
ITTER107 = id_ITTER107
SESSO = 9
STACIVX = 99
TIPO_INDDEM = "JAN"
#declare API varibles

api_url = "https://sdmx.istat.it/SDMXWS/rest/data/22_289/{}.{}.{}.{}.{}.{}/"
url = api_url.format (FREQ,ETA,ITTER107,SESSO,STACIVX,TIPO_INDDEM)
st.write(url)

if submitted:
    data = fetch(session, url)
    if data:
        st.write("ok")
    else:
        st.error("Error")
      
