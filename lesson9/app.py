# This app asks for your name and age, and helps you if you make a mistake!
# It shows friendly messages for missing or wrong inputs.

import gradio as gr  # Bring in Gradio tools

def check_inputs(name, age):
    # Check if name is empty
    if not name:
        return "Please type your name."
    # Check if age is negative
    if age < 0:
        return "Age cannot be negative. Please enter a positive number."
    # If everything is okay, greet the user
    return f"Hello, {name}! You are {age} years old."

# Create the app with text input and number input
app = gr.Interface(
    fn=check_inputs,
    inputs=[gr.Textbox(label="Your Name"), gr.Number(label="Your Age")],
    outputs="text",
    title="Friendly Greeting App",
    description="Type your name and age. The app will help you if you make a mistake."
)

# Start the app
app.launch()