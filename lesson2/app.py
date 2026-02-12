# This app asks for your name and greets you!

import gradio as gr  # Bring in Gradio tools

def greet(name):
    # This function takes the user's name and returns a greeting 
    return f"Hello, {name}!"

# Create the app with a text input box
app = gr.Interface(fn=greet, inputs="text", outputs="text")

# Start the app
app.launch()
