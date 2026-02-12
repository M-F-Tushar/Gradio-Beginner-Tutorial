# This app adds two numbers and updates the sum live as you type!

import gradio as gr  # Bring in Gradio tools

def add_numbers(a, b):
    return f"The sum is: {a + b}" 

# Create the app with two number inputs and live updates
app = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(label="First Number"), gr.Number(label="Second Number")],
    outputs="text",
    title="Live Addition App",
    description="Type two numbers and see the sum instantly!",
    live=True
)

# Start the app
app.launch()
