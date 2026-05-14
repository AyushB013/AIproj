import gradio as gr
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def chat(user_input):
    response = llm.invoke(user_input)
    return response

interface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="My Local AI"
)

interface.launch()