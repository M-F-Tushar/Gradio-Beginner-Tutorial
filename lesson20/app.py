# This app combines live updates with a custom layout using Gradio Blocks!
# The sum updates instantly as you change the slider or number input.

import gradio as gr  # Bring in Gradio tools

def add_values(slider_value, number_value):
    return f"The sum is: {slider_value + number_value}"

with gr.Blocks() as demo:
    gr.Markdown("# Live Layout Addition App")
    with gr.Row():
        slider = gr.Slider(label="Pick a number", minimum=0, maximum=100, value=50)
        number = gr.Number(label="Type a number", value=0)
    output = gr.Textbox(label="Sum")

    def update_sum(slider_value, number_value):
        return add_values(slider_value, number_value)

    slider.change(update_sum, inputs=[slider, number], outputs=output, queue=False)
    number.change(update_sum, inputs=[slider, number], outputs=output, queue=False)

demo.launch()