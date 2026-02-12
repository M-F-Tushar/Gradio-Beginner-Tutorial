# Lesson 5: Using Sliders and Controls in Your Gradio App

## Friendly Introduction

Welcome to Lesson 5! You’ve learned how to use text, numbers, and images. Now, let’s make your app interactive with sliders. Sliders let users pick a value by moving a bar. This is great for things like volume, brightness, or choosing a number easily.

## What You Will Learn
- How to add a slider to your app
- How to use the slider value in your function
- How to combine sliders with other inputs

## Real-Life Analogy
Think of a slider like the volume knob on a radio. You turn it up or down to pick the sound level you want. In your app, a slider lets the user pick a number by sliding left or right.

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that asks for your name and lets you pick a number with a slider. The app will greet you and tell you the number you picked.

### Step 2: Change the Function
We need a function that takes a name and a number from the slider. The function will use both to make a message.

### Step 3: Add a Slider Input
Gradio lets us use a slider input. The user can slide to pick a number.

### Full Code

```python
import gradio as gr

def greet_and_number(name, number):
    # Make a message using the name and number
    return f"Hello, {name}! You picked the number {number}."

app = gr.Interface(
    fn=greet_and_number,
    inputs=[gr.Textbox(label="Your Name"), gr.Slider(label="Pick a Number", minimum=1, maximum=10)],
    outputs="text"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def greet_and_number(name, number):`: Make a function that takes a name and a number.
- `return f"Hello, {name}! You picked the number {number}."`: Make a message using the name and the number.
- `app = gr.Interface(...)`: Build the app.
    - `gr.Textbox(label="Your Name")`: A box for typing your name.
    - `gr.Slider(label="Pick a Number", minimum=1, maximum=10)`: A slider for picking a number from 1 to 10.
- `outputs="text"`: The app will show a text message.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box for your name and a slider for picking a number. Type your name, slide to pick a number, and press submit. The app will greet you and tell you the number you picked!

---

In the next lesson, we’ll learn how to make your app look nicer and organize the layout. For now, try using the slider and see how it works!