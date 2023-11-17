
import streamlit as st
from st_pages import Page, show_pages, add_page_title



st.set_page_config(
        page_title="هتل ساحل طلایی",
        page_icon="logo.png",
    )

with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.image("logo.png")
st.write("# هتل ساحل طلایی ")




show_pages(
    
    [
        
        Page("Hello.py", "صفحه اصلی", "🏠"),
        Page("page/sahel.py", "ساحل", "🌊"),
        Page("page/res.py", "رستوران", "👨🏻‍🍳"),
        Page("page/room.py", "اتاق ها", "⛪️"),
        Page("page/cafe.py", "کافی شاب", "🍫"),
        Page("page/marasem.py", "مراسمات", "🌈"),
    ]
    
)
