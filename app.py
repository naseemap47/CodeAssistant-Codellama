import streamlit as st
from langchain_ollama import ChatOllama


st.title("👨‍💻 Code Assistant - Codellama")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hi, I'm a code assistant. How can I help you ?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:=st.chat_input(placeholder="Write a python code for binary search"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    # LLM - Codellama
    llm = ChatOllama(model='codellama:7b')

    with st.spinner('Thinking...'):
        # st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        # response = llm.invoke(st.session_state.messages, callbacks=[st_cb])
        response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append({"role":"assistant", "content":response.content})
        st.markdown(response.content)
        # print(response.content)