import streamlit as st
import pandas as pd

st.subheader('Uploading the csv file ')
df = st.file_uploader('Upload the CSV file : ', type=['csv', 'xlsx'])

# if df is not None:
#     st.dataframe(df)
st.subheader('Loading the csv file ')
if df is not None:
    df = pd.read_csv(df, encoding='utf-8')
    st.table(df.head())

st.subheader('Lets see images ')
img = st.file_uploader('Upload image file ', type=['jpg', 'jpeg', 'png', 'svg'])
if img is not None:
    st.image(img)

st.subheader('Working with Videos')
vdo = st.file_uploader('Upload video file ', type=['mkv', 'mp4'])
if vdo is not None:
    st.video(vdo, start_time = 5)

st.subheader('Working with Audio')
ado = st.file_uploader('Upload Audio file ', type=['mp3', 'mp2', 'wav'])
if ado is not None:
    st.audio(ado)