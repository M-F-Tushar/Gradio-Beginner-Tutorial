# This app asks for your name and age, then tells you how old you'll be next year!

import gradio as gr  # Bring in Gradio tools

def greet_and_age(name, age):
    # Add 1 to the age to find out next year's age
    next_year = age + 1
    # Make a message using the name and next year's age
    return f"Hello, {name}! Next year, you will be {next_year} years old."

# Create the app with two input boxes: one for name, one for age
app = gr.Interface(
    fn=greet_and_age,
    inputs=[gr.Textbox(label="Your Name"), gr.Number(label="Your Age")],
    outputs="text"
)

# Start the app
app.launch()