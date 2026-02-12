# This app lets you upload an image and shows it back to you!

import gradio as gr  # Bring in Gradio tools

def show_image(image):
    # Just return the image as it is
    return image

# Create the app with an image input and output
app = gr.Interface(
    fn=show_image,
    inputs=gr.Image(label="Upload an Image"),
    outputs=gr.Image(label="Here is your Image")
)

# Start the app
app.launch()