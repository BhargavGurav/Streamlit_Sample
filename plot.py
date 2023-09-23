import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

char_data = pd.DataFrame(np.random.randn(20, 3), columns=['line1', 'line2', "line3"])

st.header('1. Charts')
st.subheader('1.1 Line Chart')
st.line_chart(char_data)

st.subheader('1.2 Area chart')
st.area_chart(char_data)

st.subheader('1.3 Bar chart')
st.bar_chart(char_data)

st.header('2. Data visualization with matplotlib and Seaborn chart')

st.subheader('2.1 Loading DataFrame')
df = pd.read_csv('Unemployment in India.csv')
st.dataframe(df)

st.subheader('2.2 Distribution Plot using Matplotlib')
fig = plt.figure(figsize=(15, 8))
df['Region'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution Plot using Seaborn')
fig = plt.figure(figsize=(15, 8))
sns.distplot(df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean())
st.pyplot(fig)

st.header('3. Multiple Graphs')
col1, col2 = st.columns(2)
with col1:
    col1.write('KDE = False')
    fig1 = plt.figure()
    sns.distplot(df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean(), kde=False)
    st.pyplot(fig1)

with col2:
    col2.write('Hist = False')
    fig2 = plt.figure()
    sns.distplot(df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean(), hist=False)
    st.pyplot(fig2)

st.header('4. Changing styles')
col1, col2 = st.columns(2)
with col1:
    col1.write('KDE = False')
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    fig1 = plt.figure()
    sns.distplot(df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean(), kde=False)
    st.pyplot(fig1)

with col2:
    col2.write('Hist = False')
    sns.set_theme(context='poster', style='darkgrid')
    fig2 = plt.figure()
    sns.distplot(df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean(), hist=False)
    st.pyplot(fig2)

st.header('5. Exploring Different plots')
st.subheader('5.1 Scatter plot')
fig, ax = plt.subplots(figsize=(15, 8))
ax.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

st.subheader('5.2 Count plot')
fig = plt.figure(figsize=(15, 8))
sns.countplot(data=df, x = df['Region'].value_counts())
st.pyplot(fig)

st.subheader('5.3 Box plot')
# fig = plt.figure(figsize=(15, 8))
# sns.boxplot(data=df, x = 'Region', y=df.groupby('Region')[' Expected Unemployment Rate (%)'].mean())
# st.pyplot(fig)

st.subheader('5.4 Violine plot')
# fig = plt.figure(figsize=(15, 8))
# sns.boxplot(data=df, x = 'Region', y=df.groupby('Region')[' Expected Unemployment Rate (%)'].mean())
# st.pyplot(fig)