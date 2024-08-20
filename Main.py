import streamlit as st

tab1,tab2,tab3 = st.tabs(['About','Hobbies','Contacts'])

with tab1:
    col1,col2=st.columns([0.3,0.7])
    with col1:
        st.image("Images/Astral.png", width=200)
        st.subheader('Adith Hegde :poop:')
    with col2:
        st.write('Hi my name is Adith Vinod Hegde.I am a tweleve year old boy who is learning python and streamlit. I am currently in my summer holiday and my birthday is february 29th. I have a dog and a rabbit. I also have a very cute little sister. I got second in my swim meet and have a very good grades in my school.')
with tab2:
    st.write('My hobbies are to play video games and swim. I also like to make videogames and code.')
with tab3:
    st.write('You can contact me at vin.chinnu@gmail.com')
    st.write('You can also look at my youtube channel at https://www.youtube.com/channel/UCyh81jDd1g6efB7OdCHt7yA')