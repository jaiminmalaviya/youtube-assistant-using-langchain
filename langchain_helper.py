from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def create_db_from_youtube_video_url(video_url: str, openai_api_key) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=20)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db


def get_response_from_query(db, query, openai_api_key, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = ChatOpenAI(openai_api_key=openai_api_key)

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".

        give the answer in correct format, if it required bullet points then use the bullet points, and also add "\n" where break line is needed.

        give the all answer within 100 words and must use hierarchical bullet points. also must add "\n" after every bullet point.
        """,
    )

    chain = prompt | llm

    response = chain.invoke({"question": query, "docs": docs_page_content})
    response = response.content
    return response, docs
