
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from streamlit_option_menu import option_menu


st.set_page_config(
        page_title="هتل ساحل طلایی قشم",
        page_icon="img/logo.png",
    )



with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.snow()
# st.image("logo.png")



# col1,col2 = st.columns(2)

# with col1:
st.image("img/logo.png")

  
selected = option_menu (
    menu_title=None,
    options=[ "جهت رزرو" , "قیمت اتاق ها" , "صفحه اصلی"],
    icons=["phone","book","house" ],
    menu_icon="cast",
    default_index=2,
    orientation="horizontal",
    styles={


          "nav-link":{
              'font-family': 'Courier New' 'Courier' 'monospace'
          },

      }
  )

if selected == "جهت رزرو":

  

  c1,c2 = st.columns(2)
  
  with c1:
    
    st.caption("""
        مشخصات خودتان , تعداد نفرات , تاریخ ورود و خروج را توی واتساپ 💬 ارسال کنید
  """)
    st.divider()
    

  with c2:
    
    st.markdown("[واتساپ 💬](http://wa.me/989025342900)")
    st.divider()
    st.markdown("[تلگرام ](https://t.me/goldenbeach_hotel)")
    st.divider()
    st.markdown("[اینستاگرام ](https://instagram.com/goldenbeach_hotel)")

# with col2:
  # st.subheader("هتل ساحل طلایی قشم")



elif selected == "قیمت اتاق ها":
  st.image("img/n.png")


# st.divider()
elif selected == "صفحه اصلی":
  
  st.subheader("هتل ساحل طلایی قشم")
  with st.expander("هتل ساحل طلایی", expanded=True):
    st.image("img/pass.jpg")
  
    st.caption("""
  
  هتل ساحل طلایی در 11 کیلومتری قشم است. این هتل قبل‌ها به ساحل سیمین یا پلاژ سیمین معروف بوده. هتل ساحل طلایی از همه نظر هتلی بی‌نظیر در قشم است و طیف گسترده‌ای از خدمات و امکانات را در اختیار مسافران قرار می‌دهد. ساحل اختصاصی هتل بسیار تمیز و خلوت است  علاوه بر این‌ها مسافران می‌توانند لذت ماهیگیری  را در اسکله‌ی تفریحی هتل تجربه کنند.  هتل ساحل طلایی  چند نوع واحد اقامتی دارد: سوئیت و اتاق معمولی،سوئیتهای وی آی پی، دوبلکس دوطبقه   هم دارند. رستوران ساحلی دوطبقه با نمای رو به دریا و آلاچیق‌های چوبی کنار ساحل همواره برای مسافران خاطرات خوشی رقم زده. هتل ساحل طلایی در جاده‌ی ساحلی جنوبی و در کنار زیارتگاه شاه شهید واقع شده. این هتل کمتر از ۲۰ دقیقه با یکی از جاذبه‌های شگفت‌انگیز قشم فاصله دارد. دره‌ی ستاره‌ها با قدمتی دو میلیون ساله، یکی از جاذبه‌های طبیعی قشم است که صحبت از آن همیشه با داستان‌ها و گاهی خرافه‌های جالبی همراه بوده. اقامت در هتل ساحل طلایی و بازدید از این نقاط دیدنی می‌تواند بدل به یکی از بهترین تجربیات مسافران قشم شود.
  
  
  """
  
  
  )







show_pages(

    [
        
        Page("main.py", "صفحه اصلی", "🏠"),
        Page("page/sahel.py", "ساحل", "🌊"),
        Page("page/res.py", "رستوران", "👨🏻‍🍳"),
        Page("page/room.py", "اتاق ها", "⛪️"),
        Page("page/cafe.py", "کافی شاب", "🍫"),
        Page("page/marasem.py", "مراسمات", "🌈"),
        Page("page/soal.py", "سوالات", "؟"),


    ]

)












st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
