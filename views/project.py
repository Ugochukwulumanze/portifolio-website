import streamlit as st 

st.title('Projects')

col1 , col2 = st.columns(2,gap="small")
st.write('\n')
with col1:
    st.subheader("AI blog generator")
    st.image('assets/front page.JPG')
    st.markdown("[Click here to view the github repo](https://github.com/Ugochukwulumanze/ai-blog-generator/tree/master)")
    
with col2:
    st.subheader('Description')
    st.write("""I developed an AI-powered blog generator that transforms YouTube video content into blog posts using AssemblyAI and OpenAI APIs.
             The frontend was built with HTML and TailwindCSS, while the backend was developed using Django.
             The application sends the YouTube link via a JavaScript function, transcribes the video using AssemblyAI,
             and generates the blog post from the transcript through OpenAI's language model.""")
    st.write("Tools Used: HTML, TailwindCSS, OpenAI API, Django, AsemblyAI API")
    
st.write('\n')
col1, col2 = st.columns(2,gap="small")
with col1:
    st.subheader('LittleLemon API')
    st.image('assets/Menu list endpoint.PNG')
    st.markdown("[Click here to view the github repo]()")
    
with col2:
    st.subheader("Description")
    st.write("""I designed and developed a robust API for LittleLemon Restaurant, based in California, USA, handling the entire process from requirement analysis to production deployment.
             Using Django and DjangoRestFramework, I created endpoints for Managers, Users, and Delivery Crew, and implemented secure authorization and authentication with the Djoser library.
             Data was stored in a MySQL database, with the backend and database deployed to AWS EC2 and FLOW""")
    st.write('Tools Used: Django, DjangoRestFramework, Djoser, Python')
    
st.write('\n')
col1, col2 = st.columns(2,gap="small")
with col1:
    st.subheader('Keepclean')
    st.image('assets/homepage.PNG')
    st.markdown("[Click here to view the github repo](https://www.google.com)")
    
with col2:
    st.subheader("Description")
    st.write("""I developed a full-stack web application that enables customers to easily request waste disposal and cleaning services. 
             The frontend was built using HTML, Tailwind CSS, and JavaScript, while the backend was powered by Django and a MySQL database to manage customer details and subscriptions. 
             This platform allows customers to subscribe to waste services, ensuring prompt and efficient disposal.""")
    st.write('Tools Used: HTML, TailwindCSS, JavaScript, MySQL, Python, Django, Google and Facebook auth, AWS EC2')