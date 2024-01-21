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
        st.subheader("Add YouTube URL")
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?", max_chars=100
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?", max_chars=100, key="query"
        )
        st.session_state.openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            key="langchain_search_api_key_openai",
            max_chars=100,
            type="password",
        )
        submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if not youtube_url:
        st.warning("Please provide the YouTube URL.")
    elif not query:
        st.warning("Please provide a query.")
    elif not st.session_state.openai_api_key:
        st.warning("Please add your OpenAI API key to continue.")
    else:
        db = lch.create_db_from_youtube_video_url(
            youtube_url, st.session_state.openai_api_key
        )
        response, docs = lch.get_response_from_query(
            db, query, st.session_state.openai_api_key
        )
        st.subheader("Answer:")
        lines = response.split("\n")

        for line in lines:
            st.text(textwrap.fill(line, width=85))
