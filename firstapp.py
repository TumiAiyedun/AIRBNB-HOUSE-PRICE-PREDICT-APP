
import streamlit as st
import pandas as pd
import numpy as ny
import pickle
from PIL import Image

st.write("# AIRBNB HOUSE PRICE PREDICT APP")

model=pickle.load(open('model(rf).pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

image = Image.open('AIR BNB HOUSING IMAGE.jpg')
st.image(image)

st.sidebar.header('User Input Parameters')
  
def user_input_Parameters():
    Room_type=st.sidebar.selectbox('Room Type', ('Private room','Entire home/apt','Shared room'))
    if Room_type=='Entire home/apt':
        Entire=1
        Private=0
        Shared=0 
        
    if Room_type=='Private room':
        Entire=0
        Private=1
        Shared=0 
        
    if Room_type=='Shared room':
        Entire=0
        Private=0
        Shared=1 
        
    Region_hood=st.sidebar.selectbox('Region',('North_Region', 'North-East_Region', 'East_Region', 'West_Region'))    
    if  Region_hood=='Central_Region':
        Central=1
        North=0
        East=0
        West=0
        North_East=0
        
    if  Region_hood=='North_Region':
        Central=0
        North=1
        East=0
        West=0
        North_East=0
        
    if  Region_hood=='East_Region':
        Central=0
        North=0
        East=1
        West=0
        North_East=0
        
    if  Region_hood=='West_Region':
        Central=0
        North=0
        East=0
        West=1
        North_East=0
        
    if  Region_hood=='North-East_Region':
        Central=0
        North=0
        East=0
        West=0
        North_East=1
        
    
    Host_id=st.number_input('Host ID', step=1)
    Host_list_count=st.number_input('Host listing count', step=1)
    Longitude=st.number_input('Building longitude (degrees)', step=1)
    Latitude=st.number_input('Building latitude (degrees)', step=1)  
    minimum_nights=st.number_input('How many nights will you be staying for?',step=1)
    availability=st.number_input('Number of Days Available', step=1)
    last_rev_month=st.number_input('Month of last review?', max_value=12, min_value=1,step=1)
    last_rev_year=st.number_input('Year of last review?', max_value=2022, min_value=2012,step=1) 
    last_rev_day=st.number_input('Day of last review?', max_value=31, min_value=1,step=1) 
    no_of_reviews_year=st.number_input('Total number of reviews', step=1)
    reviews_per_month=st.number_input('Number of reviews per month?', step=1)
    
    data={'host_id':Host_id,
          'latitude':Latitude,
          'longitude':Longitude,
          'last_review_month':last_rev_month,
          'last_review_year':last_rev_year,
          'last_review_day': last_rev_day,
          'minimum_nights':minimum_nights,
          'number_of_reviews': no_of_reviews_year,
          'calculated_host_listings_count': Host_list_count,
          'availability_365':availability,
          'room_type_Private_room':Private,
          'room_type_Shared_room':Shared,
          'reviews_per_month':reviews_per_month,
          'neighbourhood_group_West Region':West,
          'neighbourhood_group_North-East Region': North_East,
          'neighbourhood_group_East Region':East,
          'neighbourhood_group_North Region':North}
         
              
    Parameters = pd.DataFrame(data, index=[0])
    return Parameters
              
input_df = user_input_Parameters()
input_df = scaler.transform(input_df)
              
if st.button('PREDICT'):
    y_out=model.predict(input_df)
    st.write(f' This room will cost you $',int(y_out[0]))
              
        
