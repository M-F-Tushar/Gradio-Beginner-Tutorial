# This app saves user names to a file called names.txt!

import gradio as gr  # Bring in Gradio tools

def save_name(name): 
    # Save the name to a file
    with open("names.txt", "a") as f:
        f.write(name + "\n")
    return f"Thanks, {name}! Your name has been saved."

# Create the app with a text input
app = gr.Interface(
    fn=save_name, 
    inputs=gr.Textbox(label="Type your name"),
    outputs="text",
    title="Save Name App",
    description="Type your name and it will be saved to a file!"
)

# Start the app
app.launch()
