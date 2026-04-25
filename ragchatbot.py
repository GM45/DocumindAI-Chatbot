from multiprocessing import context

import pdfplumber
import streamlit as st
from click import prompt
from langchain_classic.chains import llm
from langchain_classic.tools import retriever
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = "Enter the OpenAI API key here"
st.header("Glenn's Chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload a PDF file and start asking your questions", type="PDF")

#Extract contents from the PDF and chunk it

if file is not None:
    #extract text from it
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text = text + page.extract_text() + "\n"
    #st.write(text)

    #Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n","\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    #generate embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key = OPENAI_API_KEY

    )

    #store embeddings in vector db
    vector_store = FAISS.from_texts(chunks,embeddings)

    #get user question
    user_question = st.text_input("Type your question here")
    #question -> embeddings -> similarity search -> results to LLM -> response(CHAIN)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k":4}
    )

    #define the LLM and Prompts
    llm = ChatOpenAI(
        model ="gpt-4o-mini",
        temperature=0.3,
        max_tokens=1000,
        openai_api_key=OPENAI_API_KEY
    )

    #provide the prompts
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistant answering questions about a PDF document. \n\n"
         "Guidelines:\n"
         "1.Provide complete, well-explained answers using the context below.\n"
         "2.Include relevant details, numbers, explanations to give a thorough response.\n"
         "3.If the context mentions related information, include it to give fuller picture.\n"
         "4.Only use information from the provided context - do not use outside knowledge.\n"
         "5.Summarize long information,ideally in bullets where needed\n"
         "6.If the information is not in the context, say so politely.\n\n"
         "Context:\n{context}"),
        ("human","{question}")
    ])

    chain = (
            {"context":retriever | format_docs, "question": RunnablePassthrough()}
            | prompt()
            | llm
            | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)

    #generate answer

