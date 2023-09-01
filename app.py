import streamlit as st
import os
import pandas as pd
import joblib as jb
heading_style = '''
<div style="color:red;" align='center'>
<h1>water_potability</h1>
</div>
'''
def return_df(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,	
Organic_carbon,Trihalomethanes,Turbidity):
    kbn={
    'ph':[ph],
    'Hardness':[Hardness],
    'Solids':[Solids],
    'Chloramines':[Chloramines],
    'Sulfate':[Sulfate],
	'Conductivity':[Conductivity],
	'Organic_carbon':[Organic_carbon],
    'Trihalomethanes':[Trihalomethanes],
    'Turbidity':[Turbidity]
    }   
    final_df=pd.DataFrame(kbn)
    return final_df
def base_model():
    bmodel=jb.load(os.path.join('finalised_rf_model.pkl'))
    return bmodel
st.markdown(heading_style,unsafe_allow_html=True)
ph=st.number_input('ph',min_value=0)
Hardness=st.number_input('Hardness',min_value=0)
Solids=st.number_input('Solids',min_value=0)
Chloramines=st.number_input('Chloramines',min_value=0)
Sulfate=st.number_input('Sulfate',min_value=0)
Conductivity=st.number_input('Conductivity',min_value=0)
Organic_carbon=st.number_input('Organic_carbon',min_value=0)
Trihalomethanes=st.number_input('Trihalomethanes',min_value=0)
Turbidity=st.number_input('Turbidity',min_value=0)
df=return_df(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,	
Organic_carbon,Trihalomethanes,Turbidity)
if st.button('Submit'):
	model=base_model()
	preds=model.predict(df)
	predictions=preds[0]
	if predictions==1:
		st.write('Good Water')
	else:
		st.write('Not suggested for drinking')