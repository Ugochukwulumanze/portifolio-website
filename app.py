import streamlit as st
from pathlib import Path



# ---Page SetUP---
PAGE_TITLE = "Digital CV | Ugochukwu Lumanze"
PAGE_ICON = ":wave:"
about_page = st.Page(
    page = 'views/about.py',
    title = PAGE_TITLE,
    default = True
)


project_page = st.Page(
    page='views/project.py',
    title="project",
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# ----Navigation Setup------#
pg = st.navigation(pages=[about_page,project_page])

# -----Share On All Paes ---#
st.logo('assets/learn with ugo.png')
st.sidebar.text('Made with ❤ by Ugo')

pg.run()
