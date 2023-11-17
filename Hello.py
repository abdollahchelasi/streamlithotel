
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from annotated_text import annotated_text


st.set_page_config(
        page_title="هتل ساحل طلایی",
        page_icon="logo.png",
    )

with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.snow()
st.image("logo.png")


col1,col2 = st.columns(2)

with col1:
    st.header("هتل ساحل طلایی قشم")
        
annotated_text(
    "هتل ",
    ("طلایی", "ساحل"),
    ( "قشم"),
)

with col2:
    st.image("https://www.eghamat24.com/app/public/new_images/600x460/Qeshm-SahelTalaee-55.jpg")






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
