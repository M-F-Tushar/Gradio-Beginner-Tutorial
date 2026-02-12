# Lesson 7: Saving and Sharing Your Gradio App

## Friendly Introduction

Welcome to Lesson 7! You’ve made your app look nice and organized. Now, let’s learn how to save your app and share it with others. Sharing is important—your friends, family, or anyone can use your app!

## What You Will Learn
- How to save your app code
- How to run your app for others to see
- How to share your app online

## Real-Life Analogy
Think of your app like a drawing. You can keep it for yourself, or you can show it to others. Saving your app is like putting your drawing in a folder. Sharing is like showing your drawing to your friends.

## Step-by-Step Explanation

### Step 1: Save Your App Code
Make sure your app code is saved in a file, like `app.py`. This keeps your work safe.

### Step 2: Run Your App
To run your app, open a terminal and type:

```
python app.py
```

This starts your app. You’ll see a link in the terminal. Click it to open your app in a web browser.

### Step 3: Share Your App Online
Gradio can help you share your app online. When you run your app, Gradio gives you a link that starts with `https://`. You can copy this link and send it to anyone. They can use your app from anywhere!

### Full Code Example

Let’s use the app from Lesson 6:

```python
import gradio as gr

def greet_with_color(name, color):
    return f"Hello, {name}! Your favorite color is {color}."

app = gr.Interface(
    fn=greet_with_color,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Dropdown(choices=["Red", "Blue", "Green", "Yellow"], label="Favorite Color")
    ],
    outputs="text",
    title="Color Greeting App",
    description="Type your name and pick your favorite color. The app will greet you!"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def greet_with_color(name, color):`: Make a function that takes a name and a color.
- `return f"Hello, {name}! Your favorite color is {color}."`: Make a message using the name and color.
- `app = gr.Interface(...)`: Build the app with inputs, outputs, title, and description.
- `app.launch()`: Start the app. Gradio will show a link in the terminal.

### What Happens When We Run It
When you run this code, Gradio will show a link in your terminal. Click the link to open your app. If the link starts with `https://`, you can share it with anyone. They can use your app from their computer or phone!

---

In the next lesson, we’ll learn how to add more features to your app. For now, try sharing your app with someone and see how it works!