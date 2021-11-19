import streamlit as st
import requests
'''
# TaxiFareModel front
'''
def submit(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    url = 'https://taxifare.lewagon.ai/predict?pickup_datetime=' + pickup_datetime \
        + '&passenger_count=' + passenger_count \
        + '&pickup_longitude=' + pickup_longitude \
        + '&pickup_latitude=' + pickup_latitude \
        + '&dropoff_longitude=' + dropoff_longitude \
        + '&dropoff_latitude=' + dropoff_latitude
         
    return requests.get(url).json()['prediction']

st.markdown('# FORM')
pickup_datetime = st.text_input('date and time', '2013-07-06 17:18:00')
passenger_count = st.text_input('passenger count', '1')
st.markdown('## pickup')
pickup_longitude = st.text_input('pickup longitude', '-73.950655')
pickup_latitude = st.text_input('pickup latitude', '40.783282')
st.markdown('## dropoff')
dropoff_longitude = st.text_input('dropoff longitude', '-73.984365')
dropoff_latitude = st.text_input('dropoff latitude', '40.769802')

if st.button('submit'):
    st.write(submit(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count))
