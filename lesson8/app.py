# This app asks for your name, favorite fruit, and if you want a fruit salad!
# It uses radio buttons and a checkbox for choices.

import gradio as gr  # Bring in Gradio tools

def fruit_greeting(name, fruit, salad):
    # Make a message using the name, fruit, and salad choice
    if salad:
        salad_msg = "You want a fruit salad."
    else:
        salad_msg = "You don't want a fruit salad."
    return f"Hello, {name}! Your favorite fruit is {fruit}. {salad_msg}"

# Create the app with text input, radio buttons, and a checkbox
app = gr.Interface(
    fn=fruit_greeting,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Radio(choices=["Apple", "Banana", "Orange", "Grapes"], label="Favorite Fruit"),
        gr.Checkbox(label="Do you want a fruit salad?")
    ],
    outputs="text",
    title="Fruit Choice App",
    description="Type your name, pick your favorite fruit, and choose if you want a fruit salad."
)

# Start the app
app.launch()