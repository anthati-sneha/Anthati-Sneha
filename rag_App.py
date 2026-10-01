import chromadb
import streamlit as st
from ollama import chat 
from sentence_transformers import SentenceTransformer
st.set_page_config(page_title="Technova Concierge",page_icon=".",layout="wide")
@st.cache_resource
def load_resources():
    model=SentenceTransformer('all-MiniLM-L6-V2')
    client=chromadb.PersistentClient(path="chroma_db")
    collection=client.get_or_create_collection("fest_docs")
    return model,collection
model,collection=load_resources()
st.title("Nova, the Technova Conceirge")
st.caption("I only know the fest documents.Ask me anything about Technova!")