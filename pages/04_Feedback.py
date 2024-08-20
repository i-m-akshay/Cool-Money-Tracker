from altair.utils.schemapi import _subset_to_most_specific_json_paths
import streamlit as st
import pandas as pd
import os

folder_path = "data"
excel_file_path = "data/feedback.csv"
if not os.path.exists(folder_path):
  os.makedirs(folder_path)
if not os.path.exists(excel_file_path):
  dataframe = pd.DataFrame(columns=["Name", "Feedback", "Rating"])
  dataframe.to_csv(excel_file_path, index=False)


def clear():
  st.session_state.nam = ""
  st.session_state.fed = ""
  st.session_state.rat = 0


name = st.text_input("Enter Your Name", key="nam")
feedback = st.text_input("Enter Your Feedback", key="fed")
rating = st.slider('Please enter your rating',
                   min_value=1,
                   max_value=5,
                   step=1,
                   value=1)
emoji_holder = st.empty()
if rating == 1:
  emoji_holder.subheader('We will defenitly improve' + ':weary:')
if rating == 2:
  emoji_holder.subheader('We will defenitly improve your experience' +
                         ':disappointed_relieved:')
if rating == 3:
  emoji_holder.subheader('Thanks' + ':persevere:')
if rating == 4:
  emoji_holder.subheader('Oh you are loving it!!!' + ':smiley_cat:')
if rating == 5:
  emoji_holder.subheader('Thank you so much for your love' +
                         ':heart_eyes_cat:')
col1,col2 = st.columns([0.1624,0.9])
with col1:
  submit = st.button('Submit :smile:')
with col2:
  Clear = st.button('Clear :scissors:', on_click=clear)
def insert(path):
  dataframe = pd.read_csv(excel_file_path)
  lenght = len(dataframe)
  dataframe.loc[lenght] = [name, feedback, rating]
  dataframe.to_csv(excel_file_path, index = False)
def view(path):
  dataframe = pd.read_csv(excel_file_path)
  st.dataframe(dataframe)
if submit:
  insert(excel_file_path)
  st.success('Thank you for your valuable feedback')
st.subheader('Past Feedbacks')
view(excel_file_path)