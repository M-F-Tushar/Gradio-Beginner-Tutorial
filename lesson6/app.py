# This app asks for your name and favorite color, then greets you!
# It also has a title and description to look nice.

import gradio as gr  # Bring in Gradio tools

def greet_with_color(name, color):
    # Make a message using the name and color
    return f"Hello, {name}! Your favorite color is {color}."

# Create the app with a text input, dropdown, title, and description
app = gr.Interface(
    fn=greet_with_color,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Dropdown(choices=["Red", "Blue", "Green", "Yellow"], label="Favorite Color")
    ],
    outputs="text",
    title="Color Greeting App",
    description="Type your name and pick your favorite color. The app will greet you!"
)

# Start the app
app.launch()