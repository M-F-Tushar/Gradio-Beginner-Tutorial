# This app greets the user and uses a custom theme!
# Try changing the theme to see different styles.

import gradio as gr  # Bring in Gradio tools

def greet(name):
    # Make a greeting message
    return f"Hello, {name}!"

# Create the app with a theme
app = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs="text",
    title="Themed Greeting App",
    description="Type your name and see the app in different themes!",
    theme="soft"
)

# Start the app
app.launch()