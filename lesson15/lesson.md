# Lesson 15: Adding Custom Functions to Your Gradio App

## Friendly Introduction

Welcome to Lesson 15! Now you’ll learn how to add your own custom functions to your Gradio app. Custom functions let you make your app do anything you want—like math, text changes, or even fun games.

## What You Will Learn
- What a custom function is
- How to write your own function
- How to connect it to Gradio

## Real-Life Analogy
Imagine your app is a magic box. You can put any recipe (function) inside, and the box will follow your instructions. Custom functions are your recipes!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that reverses any text the user types. This is a simple custom function.

### Step 2: Write the Custom Function
We’ll write a function that takes text and returns it backwards.

### Step 3: Connect the Function to Gradio
We’ll use Gradio to show the result.

### Full Code

```python
import gradio as gr

def reverse_text(text):
    # Reverse the text
    return text[::-1]

app = gr.Interface(
    fn=reverse_text,
    inputs=gr.Textbox(label="Type something"),
    outputs="text",
    title="Reverse Text App",
    description="Type any text and see it backwards!"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def reverse_text(text):`: Make a custom function to reverse text.
- `return text[::-1]`: Return the text backwards.
- `app = gr.Interface(...)`: Build the app with a text input and text output.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to type text. The app will show your text backwards. Try different words and see what happens!

---

In the next lesson, we’ll learn how to add more than one function and let users pick which one to use. For now, try making your own custom functions!