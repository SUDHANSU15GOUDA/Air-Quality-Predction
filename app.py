import streamlit as st 
from streamlit_option_menu import option_menu
import pickle
import pandas as pd



with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Predection Page","Graphs and Charts","About us"]
    )


if selected == 'Predection Page':


    st.title('Air Quality Index Prediction')

    dt = pickle.load(open('dt.pkl','rb'))


    

    select_co = st.slider('CO AQI Value',min_value = 0,max_value = 70,step = 1,value = 0)
    
    select_ozone = st.slider('Ozone',min_value = 0,max_value = 222,step = 1,value = 0)
    
    select_no2 = st.slider('No2',min_value = 0,max_value = 91,step = 1,value = 0)
    
    select_pm= st.slider('Pm2.5',min_value = 0,max_value = 500,step = 1,value = 0)
    
    
    
            
        
        
    if st.button('Predict'):
        input_df = pd.DataFrame({'CO AQI Value':[select_co],
                                 'Ozone AQI Value':[select_ozone],
                                 'NO2 AQI Value':[select_no2],
                                'PM2.5 AQI Value':[select_pm]
                                })

        # #st.table(input_df)
        result = float(dt.predict(input_df))
        #result_percentage = dt.predict_proba(input_df)
        
        st.title('Predicted Outcome...')
        
        st.header('Concrete Compressive Strength')
        
        st.info(result)
    




# 'cement', 'blast_furnace_slag', 'fly_ash', 'water', 'superplasticizer',
#        'coarse_aggregate', 'fine_aggregate ', 'age',
#        'concrete_compressive_strength']


