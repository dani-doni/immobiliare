pip install -r requirements.txt
import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import st_folium
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

url_coord_com = 'https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/coordinate.csv'
data_coord_com = pd.read_csv(url_coord_com)
data_imm = pd.merge (
    left=data_imm,
    right=data_coord_com,
    left_on='cod_istat',
    right_on='pro_com_t',
    how='left'
)
# add coordinates to data_imm Dataframe

url_comuni = 'https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_P_17_municipalities.geojson'
# get GeoJson

m = folium.Map(location=(45.541553, 10.211802), zoom_start=10, tiles="mappa immobiliare", attr="cose mie")
# create the map called m


folium.Choropleth(
    geo_data=url_comuni,
    data=data_imm,
    columns=["cod_cat","Max di var_VAL_IMM_2016_2022"],
    key_on="feature.properties.com_catasto_code",
    bins=100,
    fill_color="YlGnBu",
    fill_opacity=0.2,
    line_opacity=0.5,
    nan_fill_color="white",
    legend_name="A",
    name="A"
).add_to(m)
# create the colored layer A and add to map m

folium.Choropleth(
    geo_data=url_comuni,
    data=data_imm,
    columns=["cod_cat","Log1000norm_com_imm_pop"],
    key_on="feature.properties.com_catasto_code",
    bins=100,
    fill_color="YlGnBu",
    fill_opacity=0.2,
    line_opacity=0.5,
    nan_fill_color="white",
    legend_name="B",
    name="B"
).add_to(m)
folium.LayerControl().add_to(m)
# create the colored layer A and add to map m


for i in range(0,len(data_imm)):
    html=f"""
        <h1> {data_imm.iloc[i]['nome_comune']}</h1>
        <p>lista valori:</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
        </p>
        <p>And that's a <a href="https://www.python-graph-gallery.com">link</a></p>
        """     
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=1650)
    folium.Marker(
      location=[data_imm.iloc[i]['lat'], data_imm.iloc[i]['long']],
        popup=popup,
        icon=folium.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{data_imm.iloc[i]['nome_comune']}</div>""")
        
   ).add_to(m)
# add marker one by one on the map

plugins.Geocoder().add_to(m)
# add searching bar to map m

plugins.ScrollZoomToggler().add_to(m)
# add scroll and zoom to map m

m.save("data_imm.html")
st_data = st_folium(m, width=725)
