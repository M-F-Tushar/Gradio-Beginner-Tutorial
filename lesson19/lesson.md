# Lesson 19: Adding Live Interactivity to Your Gradio App

## Friendly Introduction

Welcome to Lesson 19! Now you’ll learn how to make your Gradio app update outputs live, without needing to press a button. Live interactivity makes your app feel fast and responsive.

## What You Will Learn
- How to use Gradio’s live feature
- How to update outputs instantly
- How to make your app more interactive

## Real-Life Analogy
Imagine a calculator that shows the answer as soon as you type numbers, without pressing "equals." Live interactivity is like magic—your app responds right away!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that adds two numbers and shows the result instantly as you type.

### Step 2: Use Gradio’s Live Feature
We’ll set `live=True` in the app so it updates automatically.

### Full Code

```python
import gradio as gr

def add_numbers(a, b):
    return f"The sum is: {a + b}"

app = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(label="First Number"), gr.Number(label="Second Number")],
    outputs="text",
    title="Live Addition App",
    description="Type two numbers and see the sum instantly!",
    live=True
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def add_numbers(a, b):`: Function to add two numbers.
- `live=True`: Makes the app update instantly as you type.
- `app = gr.Interface(...)`: Build the app.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see two boxes for numbers. As you type, the app shows the sum instantly—no need to press submit!

---

In the next lesson, we’ll learn how to add even more custom features, like using sliders, images, or combining live updates with custom layouts. For now, try making your app interactive with live updates!