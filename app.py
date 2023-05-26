import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Bratkovsky Evgeny, MSc Software Engineering
##### *CV* 
''')

image = Image.open('photo.jpg')
st.image(image, width=200)

st.markdown('## About me', unsafe_allow_html=True)
st.info('''
I'm a machine learning engineer at a bank. Basically, I'm like a pathologist, but doing autopsies on different data :). 
I have a lot of experience working in banks in different positions and I have a good understanding of almost all banking business processes, which helps me a lot when I build models to develop the banking business.
''')


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #cb9216;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/evgeny-bratkovsky555-847ab6181/" target="_blank">Bratkovsky Evgeny</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


st.markdown('''
## Education
''')

txt('**Master's degree** (Software Engineering), *Belarusian State University of Informatics and Radioelectronics*, Belarus',
'2020-2022')
st.markdown('''
- Average grade: `9` from `10`
- Defended MSc thesis on credit scoring models and algorithms based on neural networks.
''')

txt('**Bachelor's degree** (Finance and credit), *Belarusian State Economic University*, Belarus',
'2009-2014')
st.markdown('''
- Average grade: `7` from `10`.
''')

st.markdown('''
## Work Experience in IT
''')

txt('**Business Analyst/Data Scientist**, Priorbank, Minsk, Belarus',
'06.2021-06.2023')
st.markdown('''
- Creating models for segmenting bank customers, predicting churn, scoring and many others.
- Organised a Data Science course for bank staff as part of the bank's IT Academy.
- Implementation of MLOps methodology in the bank.
- Data processing and transfer to cloud hosting was automated.
''')

txt('**Senior Internal Audit Specialist**, Belinvestbank, Minsk, Belarus',
'04.2018-06.2021')
st.markdown('''
- Audit of the business processes of the bank, improvement of the IT processes.
''')


st.markdown('''
## Skills
''')
txt3('`Python`, `Javascript`,'`SQL`,`Streamlit`,`Flask`,`AWS`, `TensorFlow`,`PyTorch`,`Docker`,`PL\SQL Developer`,`NLP`,`Computer Vision`, 
`Scoring models & many others`')



