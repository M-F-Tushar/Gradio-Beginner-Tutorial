# Lesson 8: Adding More Features to Your Gradio App

## Friendly Introduction

Welcome to Lesson 8! You’ve learned how to build, organize, and share your app. Now, let’s make your app even more powerful by adding extra features. We’ll learn how to use checkboxes and radio buttons. These let users make choices easily.

## What You Will Learn
- How to add checkboxes to your app
- How to use radio buttons for choices
- How to use these inputs in your function

## Real-Life Analogy
Think of checkboxes like a to-do list. You check off what you want. Radio buttons are like picking one flavor of ice cream—you can only choose one at a time.

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that asks for your name, lets you pick your favorite fruit (using radio buttons), and asks if you want a fruit salad (using a checkbox). The app will greet you and tell you your choices.

### Step 2: Change the Function
We need a function that takes a name, a fruit, and a yes/no answer from the checkbox.

### Step 3: Add Radio Buttons and Checkbox Inputs
Gradio lets us use radio buttons and checkboxes. Radio buttons let you pick one option. Checkboxes let you pick yes or no.

### Full Code

```python
import gradio as gr

def fruit_greeting(name, fruit, salad):
    # Make a message using the name, fruit, and salad choice
    if salad:
        salad_msg = "You want a fruit salad."
    else:
        salad_msg = "You don't want a fruit salad."
    return f"Hello, {name}! Your favorite fruit is {fruit}. {salad_msg}"

app = gr.Interface(
    fn=fruit_greeting,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Radio(choices=["Apple", "Banana", "Orange", "Grapes"], label="Favorite Fruit"),
        gr.Checkbox(label="Do you want a fruit salad?")
    ],
    outputs="text",
    title="Fruit Choice App",
    description="Type your name, pick your favorite fruit, and choose if you want a fruit salad."
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def fruit_greeting(name, fruit, salad):`: Make a function that takes a name, fruit, and salad choice.
- `if salad: ... else: ...`: Decide what message to show based on the checkbox.
- `return f"Hello, {name}! Your favorite fruit is {fruit}. {salad_msg}"`: Make a message using the name, fruit, and salad choice.
- `app = gr.Interface(...)`: Build the app.
    - `gr.Textbox(label="Your Name")`: A box for typing your name.
    - `gr.Radio(choices=["Apple", "Banana", "Orange", "Grapes"], label="Favorite Fruit")`: Radio buttons for picking one fruit.
    - `gr.Checkbox(label="Do you want a fruit salad?")`: Checkbox for yes/no.
    - `title` and `description`: Make the app clear and friendly.
- `outputs="text"`: The app will show a text message.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box for your name, radio buttons for fruit, and a checkbox for fruit salad. Type your name, pick a fruit, check the box if you want a fruit salad, and press submit. The app will greet you and tell you your choices!

---

In the next lesson, we’ll learn how to handle errors and help users if something goes wrong. For now, try using the new features and see how they work!