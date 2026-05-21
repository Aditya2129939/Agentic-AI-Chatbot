import streamlit as st

from rag.graph import graph


st.set_page_config(
    page_title="Agentic RAG Chatbot",
    layout="wide"
)

st.title("Agentic RAG Chatbot")

st.write("PDF + Web Search + DeepEval")


question = st.text_input(
    "Enter your question"
)

use_web = st.checkbox(
    "Use Web Search"
)


if st.button("Submit"):

    if question.strip() == "":
        st.warning("Please enter question")
    else:

        with st.spinner("Processing..."):

            result = graph.invoke(
                {
                    "question": question,
                    "use_web": use_web
                }
            )

        st.subheader("Answer")

        st.write(result["answer"])