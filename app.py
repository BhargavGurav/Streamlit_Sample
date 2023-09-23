import streamlit as st

st.title('title() -> for titles')       # to show title
st.header('header() -> for headers')       # to show header
st.subheader('subheader() -> for subheaders') # for subheaders
st.text('text() -> for text ')               # for texts

st.markdown('markdown() -> for markdowns like in jupyter notebook')
st.markdown('# Markdown 1')
st.markdown('## Markdown 1')
st.markdown('### Markdown 1')
st.markdown('#### Markdown 1')
st.markdown('##### Markdown 1')
st.markdown('###### Markdown 1')
st.markdown('- Markdown 1')
st.markdown('`Markdown 1`')
st.markdown('~Markdown 1~')
st.markdown('*Markdown 1*')
st.markdown('**Markdown 1**')
st.markdown('_Markdown 1_')

st.success('success() -> for success message')  # for success message
st.warning('warning() -> for warning message') # for warning
st.info('info() -> for info blue message')
st.error('error() -> for error message')

exp = ZeroDivisionError('Division not possible by 0')
st.exception(exp)

st.help(ZeroDivisionError)

st.write('range(1, 11)')
st.write(range(1, 11))
st.write(1+2+5)             # code or strings

st.code('x = 10 \n'
        'for i in range(x):\n'
        '   print(i)')                # to write a code


st.checkbox('Vegeterian')
st.checkbox('Non-Vegeterian')       # to chcekboxes

if(st.checkbox('Mix')):
    st.write('You prefer to eat both')

st.radio('Gender : ', ('Male', 'Female', 'Trans'))

radioButton = st.radio('Select Mood : ', ('Neutral', 'Happy', 'Sad', 'Angry'))

if(radioButton == 'Happy'):
    st.write('You are happy good for you.')
elif(radioButton == 'Sad'):
    st.write('Oww, You can talk to me if you want')
elif(radioButton == 'Angry'):
    st.write('Oh man anger is not good for you.')


st.subheader('Select Domain : ')
selectBoxAns = st.selectbox('Data Science : ', ['Data analysis', 'Data mining', 'Web scrapping', 'Machine Learning', 'Deep learning', 'Natural Language Processing', 'Computer Vision', 'Image Processing'])

st.write(selectBoxAns, ' then, Good choice Bro !')

st.subheader('Select Domain : ')
selectBoxAns = st.multiselect('Data Science : ', ['Data analysis', 'Data mining', 'Web scrapping', 'Machine Learning', 'Deep learning', 'Natural Language Processing', 'Computer Vision', 'Image Processing'])

st.subheader('Button')
if(st.button('Click me')):
    st.write('Thanks for clicking')

st.subheader('Slider')
value = st.slider('Select efficiency level : ', 1, 100, step = 1)
if(value<50):
    st.write('Keep practising bro! minimum you should be 50%')
else:
    st.write('Fantastic man, keep gaining knowledge')

st.subheader('User input : ')
name = st.text_input('Name : ')
# if(name != ''):
#     st.write('Hello ', name)
password = st.text_input('Password : ', type='password')

st.subheader('Text area')
st.text_area('Introduce yourself in 200-300 words : ')

st.subheader('Number')
st.number_input('Select age : ', 18, 100)

st.subheader('Date')
st.date_input('Select Date : ')

st.subheader('Time')
st.time_input('Select Time : ')


