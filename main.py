from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
def chat(message, history):
    try:
        response = llm.invoke(message)
        return response
    except Exception as e:
        return f"Error: {str(e)}"