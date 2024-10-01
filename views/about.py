import streamlit as st
from pathlib import Path

from forms.contact import contact_form

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "resume.pdf"

with open(resume_file,"rb") as pdffile:
    resume = pdffile.read()

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

    

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.image("assets/profile-pic.png")

with col2:
    st.title("Ugochukwu Lumanze", anchor=False)
    st.write('''Experienced and detail-oriented Python Backend Developer with a strong background in designing and implementing scalable 
             and efficient backend systems. Adept at collaborating with cross-functional teams to drive project success. 
             Proven expertise in optimizing database performance, implementing RESTful APIs, and ensuring the security and
             integrity of data. Committed to staying current with emerging technologies and continuously enhancing development skills''')
    st.download_button(
        label=" 📄  Download Resume",
        data= resume,
        file_name=resume_file.name,
        mime= "application/octet-stream" 
        )
    if st.button("✉️ Contact Me"):
        show_contact_form()


#-------SOCIAL_MEDIA------------------#
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/ugochukwu-lumanze",
    "GitHub":"https://github.com/Ugochukwulumanze",
    "Twitter": "https://x.com/Ulumanze",
    "Facebook":"https://web.facebook.com/ugochukwu.lumanze?_rdc=1&_rdr",
}
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
 
# --- EXPERIENCE & QUALIFICATIONS ---    
st.write('\n')
st.header('WORK EXPERIENCE',anchor=False)
st.subheader('Python Backend Engineer-NIIT',anchor=False)
st.write('September 2021 - Present')
st.write(
    """
    - Developed and maintained backend systems using Python and Django, improving performance by 30%
    - Designed and implemented RESTful APIs, reducing integration issues by 15%.
    - Collaborated with frontend developers to integrate user-facing elements, cutting deployment time by 20%.
    - Conducted code reviews, improving team efficiency and ensuring compliance with best practices.
    - Utilized a stack including AWS EC2, MySQL, and Docker to deploy cloud-based solutions.
    """
)
# --- SKILLS ---

st.write("\n")
st.header("Hard Skills", anchor=False)
st.write(
    """
   - Back-End: Python, Django, DjangoRestFramework, Flask, FastAPI.
   - Database: MongoDB, MySQL, PostgreSQL, SQLite
   - Cloud and DevOps: AWS (S3, EC2, RDS, DynamoDB, SES, Transcribe, Amplify), Docker, CI CD with GitHub Actions, Nginx, PM2, Linux.
   - Front-End: HTML, CSS, Bootstrap, Tailwind CSS
   - Tools: Insomnia, Figma, VS Code, Open AI, GitHub, Firebase, Gitlab, Slack, etc.
   """
)
st.write("\n")
st.header("Soft Skills", anchor=False)
st.write('I prioritize communication, teamwork, creativity, empathy, accountability, patience, confidence, collaboration, and time management.')