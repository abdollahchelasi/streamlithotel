import streamlit as st



with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.text("🍫  کافی شاپ ساحل طلایی")






col1,col2 = st.columns(2)




with col1:
    with st.expander("کافی شاپ", expanded=True):
        st.image("img/c.png")
        st.caption("""
        کافی شاپ
            """)


        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)



with col2:
  with st.expander("کافی شاپ", expanded=True):
    st.image("img/c1.jpg")
    st.caption(
      """
          کافی شاپ
      """
    )




with st.expander("کافی شاپ", expanded=True):
  st.image("img/c2.jpg")
  st.caption(
  """
      کافی شاپ
  """
)












st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)