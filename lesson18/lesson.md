# Lesson 18: Using Custom Layouts in Your Gradio App
 
## Friendly Introduction

Welcome to Lesson 18! Now you’ll learn how to use custom layouts in your Gradio app. Layouts help you organize your app so it looks neat and is easy to use. You can arrange buttons, inputs, and outputs in different ways.

## What You Will Learn
- How to use Gradio Blocks for custom layouts
- How to arrange inputs and outputs
- How to make your app look professional

## Real-Life Analogy
Imagine you’re arranging furniture in a room. You want everything to be easy to reach and look nice. Custom layouts are like arranging your app’s furniture!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app with two inputs (name and age) and one output. We’ll arrange them side by side using Gradio Blocks.

### Step 2: Use Gradio Blocks
Blocks let you build your app piece by piece and arrange them however you want.

### Full Code

```python
import gradio as gr

def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

with gr.Blocks() as demo:
    gr.Markdown("# Custom Layout Greeting App")
    with gr.Row():
        name_input = gr.Textbox(label="Your Name")
        age_input = gr.Number(label="Your Age")
    output = gr.Textbox(label="Greeting")
    btn = gr.Button("Submit")

    def on_submit(name, age):
        return greet(name, age)

    btn.click(on_submit, inputs=[name_input, age_input], outputs=output)

demo.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def greet(name, age):`: Function to greet the user.
- `with gr.Blocks() as demo:`: Start building a custom layout.
- `gr.Markdown(...)`: Add a title.
- `with gr.Row(): ...`: Arrange inputs side by side.
- `gr.Button(...)`: Add a button.
- `btn.click(...)`: Connect the button to the function.
- `demo.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a neat layout with inputs side by side and a button below. The app will greet you when you press submit!

---

In the next lesson, we’ll learn how to add more advanced interactivity, like updating outputs live. For now, try arranging your app in different ways!
