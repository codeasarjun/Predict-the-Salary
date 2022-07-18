from cProfile import label
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def accepted_countries(categories, cutoff):
    accepted_countries_mapping={}
    for i in range(len(categories)):
        if categories[i]>=cutoff:
            accepted_countries_mapping[categories.index[i]]=categories.index[i]
        else:
            accepted_countries_mapping[categories.index[i]]='others'
    return accepted_countries_mapping

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral':
        return 'Post Grad'
    return 'less than bachelors'


def clean_Experiance(x):
    if x =='Less than 1 year':
        return .5
    if x=='More than 50 years':
        return 50
    return float(x)


@st.cache
def load_data():
    df=pd.read_csv('survey_2021.csv')
    df=df[['Country','Employment','CompTotal','CompFreq','EdLevel','YearsCodePro']]
    df=df.dropna()

    


    df=df.rename({'CompTotal':'Salary'},axis=1)
    df=df.rename({'Employment':'Employment_status'},axis=1)
    df=df.rename({'YearsCodePro':'Experiance'},axis=1)
    country_map=accepted_countries(df.Country.value_counts(),400)
    df.Country=df.Country.map(country_map)
    df=df[df['Country'] !='other']
    df['EdLevel']=df['EdLevel'].apply(clean_education)
    df=df[df['Employment_status']=='Employed full-time'] 
    df=df.drop('Employment_status',axis=1)
    df.Experiance=df.Experiance.apply(clean_Experiance)

    return df
df=load_data()

def show_more_info():

    st.title('Know more about Data')
    st.write("""### Data used for prediction""")
    data=df['Country'].value_counts()
    fig1,ax1=plt.subplots()
    ax1.pie(data,labels=data.index,autopct="%.1f%%",shadow=True)
    ax1.axis("equal")
    st.pyplot(fig1)








