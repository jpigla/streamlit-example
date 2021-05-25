import pandas as pd
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 50)

import streamlit as st
st.set_page_config(layout="wide")

st.markdown(
    """<style>
        .dataframe {text-align: left !important}
    </style>
    """, unsafe_allow_html=True)

cars = {'Ranking URL': ['https://tipps.computerbild.de/software/kommunikation/zoom-erkennt-kamera-nicht-was-tun-1056805.html','https://tipps.computerbild.de/internet/kommunikation/zoom-kostenlos-nutzen-925739.html','https://tipps.computerbild.de/software/kommunikation/zoom-account-erstellen-so-gehen-sie-vor-1049057.html'],
        'SERP Page Title': ['Zoom erkennt Kamera nicht: das können Sie dagegen tun | TippCenter',"Zoom kostenlos nutzen: So geht's | TippCenter","Zoom-Account erstellen: Mit diesen Schritten klappt's | TippCenter"],
        'Snippet': ['24. Febr. 2021 ... Zoom zählt zu den populärsten Anwendungen für private und geschäftliche Videokonferenzen. Wenn bei einem Meeting die Kamera nicht ...','29. Sept. 2020 ... Trotz kostenlosen Angebots bietet Zoom zahlreiche Funktionen an, die auch größeren Gruppen problemlos bereitstehen. Dennoch gibt es einige ...','4. Febr. 2021 ... Um einen Zoom-Account zu erstellen, benötigen Sie eine E-Mail-Adresse, die Anmeldung und Nutzung vieler Funktionen der Anwendung sind ...'],
        'Search Query': ['zoom','zoom','zoom']
        }

df = pd.DataFrame(cars)

st.dataframe(df)
