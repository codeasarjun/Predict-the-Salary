import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
        reg_loaded=data['model']
    return data

data=load_model()
loaded_regressor=data['model']
label_edu=data['education_label']
label_country=data['country_label']

def show_prediction_page():
    st.title('Software Developer Salary Prediction')
    st.write("""### we need some information to predict the salary """)


    # for data input 

    countries=('Sweden', 'Spain', 'Germany', 'Turkey', 'Canada', 'others',
        'France', 'Switzerland',
        'United Kingdom of Great Britain and Northern Ireland',
        'Russian Federation', 'Israel', 'Ukraine',
        'United States of America', 'Brazil', 'Italy', 'Netherlands',
        'Poland', 'Austria', 'India', 'Denmark', 'Australia', 'Belgium',
        'Iran, Islamic Republic of...', 'Argentina', 'Norway',
        'Czech Republic', 'Mexico')
    education_s=('Master’s degree', 'Bachelor’s degree', 'Post Grad')
    country=st.selectbox('Choose your country',countries)
    education=st.selectbox('Your Education Level',education_s)

    exp=st.slider('Years of Exp',0,50,3)

    cal_btn=st.button('Predict Salary')
    if cal_btn:
        x=np.array([[country,education,exp]])
        x[:,0]=label_country.fit_transform(x[:,0])
        x[:,1]=label_edu.fit_transform(x[:,1])
        x=x.astype(float)
        salary=loaded_regressor.predict(x)
        st.subheader(f"your expected salary ${salary[0]:.2f} ")
        




