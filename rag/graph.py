from typing import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END

from rag.retriever import retriever
from rag.websearch import web_search
from rag.evaluator import evaluate_response
from dotenv import load_dotenv

load_dotenv()
import os
import openai

from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)


# =========================
# STATE
# =========================

class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    use_web: bool


# =========================
# PDF RETRIEVAL
# =========================

def retrieve(state):

    print("\n Using PDF Retrieval...\n")

    docs = retriever.invoke(state["question"])

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "context": context
    }


# =========================
# WEB SEARCH
# =========================

def search_web(state):

    print("\n Using Web Search...\n")

    web_result = web_search(state["question"])

    return {
        "context": web_result
    }


# =========================
# GENERATE ANSWER
# =========================

def generate(state):

    print("\n Generating Answer...\n")

    prompt = f"""
You are an intelligent AI assistant.

Answer the user question using ONLY the provided context.

If answer is not available in context,
say:
"I could not find relevant information."

========================

Context:
{state['context']}

========================

Question:
{state['question']}

========================

Answer:
"""

    try:
        response = llm.invoke(prompt)

        return {
            "answer": response.content
        }

    except Exception as e:
        # Log the error for debugging
        print("LLM invocation error:", e)

        # Friendly handling for quota / rate-limit errors
        err_text = str(e).lower()
        if "insufficient_quota" in err_text or "quota" in err_text or "429" in err_text:
            return {
                "answer": (
                    "OpenAI quota exceeded or rate limited. "
                    "Please check your OpenAI billing/plan or set a different OPENAI_API_KEY in your .env."
                )
            }

        # Generic fallback message
        return {
            "answer": f"LLM error: {e}. Check logs for details."
        }


# =========================
# EVALUATE RESPONSE
# =========================

def evaluate(state):

    print("\n Evaluating Answer...\n")

    result = evaluate_response(
        question=state["question"],
        answer=state["answer"],
        context=state["context"]
    )

    print("Evaluation Result:", result)

    faithfulness = result["faithfulness"]
    relevancy = result["relevancy"]

    print("Faithfulness:", faithfulness)
    print("Relevancy:", relevancy)

    # If score is low → regenerate
    if faithfulness < 0.80 or relevancy < 0.80:

        print("\n Low score detected. Regenerating...\n")

        return "regenerate"

    print("\n Good Answer\n")

    return "good"


# =========================
# ROUTER
# =========================

def router(state):

    """
    Decide whether to use:
    - PDF Retrieval
    - Web Search
    """

    if state["use_web"]:

        print("\n Routing to WEB SEARCH\n")

        return "web"

    print("\n Routing to PDF RAG\n")

    return "pdf"


# =========================
# BUILD GRAPH
# =========================

workflow = StateGraph(AgentState)


# Nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("search_web", search_web)
workflow.add_node("generate", generate)


# =========================
# CONDITIONAL ENTRY POINT
# =========================

workflow.set_conditional_entry_point(
    router,
    {
        "pdf": "retrieve",
        "web": "search_web"
    }
)


# =========================
# EDGES
# =========================

workflow.add_edge("retrieve", "generate")

workflow.add_edge("search_web", "generate")


# =========================
# CONDITIONAL EVALUATION
# =========================

workflow.add_conditional_edges(
    "generate",
    evaluate,
    {
        "good": END,
        "regenerate": "generate"
    }
)


# =========================
# COMPILE GRAPH
# =========================

graph = workflow.compile()


print("\n Agentic RAG Graph Ready\n")