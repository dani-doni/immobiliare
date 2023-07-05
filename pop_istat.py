import streamlit as st
import pandas as pd
# libraries imported

url_CL_ITTER107 = 'https://raw.githubusercontent.com/ondata/guida-api-istat/master/processing/DCIS_POPRES1/3_Dimension_CL_ITTER107.csv'
CL_ITTER107 = pd.read_csv(url_CL_ITTER107)
# take data of ITTER107 and read it as csv

chosen_ITTER107 = st.selectbox('Comune', options=list(CL_ITTER107['dimensionValueDescription']))
#choose a ITTER107 from streamlit frontend

print ("hai scelto il comune:" + chosen_ITTER107 )