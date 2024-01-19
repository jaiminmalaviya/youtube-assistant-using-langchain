import streamlit as st
import langchain_helper as lch
import textwrap

st.set_page_config(
    page_title="YouTube Assistant App",
    page_icon="📺",
    initial_sidebar_state="expanded",
)

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?", max_chars=100
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?", max_chars=100, key="query"
        )
        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    lines = response.split("\n")

    for line in lines:
        st.text(textwrap.fill(line, width=85))
