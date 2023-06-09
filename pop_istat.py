import streamlit as st
import pandas as pd
import aiohttp
import asyncio

#import requests
#from requests.adapters import HTTPAdapter
#from urllib3.util.retry import Retry

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


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


asyncio.run(main())
       

      
