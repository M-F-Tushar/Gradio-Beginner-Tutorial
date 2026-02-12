# Lesson 3: Using Different Types of Input in Gradio

## Friendly Introduction

Welcome to Lesson 3! You’ve already made an app that says hello and greets people by name. Now, let’s make your app even smarter. We’ll learn how to use different types of input, like text and numbers. This will help your app do more things, just like a calculator or a form you fill out online.

## What You Will Learn
- How to use text and number inputs in Gradio
- How to combine different inputs
- How to use the inputs in your app

## Real-Life Analogy
Think of your app like a friendly robot. Sometimes, the robot needs to know your name (text), and sometimes it needs to know your age (number). By giving the robot both, it can talk to you in a more personal way!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that asks for your name and your age. The app will greet you and tell you how old you will be next year.

### Step 2: Change the Function
We need a function that takes two things: a name and an age. The function will use both to make a message.

### Step 3: Add Two Input Boxes
Gradio lets us add more than one input. We’ll use a text box for the name and a number box for the age.

### Full Code

```python
import gradio as gr

def greet_and_age(name, age):
    # Make a message using the name and age
    next_year = age + 1
    return f"Hello, {name}! Next year, you will be {next_year} years old."

app = gr.Interface(
    fn=greet_and_age,
    inputs=[gr.Textbox(label="Your Name"), gr.Number(label="Your Age")],
    outputs="text"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools so we can build our app.
- `def greet_and_age(name, age):`: Make a function that takes two things: a name and an age.
- `next_year = age + 1`: Add 1 to the age to find out how old the user will be next year.
- `return f"Hello, {name}! Next year, you will be {next_year} years old."`: Make a message using the name and the new age.
- `app = gr.Interface(...)`: Build the app. We use two input boxes:
    - `gr.Textbox(label="Your Name")`: A box for typing your name.
    - `gr.Number(label="Your Age")`: A box for typing your age as a number.
- `outputs="text"`: The app will show a text message.
- `app.launch()`: Start the app. This opens the app in your web browser.

### What Happens When We Run It
When you run this code, you’ll see two boxes: one for your name and one for your age. Type your name and age, then press submit. The app will greet you and tell you how old you’ll be next year!

---

In the next lesson, we’ll learn how to use other types of input, like images or sliders. For now, try using your app with different names and ages!