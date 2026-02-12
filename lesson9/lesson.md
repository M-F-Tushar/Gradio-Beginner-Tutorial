# Lesson 9: Helping Users and Handling Errors in Your Gradio App

## Friendly Introduction

Welcome to Lesson 9! You’ve added many features to your app. Now, let’s learn how to help users and handle errors. Sometimes, users make mistakes or something goes wrong. A friendly app helps users and explains what to do.

## What You Will Learn
- How to show helpful messages
- How to handle errors in your app
- How to make your app user-friendly

## Real-Life Analogy
Imagine you’re baking a cake. If you forget an ingredient, a helpful friend reminds you. Your app can do the same—if something is missing or wrong, it can show a message to help.

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that asks for your name and age. If the user forgets to type their name or enters a negative age, the app will show a helpful message.

### Step 2: Change the Function
We need a function that checks the inputs. If something is wrong, it returns a message explaining what to fix.

### Step 3: Add Error Handling
We’ll use simple checks in the function to help the user.

### Full Code

```python
import gradio as gr

def check_inputs(name, age):
    # Check if name is empty
    if not name:
        return "Please type your name."
    # Check if age is negative
    if age < 0:
        return "Age cannot be negative. Please enter a positive number."
    # If everything is okay, greet the user
    return f"Hello, {name}! You are {age} years old."

app = gr.Interface(
    fn=check_inputs,
    inputs=[gr.Textbox(label="Your Name"), gr.Number(label="Your Age")],
    outputs="text",
    title="Friendly Greeting App",
    description="Type your name and age. The app will help you if you make a mistake."
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def check_inputs(name, age):`: Make a function that takes a name and age.
- `if not name: ...`: If the name is empty, show a helpful message.
- `if age < 0: ...`: If the age is negative, show a helpful message.
- `return f"Hello, {name}! You are {age} years old."`: If everything is okay, greet the user.
- `app = gr.Interface(...)`: Build the app with inputs, outputs, title, and description.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box for your name and age. If you forget your name or enter a negative age, the app will help you with a friendly message. If everything is correct, it will greet you!

---

In the next lesson, we’ll learn how to use Gradio’s advanced features, like uploading files or using multiple pages. For now, try making your app helpful and friendly!