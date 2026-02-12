# This app connects to a simple machine learning model!
# The model checks if a number is big or small.

import gradio as gr  # Bring in Gradio tools

def simple_model(number):
    # The model checks if the number is big or small
    if number > 10:
        return "Big"
    else:
        return "Small"

# Create the app with a number input and text output
app = gr.Interface(
    fn=simple_model,
    inputs=gr.Number(label="Enter a Number"),
    outputs="text",
    title="Simple Model App",
    description="Type a number and see if the model thinks it is big or small."
)

# Start the app
app.launch()