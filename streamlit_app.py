import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from base import retrieval
from key import hf_email, hf_pass

st.set_page_config(page_title="🤗💬 HugChat")
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "¿Cuál es tu pregunta?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Generando respuesta..."):
            answer = str(prompt)
            answer = f'"{answer}"'
            response = retrieval(answer) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
