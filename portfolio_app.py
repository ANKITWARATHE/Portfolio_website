import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Ankit Warathe - Portfolio", page_icon="📊", layout="wide")

# Header
st.title("Ankit Warathe")
st.subheader("Data Scientist | Machine Learning | Deep Learning")

# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Skills", "Projects", "Experience", "Contact"])

# About Section
if page == "About":
    st.header("About Me")
    st.write("""
    Data Scientist with expertise in machine learning, deep learning, and data analytics. 
    Passionate about solving real-world problems using AI and data-driven insights.
    """)

# Skills Section
elif page == "Skills":
    st.header("Skills")
    skills = [
        "Python, SQL, Pandas, NumPy",
        "Machine Learning: Scikit-learn",
        "Deep Learning: TensorFlow, PyTorch, Keras",
        "Computer Vision: OpenCV, YOLO",
        "NLP: NLTK, TextBlob",
        "Data Visualization: Power BI, Tableau",
        "Cloud: AWS (S3, EC2, SageMaker)"
    ]
    for skill in skills:
        st.markdown(f"✅ {skill}")

# Projects Section
elif page == "Projects":
    st.header("Projects")
    st.subheader("Book Recommendation System")
    st.write("Designed a personalized book recommendation system using collaborative filtering.")
    st.markdown("[GitHub Repository](https://github.com/ANKITWARATHE/Book_Recommendation_System.git)")
    
    st.subheader("Cabinet Part Identification")
    st.write("Developed a computer vision model for switchgear cabinet part identification.")

# Experience Section
elif page == "Experience":
    st.header("Experience")
    st.subheader("Data Science Intern - AISPRY (10/2024 - 11/2024)")
    st.write("Developed a computer vision model achieving mAP of 0.808.")
    
    st.subheader("Cataloging Executive - Iksula Services (10/2023 - 09/2024)")
    st.write("Designed data cataloging frameworks and improved data workflows.")

# Contact Section
elif page == "Contact":
    st.header("Contact")
    st.write("📧 Email: ankitwarathe@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/ankit-warathe-161345b3/)")
    st.write("🐙 [GitHub](https://github.com/ANKITWARATHE)")
