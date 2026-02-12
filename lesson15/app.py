# This app uses a custom function to reverse any text you type!

import gradio as gr  # Bring in Gradio tools 

def reverse_text(text):
    # Reverse the text
    return text[::-1]

# Create the app with a text input and text output
app = gr.Interface(
    fn=reverse_text,
    inputs=gr.Textbox(label="Type something"),
    outputs="text",
    title="Reverse Text App",
    description="Type any text and see it backwards!"
)

# Start the app
app.launch()
