# Lesson 16: Letting Users Pick Between Multiple Functions

## Friendly Introduction

Welcome to Lesson 16! Now you’ll learn how to let users pick which function they want to use in your Gradio app. This makes your app more flexible and fun—like a toolbox with many tools!

## What You Will Learn
- How to add multiple functions to your app
- How to let users choose which function to use
- How to organize your app for easy use

## Real-Life Analogy
Imagine you have a toolbox. Sometimes you need a hammer, sometimes a screwdriver. Your app can offer different tools (functions) for different jobs!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app with two functions:
- One reverses text
- One changes text to uppercase
The user can pick which function to use.

### Step 2: Write the Functions
We’ll write two functions: one for reversing text, one for making text uppercase.

### Step 3: Use Gradio’s Dropdown or Radio to Let Users Choose
We’ll use a dropdown so the user can pick which function to use.

### Full Code

```python
import gradio as gr

def reverse_text(text):
    return text[::-1]

def uppercase_text(text):
    return text.upper()

# Function to pick which operation to use
def choose_function(text, operation):
    if operation == "Reverse":
        return reverse_text(text)
    elif operation == "Uppercase":
        return uppercase_text(text)
    else:
        return "Unknown operation."

app = gr.Interface(
    fn=choose_function,
    inputs=[
        gr.Textbox(label="Type something"),
        gr.Dropdown(choices=["Reverse", "Uppercase"], label="Choose operation")
    ],
    outputs="text",
    title="Multi-Function Text App",
    description="Type text and pick an operation!"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def reverse_text(text):`: Function to reverse text.
- `def uppercase_text(text):`: Function to make text uppercase.
- `def choose_function(text, operation):`: Function to pick which operation to use.
- `gr.Textbox(...)`: Input for text.
- `gr.Dropdown(...)`: Input for choosing the operation.
- `app = gr.Interface(...)`: Build the app.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to type text and a dropdown to pick an operation. The app will show the result based on your choice!

---

In the next lesson, we’ll learn how to add even more advanced features, like saving user input or using custom layouts. For now, try making your own multi-function apps!