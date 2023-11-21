import streamlit as st



with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)



st.header("""🌈 مراسم ساحل طلایی

ما در هتل ساحل طلایی جشن تولد و مراسمات عقد شاد و به یاد ماندنی برای شما آماده کرده ایم .
از طراحی دکوراسیون زیبا و نوربردازی شگفت انگیز تا منوی لذیذ و خدمات عالی , همه چیز برای شما تدارک دیده شده است .
""")

st.divider()

col1,col2 = st.columns(2)




with col1:
    with st.expander("مراسم", expanded=True):
        st.image("img/m1.png")
        st.caption("""
            مراسمات هتل ساحل طلایی
            """)
       



with col2:
  with st.expander("ویدیوی مراسم", expanded=True):
    st.video("m1.mp4",)
    st.caption(
      """
      ویدیویی از مراسمات هتل ساحل طلایی
      """
    )




















st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
