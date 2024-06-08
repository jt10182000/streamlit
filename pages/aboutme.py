import streamlit as st

st.title("About Angelo 👦")



st.title("🖼️Self Gallery")


image_paths = ["./pic/me4.jpg", "./pic/me1.jpg", "./pic/me2.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 Castro, Angelo L.")

st.markdown("""
##### 👨‍👦‍👦 Family Members

* 🤱 Mother's Name: Lilibeth Castro
* 👨 Father's Name: Albert Castro
* 👧 Sister's Name: Alyssa May Castro

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** ANGELO CASTRO")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Barangay Dos Hermanas Talisay City")

with st.expander("Who I am 10 years From now??"):
    st.markdown("""
    
    #
                Ten Years From Now: A Glimpse into the Future as an Information Student
In the year 2034, I envision myself as an accomplished information professional, leveraging the skills 
                and knowledge acquired through a decade of rigorous study and practical experience. The journey from a 
                curious student to a seasoned expert has been transformative, marked by significant technological advancements, 
                evolving industry demands, and personal growth. This essay delves into the aspirations, milestones, and the envisioned
                role I will play in the realm of information science ten years from now.

                Personal Growth and Vision
The journey to becoming a prominent information professional will be shaped by continuous learning and personal growth. I will embrace a mindset
                 of curiosity and resilience, constantly seeking new knowledge and adapting to changing circumstances. My passion for information 
                 science will be fueled by a desire to make a positive impact on the world, addressing societal challenges through innovative solutions.

In 2034, I will be a testament to the transformative power of education, perseverance, and a forward-thinking vision. My career will be a blend of research 
                excellence, educational mentorship, industry leadership, and societal impact. As I reflect on the journey from an eager information student 
                to a trailblazing professional, I will take pride in the contributions I have made to the field and the legacy I continue to build.

In conclusion, ten years from now, I will be an influential information scientist, educator, and leader, dedicated to advancing the field and harnessing the 
                power of data for the greater good. My story will be one of relentless pursuit of knowledge, innovative thinking, and unwavering commitment to 
                making a difference in the world.
    """, unsafe_allow_html=True)
# Quotes
st.header("Favorite Quotes")
st.write("1. *\"Every day is a new opportunity to learn and grow.\"*")
st.write("2. *\"Embrace the challenges, for they are the stepping stones to success.\"*")
st.write("3. *\"Kindness is the language that the deaf can hear and the blind can see.\"*")
st.write("4. *\"Dream big, work hard, stay focused, and surround yourself with good people.\"*")
st.write("5. *\"In a world where you can be anything, be yourself.\"*")



import streamlit as st


images = [
    {"path": "./pic/us1.jpg", "caption": "Throughout my academic journey, the invaluable support of my classmates has been instrumental in shaping my growth and success. As I reflect on the myriad experiences shared with these individuals, it becomes evident that their contributions have enriched my learning, inspired me to persevere through challenges, and fostered a sense of camaraderie that transcends the classroom."},
    {"path": "./pic/us2.jpg", "caption": "First and foremost, my classmates have served as pillars of knowledge and insight, offering diverse perspectives that have broadened my understanding of complex subjects. Whether through lively classroom discussions, collaborative projects, or late-night study sessions, their unique viewpoints have challenged my assumptions and sparked new ideas. In this dynamic exchange of thoughts and opinions, I have gained a deeper appreciation for the multifaceted nature of learning and the power of collective intelligence."},
    {"path": "./pic/us3.jpg", "caption": "the support of my classmates has been an indispensable aspect of my academic journey, shaping my growth, inspiring my perseverance, and enriching my experience in countless ways. Together, we have navigated the challenges of academia, celebrated the joys of learning, and forged lifelong friendships that will endure far beyond the confines of the classroom. As I continue on my path, I am grateful for the privilege of learning alongside such remarkable individuals, whose kindness, generosity, and friendship have made all the difference in my journey."}
]


st.title("🖼️Gallery")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")
