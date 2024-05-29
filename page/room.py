import streamlit as st


with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.header("⛪️ اتاق های ساحل طلایی ⛪️")





col1,col2 = st.columns(2)




with col1:
    with st.expander("101 اتاق", expanded=True):
        st.image("img/h1.png")
        st.caption("""
          اتاق ها با بهترین امکانات
            """)


        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)



with col2:
  with st.expander("220 اتاق", expanded=True):
    st.image("img/h2.png")
    st.caption(
      """
خدمات و جاهای دیدنی
      """
    )



with col1:
    with st.expander("114 اتاق", expanded=True):
        st.image("img/h3.png")
        st.caption("""
صدای امواج دریا توی اتاق
            """)


        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)



with col2:
  with st.expander("118 اتاق", expanded=True):
    st.image("img/h4.png")
    st.caption(
      """
آرامش و هیجان
      """
    )
















st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
