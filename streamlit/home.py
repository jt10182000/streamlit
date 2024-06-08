
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "👨‍💻"),
        Section("Main Page", "📢"),
        Page("pages/aboutme.py", "👦🏻ABOUT ME", "1️⃣", in_section=True),
        Page("pages/description.py", "📜Streamlit App Description", "2️⃣", in_section=True),
        Page("pages/learnings.py", "🧠 What I Have Learned", "3️⃣", in_section=True),
     
  
        Section("Sample Projects", "📂"),
        Page("pages/analyzer.py", "📝Basic Sentiment Analyzer", "1️⃣", in_section=True),
        Page("pages/classification.py", "💐Flower Classification", "2️⃣", in_section=True),
        Page("pages/prediction.py", "📊 Prediction", "3️⃣", in_section=True),

        Section("Project Source Code","💻"),
        Page("pages/analyze_src.py","Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/classification_src.py","Image Classificatiom SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py","Prediction SRC", "3️⃣", in_section=True),
        
    ]
)

hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS PRESENTED BY: ")
st.header("CASTRO, ANGELO of BSIS 3B")
st.image("./me.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("For more info. Contact [Angelo Casstro](https/facebook.com/gello.0112) on Fb")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("History, Purpose and, Usage"""):
    st.markdown("""
    
    
    #

        History of Machine Learning
Machine learning, a subfield of artificial intelligence (AI), has evolved over decades. The concept dates back to the 1950s, when Arthur Samuel,
             an IBM engineer, created a checkers-playing program, pioneering the term "machine learning." In 1957, Frank Rosenblatt developed the perceptron, an 
            early neural network model. During the 1960s and 1970s, research in AI and machine learning grew, but progress slowed due to limited computational power and data availability.
               
                 Purpose of Machine Learning
he primary purpose of machine learning is to develop algorithms and statistical models that enable computers to perform specific tasks without explicit instructions, relying instead on patterns and inference.
                 Machine learning aims to automate and improve decision-making processes, enhance the accuracy of predictions, and uncover insights from large and complex datasets. Its objectives include:

* Automation: Automating repetitive and mundane tasks, improving efficiency and reducing human error.
* Prediction: Making accurate predictions based on historical data, such as stock market trends, weather forecasting, and disease outbreaks.
* Pattern Recognition: Identifying patterns and relationships in data that are not apparent to human analysts.
* Personalization: Tailoring services and products to individual users' preferences, such as recommendation systems in e-commerce and content platforms.
* Optimization: Enhancing processes and systems, such as supply chain management, through data-driven decision-making.
                
                 Usage of Machine Learning
Machine learning is used across various industries and applications, including:

* Healthcare: Diagnosing diseases, predicting patient outcomes, and personalizing treatment plans through analyzing medical data and imaging.
* Finance: Fraud detection, algorithmic trading, credit scoring, and risk management by analyzing financial data.
* Retail: Personalized recommendations, inventory management, and customer segmentation to improve sales and customer satisfaction.
* Manufacturing: Predictive maintenance, quality control, and process optimization through analysis of sensor data and production metrics.
* Transportation: Autonomous vehicles, traffic prediction, and route optimization to enhance safety and efficiency.
* Entertainment: Content recommendation, user behavior analysis, and audience targeting in media and entertainment platforms.             
    #""", unsafe_allow_html=True)

st.title('Introduction to the Streamlit Application Project')

st.markdown("""


##### 👨‍🔧 More Content

Welcome to our Streamlit Application Project, a comprehensive initiative designed to harness the power of machine learning through an 
            intuitive and interactive web interface. This project aims to showcase the versatility and practicality of machine learning 
            models in real-world applications, specifically focusing on three key areas: sentiment analysis, image classification, and predictive analytics.
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./ml.jpg")


st.markdown("""
Machine learning is a branch of artificial intelligence (AI) that focuses on developing algorithms and statistical models that enable computers 
            to perform tasks without explicit instructions. Instead, these systems learn from data, identifying patterns and making decisions with 
            minimal human intervention. The core idea is to allow the machine to improve its performance over time as it is exposed to more data.
Quantitative methods refer to a set of techniques used in research and analysis that rely on quantifiable data, numerical values, and statistical 
            methods to investigate phenomena, test hypotheses, and draw conclusions. These methods are particularly useful in fields such as social sciences, 
            economics, psychology, and natural sciences, where researchers seek to measure and analyze observable and measurable variables. 
                       
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
