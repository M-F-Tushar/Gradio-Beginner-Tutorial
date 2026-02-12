# This app asks for your name and lets you pick a number with a slider!

import gradio as gr  # Bring in Gradio tools

def greet_and_number(name, number):
    # Make a message using the name and number
    return f"Hello, {name}! You picked the number {number}."

# Create the app with a text input and a slider
app = gr.Interface(
    fn=greet_and_number,
    inputs=[gr.Textbox(label="Your Name"), gr.Slider(label="Pick a Number", minimum=1, maximum=10)],
    outputs="text"
)

# Start the app
app.launch()