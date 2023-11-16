
import streamlit as st
from st_pages import Page, show_pages, add_page_title



st.set_page_config(
        page_title="هتل ساحل طلایی",
        page_icon="👋",
    )

with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

  
st.write("# هتل ساحل طلایی 👋")



show_pages(
    
    [
        
        Page("app.py", "صفحه اصلی", "🏠"),
        Page("page/game.py", "ساحل", "🎮"),
        Page("page/application.py", "رستوران", "📳"),
        Page("page/arz.py", "اتاق ها", "₿"),
        Page("page/rahnama.py", "کافی شاب", "🚦"),
        Page("page/rahnama.py", "مراسمات", "🚦"),
    ]
    
)
