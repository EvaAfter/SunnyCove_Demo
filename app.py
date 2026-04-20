import gradio as gr

def greet(name):
    return f"Hello {name}! Welcome to SunnyCove 🌞"

iface = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text"
)

iface.launch()
