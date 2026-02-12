# Lesson 12: Connecting Gradio to a Machine Learning Model 

## Friendly Introduction

Welcome to Lesson 12! Now you’ll learn how to connect Gradio to a machine learning model. Don’t worry if you don’t know what machine learning is—we’ll explain everything step by step.

## What You Will Learn
- What a machine learning model is
- How to use a simple model in your app
- How Gradio can show model results

## Real-Life Analogy
Imagine a smart robot that can look at numbers and guess if they are big or small. Machine learning models are like smart robots that can make predictions based on data.

## Step-by-Step Explanation

### Step 1: What is a Machine Learning Model?
A machine learning model is a computer program that learns from examples. It can make predictions, like guessing if a number is big or small.

### Step 2: Make a Simple Model
We’ll use a simple model that checks if a number is greater than 10. If it is, the model says "Big". If not, it says "Small".

### Step 3: Connect the Model to Gradio
We’ll write a function that uses the model and show the result in the app.

### Full Code

```python
import gradio as gr

def simple_model(number):
    # The model checks if the number is big or small
    if number > 10:
        return "Big"
    else:
        return "Small"

app = gr.Interface(
    fn=simple_model,
    inputs=gr.Number(label="Enter a Number"),
    outputs="text",
    title="Simple Model App",
    description="Type a number and see if the model thinks it is big or small."
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def simple_model(number):`: Make a function that acts like a model.
- `if number > 10: ... else: ...`: The model checks if the number is big or small.
- `app = gr.Interface(...)`: Build the app with a number input and text output.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to enter a number. The app will tell you if the number is big or small, using the model.

---

In the next lesson, we’ll use a real machine learning model to make predictions. For now, try connecting your app to this simple model!
