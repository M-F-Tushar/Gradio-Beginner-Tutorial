# This app lets users pick between reversing text or making it uppercase!

import gradio as gr  # Bring in Gradio tools

def reverse_text(text): 
    return text[::-1]

def uppercase_text(text):
    return text.upper()

# Function to pick which operation to use
def choose_function(text, operation):
    if operation == "Reverse":
        return reverse_text(text)
    elif operation == "Uppercase":
        return uppercase_text(text)
    else:
        return "Unknown operation."

# Create the app with text input and dropdown for operation
app = gr.Interface(
    fn=choose_function,
    inputs=[
        gr.Textbox(label="Type something"),
        gr.Dropdown(choices=["Reverse", "Uppercase"], label="Choose operation")
    ],
    outputs="text",
    title="Multi-Function Text App",
    description="Type text and pick an operation!"
)

# Start the app
app.launch()
