# This app uses Gradio Blocks for a custom layout!
# Inputs are arranged side by side, and a button triggers the greeting.

import gradio as gr  # Bring in Gradio tools

def greet(name, age):
    return f"Hello, {name}! You are {age} years old." 

with gr.Blocks() as demo: 
    gr.Markdown("# Custom Layout Greeting App")
    with gr.Row():
        name_input = gr.Textbox(label="Your Name")
        age_input = gr.Number(label="Your Age")
    output = gr.Textbox(label="Greeting")
    btn = gr.Button("Submit")

    def on_submit(name, age):
        return greet(name, age)

    btn.click(on_submit, inputs=[name_input, age_input], outputs=output)

demo.launch()
