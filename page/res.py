import streamlit as st



with open("c.css") as f:
  st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.text("👨🏻‍🍳 رستوران ساحل طلایی 👨🏻‍🍳")


col1,col2 = st.columns(2)




with col1:
    with st.expander("رستوران", expanded=True):
        st.image("https://cdn01.booking.ir/2023/7/166ad996-16b4-40dc-bb49-3908bf815f7c.jpg")
        st.caption("""
            رستوران هتل ساحل طلایی
            """)


      


with col2:
  with st.expander("رستوران", expanded=True):
    st.image("https://cdn.alibaba.ir/ostorage/hotel-accommodation-images/2023-09-17/1350cbdf-c515-4673-a9e4-94113a3ada4e.jpg")
    st.caption(
      """
      رستوران هتل ساحل طلایی
      """
    )





















st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
