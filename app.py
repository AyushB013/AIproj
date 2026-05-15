import gradio as gr
from main import chat
with gr.Blocks() as demo:
    gr.Markdown("# The Local AI")
    gr.Markdown("Powered by Ollama + Gradio")
    chatbot = gr.ChatInterface(fn=chat, title="The Local AI")
demo.launch(css_paths="styles.css")