import streamlit as st
import os
from retriever import retrieve_context
from generator import generate_response
import numpy as np
print(np.__version__)
print(np.array([1, 2, 3]))

st.title("RAG-based Chatbot ")
user_input = st.text_input("Ask your question:")

# Option to select data source
# data_source = st.selectbox("Select Data Source", ("Twitter", "NewsAPI"))

if user_input:
    context = retrieve_context(user_input, "Twitter")
    
    st.write("Retrieved Context:", context)
    
    try:
        response = generate_response(user_input, context)
    except ConnectionError as e:
        response = f"Error loading the model: {e}"
    
    st.write(f"Chatbot: {response}")

