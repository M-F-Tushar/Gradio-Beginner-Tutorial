# This app has two pages: one for text files and one for images! 
# It uses Gradio Tabs for organization.

import gradio as gr  # Bring in Gradio tools

def show_text_file(file):
    # Read the text file and show its content
    if file is None:
        return "No file uploaded."
    content = file.read().decode("utf-8")
    return content

def show_image_file(image):
    # Just return the image
    return image

# Create two pages (Tabs) for the app
with gr.Tab("Text File"):
    text_interface = gr.Interface(
        fn=show_text_file,
        inputs=gr.File(label="Upload a Text File"),
        outputs="text",
        title="Show Text File Content"
    )

with gr.Tab("Image File"):
    image_interface = gr.Interface(
        fn=show_image_file,
        inputs=gr.Image(label="Upload an Image"),
        outputs=gr.Image(label="Here is your Image"),
        title="Show Image File"
    )

# Combine the pages and launch the app
gr.TabbedInterface([text_interface, image_interface], ["Text File", "Image File"]).launch()
