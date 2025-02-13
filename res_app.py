import streamlit as st

about_me = st.Page(
                    page="views/about_me.py",
                    title = "About Me", 
                    icon=":material/account_circle:",
                    default=True
                    
)

project_1_page = st.Page(
                    page="views/my_project.py",
                    title = "My Project", 
                    icon=":material/smart_toy:",
                    
)

# ------------Navigate setup-------
pg = st.navigation(pages=[about_me,project_1_page])

# pg = st.navigation(
#     {
#                 "info":[about_me],
#                 "projects":[project_1_page]
#     }
# )

# ---------share accross all the pages

# st.logo("asssets/anuj_logo.png", size="large", link=None, icon_image=None)
st.sidebar.text("Made with ❤ By Anuj")

# ---------Run Application---
pg.run()
