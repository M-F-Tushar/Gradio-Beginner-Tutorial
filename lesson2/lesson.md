# Lesson 2: Adding User Input to Your Gradio App 

## Friendly Introduction

Welcome back! In the last lesson, your app said "Hello, World!". Now, let’s make your app talk to people. You’ll learn how to let users type something and see a response.

## What You Will Learn
- How to ask the user for input
- How to use that input in your app
- How to show the result

## Real-Life Analogy
Imagine you’re at a pizza shop. The chef asks, “What’s your name?” and then says, “Hello, [your name]!” Your app will do the same!

## Step-by-Step Explanation

### Step 1: Change the Function
We want the app to greet the user by name. So, we need to ask for their name.

### Step 2: Add an Input Box
Gradio lets us add an input box. The user can type their name.

### Full Code

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

app = gr.Interface(fn=greet, inputs="text", outputs="text")
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def greet(name):`: Make a function that takes a name.
- `return f"Hello, {name}!"`: Give back a greeting with the name.
- `app = gr.Interface(fn=greet, inputs="text", outputs="text")`: Build the app. "inputs" is a text box. "outputs" is what the app shows.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box. Type your name and press submit. The app will say hello to you!

---

In the next lesson, we’ll learn how to add more types of input. For now, try greeting yourself and others!
