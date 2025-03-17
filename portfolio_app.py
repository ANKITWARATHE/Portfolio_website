import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Ankit Warathe - Portfolio", page_icon="📊", layout="wide")

# Header
st.title("Ankit Warathe")
st.subheader("Data Scientist | Machine Learning | Deep Learning")


# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Skills", "Projects", "Experience", "Certificates", "Contact"])

# About Section
if page == "About":
    st.header("About Me")
    st.write("""
    Data Scientist with expertise in machine learning, deep learning, and data analytics. Skilled in Python, SQL, Power BI, and Tableau, with experience in computer vision, Natural Language Processing (NLP), and predictive modeling. Certified in Python for Data Science and Data Visualization, with a proven ability to optimize workflows and drive data-driven decision-making. Passionate about solving real-world problems through Artificial Intelligence (AI) and analytics.
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
    st.write("●	Developed a computer vision model for switchgear cabinet part identification with a mean Average Precision (mAP) of 0.808, significantly reducing manual efforts.")
    st.write("● Created an interactive Streamlit-based web application for real-time component identification, improving operational efficiency.") 
    st.write("● Improved operational efficiency by reducing manual labeling efforts, saving time, and enhancing data quality.") 

    st.write("\n")
    
    st.subheader("Cataloging Executive - Iksula Services (10/2023 - 09/2024)")
    st.write("●	Designed and implemented efficient data cataloging frameworks to streamline data discoverability and usability.")
    st.write("●	Conducted annotation tasks to label datasets accurately, ensuring high-quality data for machine learning and computer vision models.")
    st.write("●	Collaborated with cross-functional teams to improve data workflows.")


# Certificate
elif page == "Certificates":
    st.header("Certificates")
    st.write("1. Python for Data Science Certification by IIT Madras- 2023")
    st.write("2. Basic SQL Course by 360DigiTMG - 2023")
    st.write("3. Data Visualization using Power BI by 360DigiTMG - 2023")
    st.write("4. Data Visualization Using Tableau by 360DigiTMG - 2024")
    st.write("5. Python Fundamentals by NASSCOM - 2024")
    st.write("6. Certificate Course on Data Science by NASSCOM – 2025")



# Contact Section
elif page == "Contact":
    st.header("Contact")
    st.write("📧 Email: ankitwarathe@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/ankit-warathe-161345b3/)")
    st.write("🐙 [GitHub](https://github.com/ANKITWARATHE)")
