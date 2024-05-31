
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from streamlit_option_menu import option_menu
from jdatetime import datetime
import hydralit_components as hc

st.set_page_config(
        page_title="هتل ساحل طلایی قشم",
        page_icon="img/logo.png",
        initial_sidebar_state='collapsed',
        layout='wide',
    )



with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

# st.snow()
# st.image("logo.png")


now = datetime.now()
tim = now.strftime("%Y/%m/%d")

# col1,col2 = st.columns(2)

# with col1:





menu_data = [

    
    {'id':'home','icon': "🏚", 'label':"صفحه اصلی",},

    {"id": "room", "icon": "", "label": "اتاق ها"},
    {'id':'cafe','icon':"",'label':"کافی شاب"},
    {'id':'resturan','icon': "", 'label':"رستوران"},
    {'id':'marasem','icon': "", 'label':"مراسمات"},
    {'id':'sahel','icon': "", 'label':"ساحل"},
    {'id':'soal','icon': "", 'label':"سوالات"},
    
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    
    
#     home_name='Home',
#     login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned

)



# st.info(f"{menu_id}")



if menu_id == "room":

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













if menu_id == "home":
  
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

    st.write("تاریخ امروز :", tim)
    st.caption("""
          مشخصات خودتان , تعداد نفرات , تاریخ ورود و خروج را توی واتساپ 💬 ارسال کنید
    """)
          
    st.divider()
    
          
    c1,c2 = st.columns(2)
    phone_number = "+989025342900"
    with c1:
      # st.markdown(f'<a href="tel:{phone_number}">{phone_number}</a>', unsafe_allow_html=True)
      st.markdown("[شمار ه تماس](tel:989025342900)")
      st.divider()
      
      

    with c2:
      
      st.markdown("[واتساپ 💬](http://wa.me/989025342900)")

      st.divider()

    with c1:

      st.markdown("[تلگرام ](https://t.me/goldenbeach_hotel)")
      st.divider()

    with c2:     
      st.markdown("[اینستاگرام ](https://instagram.com/goldenbeach_hotel)")

  # with col2:
    # st.subheader("هتل ساحل طلایی قشم")



  elif selected == "قیمت اتاق ها":
    st.success("در حال بروزرسانی قیمت ها")   
    # st.image("img/n.png")


  # st.divider()
  elif selected == "صفحه اصلی":

    col1,col2 = st.columns(2)

    with col1:
       
      st.subheader("هتل ساحل طلایی قشم")

    with col2:
      st.image("img/logo.png",width=100)

       
    with st.expander("هتل ساحل طلایی", expanded=True):
      st.image("img/pass.jpg")
    
      st.caption("""
    
    هتل ساحل طلایی در 11 کیلومتری قشم است. این هتل قبل‌ها به ساحل سیمین یا پلاژ سیمین معروف بوده. هتل ساحل طلایی از همه نظر هتلی بی‌نظیر در قشم است و طیف گسترده‌ای از خدمات و امکانات را در اختیار مسافران قرار می‌دهد. ساحل اختصاصی هتل بسیار تمیز و خلوت است  علاوه بر این‌ها مسافران می‌توانند لذت ماهیگیری  را در اسکله‌ی تفریحی هتل تجربه کنند.  هتل ساحل طلایی  چند نوع واحد اقامتی دارد: سوئیت و اتاق معمولی،سوئیتهای وی آی پی، دوبلکس دوطبقه   هم دارند. رستوران ساحلی دوطبقه با نمای رو به دریا و آلاچیق‌های چوبی کنار ساحل همواره برای مسافران خاطرات خوشی رقم زده. هتل ساحل طلایی در جاده‌ی ساحلی جنوبی و در کنار زیارتگاه شاه شهید واقع شده. این هتل کمتر از ۲۰ دقیقه با یکی از جاذبه‌های شگفت‌انگیز قشم فاصله دارد. دره‌ی ستاره‌ها با قدمتی دو میلیون ساله، یکی از جاذبه‌های طبیعی قشم است که صحبت از آن همیشه با داستان‌ها و گاهی خرافه‌های جالبی همراه بوده. اقامت در هتل ساحل طلایی و بازدید از این نقاط دیدنی می‌تواند بدل به یکی از بهترین تجربیات مسافران قشم شود.
    
    
    """
    
    
    )







if menu_id == "cafe":


  st.header("🍫  کافی شاپ ساحل طلایی")






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











if menu_id == "resturan":


  st.header("👨🏻‍🍳 رستوران ساحل طلایی 👨🏻‍🍳")


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





if menu_id == "sahel":


  st.header("ساحل 🌊 ساحل طلایی 🌊")





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


















if menu_id == "marasem":
   



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





if menu_id == "soal":
   

  st.header("❓ سوالات ❓")

  option = st.radio(
    """
    روی گزینه سوالات کلیک کنید
    """
    ,
    ("""اتاق ها رو به دریا هستند ؟ 🏠""",
    """آیا پارکینگ دارد ؟ 🅿️""",
    """رستوران چه ساعتی باز میشه ؟ 👨🏽‍🍳""",
    """کافی شاپ چه ساعتی باز میشه ؟ ☕""",
    """آیا آلاچیق هم وجود دارد ؟ 🛖""",
    """تور گردشگری هم دارید ؟ 🚕""",
    """آدرس هتل شما کجاست ؟ 📍""",
    """اتاق ها چند خوابه هستند ؟ ⛪️""",
    
    )
  )

  st.divider()
  # Display the selected option
  if option == "اتاق ها رو به دریا هستند ؟ 🏠":
    st.write("""
    بله ! تمامی اتاق ها رو به دریا هستند 🏠
    """)


  elif option == "آیا پارکینگ دارد ؟ 🅿️":
    st.write("بله ! پارکینگ وجود دارد 🅿️")



  elif option == "رستوران چه ساعتی باز میشه ؟ 👨🏽‍🍳":
    st.write("""
              👨🏽‍🍳
    رستوران برای صبحانه 8 الی 9:30
    و برای ناهار ساعت 13 الی 15:30
    و برای شام 20:30 الی 23:00
    باز است

    """)

  elif option == "کافی شاپ چه ساعتی باز میشه ؟ ☕":
    st.write("""
    کافی شاپ صبح 11 الی 13 باز است و عصر از ساعت 16 الی 23 باز است ☕
    """)


  elif option == "آیا آلاچیق هم وجود دارد ؟ 🛖":
    st.write("بله آلاچیق های کولردار و بدون کولر لب ساحل قرار دارد که میتونید صدای امواج دریا را گوش کنید 🛖")


  elif option == "تور گردشگری هم دارید ؟ 🚕":
    st.write("بله , تور گردشگری داریم 🚕")

  elif option == "آدرس هتل شما کجاست ؟ 📍":
    st.write("""
    جزیره قشم - جاده ساحل جنوبی , رمچاه ( روبروی زیارتگاه شاه شهید و غار خربس ) 📍
    هتل ساحل طلایی قشم

    """)



  elif option == "اتاق ها چند خوابه هستند ؟ ⛪️":
    st.write("""
    ⛪️  این هتل دارای { اتاق های یک خوابه 4 تخته ,  اتاق های 3 تخته , دو خوابه 6 تخته , یک خوابه 5 تخته , دوبلکس 8 تخته , دوبلکس 6 تخته } ⛪️
  """)












st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
