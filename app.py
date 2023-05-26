import streamlit as st
from PIL import Image
import base64
from pathlib import Path

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#image = Image.open('photo-round.png')

#with open("photo-round.png", "rb") as f:
   # data = base64.b64encode(f.read()).decode("utf-8")

  #  st.markdown(
      #  f"""
     #   <div style="display:table;margin-top:-20%;margin-left:20%;">
     #       <img src="data:image/png;base64,{data}" width="100" height="150">
     #   </div>
    #    """,
    #    unsafe_allow_html=True,
    )
#col1, col2, col3 = st.columns([0.2, 5, 0.2]) 
#col2.image(image, use_column_width=True)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
    img_to_bytes("photo-round.png")
)
st.markdown(
    header_html, unsafe_allow_html=True,
)












#def img_to_bytes(img_path):
    #img_bytes = Path(img_path).read_bytes()
   # encoded = base64.b64encode(img_bytes).decode()
   # return encoded
#def img_to_html(img_path):
    #img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      #img_to_bytes(img_path)
  #  )
   # return img_html

#st.markdown(img_to_html('photo-round.png'), unsafe_allow_html=True)
    



    

#st.image(image, width=155)
#st.markdown("<h1 style='text-align: center; '>Bratkovsky Evgeny (Data Scientist, MSc Software Engineering)</h1>", unsafe_allow_html = True)
st.title(':orange[Bratkovsky Evgeny]')
#st.markdown('#:orange[Data Scientist],:orange[MSc Software Engineering]')
#st.title(':red[MSc Software Engineering]')
#st.write('''
# *Bratkovsky Evgeny*
## *MSc Software Engineering* 
#''')



st.markdown('## *About me*', unsafe_allow_html=True)
#st.info('''
#*I'm a Data Scientist. Basically, I'm like a pathologist, but doing autopsies on different data*:). 
#*I have a lot of experience working in banks and I have a good understanding of almost all banking business processes, which helps me a lot when I build models to develop the banking business*.
#''')
st.write('I am a Data Scientist :sunglasses:. I have a lot of experience working in banks and I have a good understanding of almost all banking business processes, which helps me a lot when I build models to develop the banking business. ')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #cb9216;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/evgeny-bratkovsky555-847ab6181/" target="_blank">Bratkovsky Evgeny</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link enabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact-with-me">Contact with me</a>
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
## *Education*
''')

txt('**MSc Software Engineering**, Belarusian State University of Informatics and Radioelectronics, Belarus','2020-2022')
st.markdown('''
- Average grade: `9` from `10`
- Defended MSc thesis on credit scoring models and algorithms based on neural networks.
''')

txt('**Bachelor degree in Finance & credit**, Belarusian State Economic University, Belarus','2009-2014')
st.markdown('''
- Average grade: `7` from `10`.
''')

st.markdown('''
## *Work Experience*
''')

txt('**Business Analyst/Data Scientist**, Priorbank, Belarus','06.2021 — 06.2023')
st.markdown('''
- Creating models for segmenting bank customers, predicting churn, scoring and many others.
- Organised a Data Science course for bank staff as part of the bank's IT Academy.
- Implementation of MLOps methodology in the bank.
- Automation of data processing and transfer to cloud data storage.
''')

txt('**Senior Internal Audit Specialist**, Belinvestbank, Belarus','04.2018 — 06.2021')
st.markdown('''
- Audit of the business processes, improvement of the IT processes.
''')



st.markdown('''
## *Skills*
''')
txt3('Programming', '`Python`, `Javascript`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `Numpy`')
txt3('Data visualization', '`Apache Superset`,`Tableau`,`Matplotlib`, `Seaborn`, `Plotly`, `Altair`')
txt3('Machine Learning', '`Catboost`,`XGBoost`,`Logistic Regression`, `Random Forest`,`DBSCAN and many others`')
txt3('Deep Learning', '`TensorFlow`,`PyTorch`,`ANN`,`Computer Vision`, `NLP`')
txt3('Model deployment', '`Streamlit`, `Gradio`,`Flask`')



st.markdown('''
## *Contact with me*
''')
contact_form = """
<form action="https://formsubmit.co/zhenyabratkovski5@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#def local_css(file_name):
    #with open(file_name) as f:
        #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#local_css("style.css")

