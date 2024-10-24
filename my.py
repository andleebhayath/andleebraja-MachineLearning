from langchain_community.llms import Ollama
import streamlit as st
llm = Ollama(model= "llama3")
st.title("Chatbot using Llama3")
prompt=st.text_area("Enter your Prompt:")
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):

            for response in llm.stream(prompt, stop=['<|eot_id>']):
                st.write(response['text'])

            ----st.write_stream(llm.stream(prompt,stop=['<|eot_id>']))
        
