import streamlit as st
import datetime # Add this!
import requests # Add this!
import pandas as pd
import numpy as np
import pydeck as pdk
mapboxApiToken = 'pk.eyJ1IjoiYWNlZGIiLCJhIjoiY2tpOHQ2dHpoMDJhMTJ6cmtjMzZzc2phNyJ9.POuta9x6vq_aR-uBEvakOw'

'''
# TaxiFareModel front

This front queries the Le Wagon [taxi fare model API](http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''

key = '2012-10-06 12:10:20.0000001'
pickup_date = st.date_input('pickup date', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup time', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}UTC'
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

# 1. Enter here the address of your API.
url = 'http://taxifare.lewagon.ai/predict_fare'

# 2. Let's build a dictionary containing the parameters for our API.
params = dict(
    key=key,
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

# 3. Let's call our API using the `requests` package.
response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API.
prediction = response.json()

## Finally, we can display the prediction to the user.

f"${round(prediction['prediction'], 2)}"


# @st.cache
# def get_map_data():
#     print('get_map_data called')
#     return pd.DataFrame(
#         data= np.array([
#             [pickup_longitude,pickup_latitude],
#             [dropoff_longitude,dropoff_latitude],
#             ]),
#         columns= ['lon','lat'],
#         index=['star','end']
#         )

# df = get_map_data()
# #st.map(df)
# GREEN_RGB = [0, 255, 0, 40]
# RED_RGB = [240, 100, 0, 40]
# st.pydeck_chart(pdk.Deck(
#      map_style='mapbox://styles/mapbox/light-v9',
#      initial_view_state=pdk.ViewState(
#          latitude=(pickup_latitude+dropoff_latitude)/2,
#          longitude=(pickup_longitude+dropoff_longitude)/2,
#          zoom=8,
#          pitch=40,
#      ),
#      layers=[
#         pdk.Layer(
#         'ScatterplotLayer',
#         df,
#         get_position=['lon', 'lat'],
#         auto_highlight=False,
#         get_radius=300,
#         get_fill_color='[180, 0, 200, 140]',
#         pickable=True
#          ),
#         pdk.Layer(
#             "ArcLayer",
#             data=df,
#             get_width=6,
#             get_source_position=[pickup_longitude, pickup_latitude],
#             get_target_position=[dropoff_longitude, dropoff_latitude],
#             get_tilt=2,
#             get_source_color=GREEN_RGB,
#             get_target_color=RED_RGB,
#             pickable=True,
#             opacity=100,
#             auto_highlight=False
#             )
#      ],
#  ))
