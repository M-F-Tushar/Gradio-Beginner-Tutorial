# Lesson 17: Saving User Input in Your Gradio App

## Friendly Introduction

Welcome to Lesson 17! Now you’ll learn how to save user input in your Gradio app. Saving input means keeping track of what users type or upload, so you can use it later or remember it.

## What You Will Learn
- How to save user input to a file
- How to use saved input in your app
- Why saving input is useful

## Real-Life Analogy
Imagine you’re keeping a diary. Every day, you write down what happened so you can remember it later. Saving user input is like keeping a diary for your app!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that asks for your name and saves it to a file called `names.txt`. Every time someone types their name, it gets added to the file.

### Step 2: Write the Function to Save Input
We’ll write a function that takes the name and writes it to a file.

### Step 3: Connect the Function to Gradio
We’ll use Gradio to get the name and show a message.

### Full Code

```python
import gradio as gr

def save_name(name):
    # Save the name to a file
    with open("names.txt", "a") as f:
        f.write(name + "\n")
    return f"Thanks, {name}! Your name has been saved."

app = gr.Interface(
    fn=save_name,
    inputs=gr.Textbox(label="Type your name"),
    outputs="text",
    title="Save Name App",
    description="Type your name and it will be saved to a file!"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def save_name(name):`: Function to save the name.
- `with open("names.txt", "a") as f: ...`: Open the file and add the name.
- `app = gr.Interface(...)`: Build the app.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to type your name. The app will save your name to a file and show a thank you message. Check the file `names.txt` to see all the names!

---

In the next lesson, we’ll learn how to use custom layouts to make your app look even better. For now, try saving different names and see how the file grows!