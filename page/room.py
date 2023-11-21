import streamlit as st


with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.header("اتاق های ساحل طلایی")





col1,col2 = st.columns(2)




with col1:
    with st.expander("اتاق", expanded=True):
        st.image("https://www.vidagasht.com/wp-content/uploads/2020/01/golden-beach-hotel-qeshm-triple-room-2.jpg")
        st.caption("""
        اتاق ها
            """)


        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)



with col2:
  with st.expander("اتاق", expanded=True):
    st.image("https://cdn.alibaba.ir/inh/domestic-hotel/image_5e617b9c-d139-4912-adf5-bfbfc8070caf.jpg")
    st.caption(
      """
          اتاق ها
      """
    )



















st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
