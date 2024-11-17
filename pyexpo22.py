import streamlit as st

# Portfolio title and introduction
st.title("My Portfolio")
st.header("Hi, I'm Swathi!")
st.subheader("Aspiring IT Professional | First Graduate of My Family")

# About section
st.write("""
Welcome to my portfolio! I'm passionate about technology and always eager to learn and grow in the field of Information Technology. This portfolio showcases my skills, projects, and contact information.
""")

# Skills section
st.header("Skills")
st.write("""
- Python programming
- Web development (HTML, CSS, and basic JavaScript)
- Problem-solving and critical thinking
- Team collaboration and leadership
""")

# Projects section
st.header("Projects")
st.write("""
- **Rock, Paper, Scissors Game**: Created a fun game using Python, HTML, and CSS.
- **Portfolio Website**: Designed this interactive portfolio using Streamlit.
- **Student Management System**: Built a basic student records app using Python.
""")

# Contact information
st.header("Contact Me")
st.write("Feel free to reach out to me through the following:")
st.write("- **Email**: swathivkg837@gmail.com")
st.write("- **LinkedIn**: [Swathi's LinkedIn](https://www.linkedin.com/in/swathivkg/)")

# Footer
st.write("Thank you for visiting my portfolio!")