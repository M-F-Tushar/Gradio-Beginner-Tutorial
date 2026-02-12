# Lesson 20: Combining Live Updates with Custom Layouts

## Friendly Introduction

Welcome to Lesson 20! Now you’ll learn how to combine live updates with custom layouts in your Gradio app. This makes your app both beautiful and interactive.

## What You Will Learn
- How to use Gradio Blocks with live updates
- How to arrange inputs and outputs for live interactivity
- How to make your app look and feel professional

## Real-Life Analogy
Imagine a smart dashboard that updates instantly as you change settings. Combining live updates and custom layouts makes your app feel modern and easy to use!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app with a slider and a number input, arranged side by side. The app will show the sum live as you change the values.

### Step 2: Use Gradio Blocks and Live Feature
We’ll use Blocks for layout and set live updates for instant feedback.

### Full Code

```python
import gradio as gr

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
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def add_values(slider_value, number_value):`: Function to add values.
- `with gr.Blocks() as demo:`: Start custom layout.
- `gr.Slider(...)` and `gr.Number(...)`: Inputs arranged side by side.
- `output = gr.Textbox(...)`: Output box for the sum.
- `slider.change(...)` and `number.change(...)`: Update output live as values change.
- `demo.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a slider and a number input side by side. As you change either, the sum updates instantly. The app looks neat and feels fast!

---

Congratulations! You now know how to combine live updates and custom layouts for a modern Gradio app. Try adding more inputs or outputs and see what you can build!