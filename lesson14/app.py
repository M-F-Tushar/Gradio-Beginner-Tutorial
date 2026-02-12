# This app can be deployed online using Gradio's sharing feature or Hugging Face Spaces!
# Use any of your previous app code here.  

import gradio as gr  # Bring in Gradio tools

def greet(name):
    # Make a greeting message
    return f"Hello, {name}!"

# Create the app
app = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs="text",
    title="Deployable Greeting App",
    description="Type your name and see how easy it is to share your app online!"
)

# Start the app
app.launch()
