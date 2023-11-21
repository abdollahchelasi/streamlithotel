import streamlit as st

with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)



st.text("🌊 با نگاهی به این نمای ساحل دریا، شما می‌توانید امواج آرام و زیبای دریا را مشاهده کنید 🌊")





col1,col2,col3 = st.columns(3)




with col1:
    with st.expander("ساحل", expanded=True):
        st.image("img/d.jpg")
        st.caption("""
            ساحل
            """)


        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)



with col2:
  with st.expander("ساحل", expanded=True):
    st.image("img/d2.jpg")
    st.caption(
      """
        ساحل
      """
    )



with col3:
  with st.expander("ساحل", expanded=True):
    st.image("img/d3.jpg")
    st.caption(
      """
        ساحل
      """
    )



















st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)