import streamlit as st

# Page title
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Portfolio")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About Me", "Skills", "Resume", "Contact"]
)

# HOME
if page == "Home":
    st.title("Welcome to My Portfolio")

    st.write(
        """
        Hello! I am a college student in RTU, passionate about technology and programming.
        This portfolio showcases my skills, experience, and background.
        """
    )

    st.subheader("About This Website")
    st.write("""
    • Skills  
    • Resume  
    • Contact Information
    """)

    st.success("Use the sidebar to navigate through my portfolio pages.")

# ABOUT
elif page == "About Me":
    st.title("About Me")

    st.write("""
    Hello! My name is John Kurt Chebat. I am currently studying Information Technology.
    I enjoy learning about programming, web development, and technology.
    """)

    st.subheader("Interests")
    st.write("""
    • Web Development  
    • Programming  
    • Networking  
    • Data Analysis
    """)

# SKILLS
elif page == "Skills":
    st.title("My Skills")

    st.subheader("Programming Languages")
    st.write("""
    • Python  
    • Java  
    • HTML  
    • CSS
    """)

    st.subheader("Tools")
    st.write("""
    • Visual Studio Code  
    • GitHub  
    • Streamlit
    """)

    st.subheader("Other Skills")
    st.write("""
    • Problem Solving  
    • Teamwork
    """)

# RESUME
elif page == "Resume":
    st.title("My Resume")

    st.subheader("Education")
    st.write("Bachelor of Science in Information Technology")

    st.subheader("Certifications")
    st.write("""
    • Basic Python Programming  
    • Networking Fundamentals
    """)

    st.subheader("Experience")
    st.write("""
    • Academic Projects  
    • Systems Integration Research
    """)

# CONTACT
elif page == "Contact":
    st.title("Contact Me through:")

    st.write("Email: kurttadeo1@gmail.com")
    st.write("Phone: 09914733165")