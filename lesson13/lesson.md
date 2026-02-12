# Lesson 13: Using a Real Machine Learning Model in Gradio 

## Friendly Introduction

Welcome to Lesson 13! Now you’ll learn how to use a real machine learning model in your Gradio app. We’ll use a simple model that can recognize numbers written by hand (called digits). Don’t worry—we’ll explain everything step by step.

## What You Will Learn
- What a real machine learning model is
- How to use a model to make predictions
- How to connect the model to Gradio

## Real-Life Analogy
Imagine a robot that can look at a picture of a number and guess what number it is. That’s what our model will do!

## Step-by-Step Explanation

### Step 1: What is a Real Machine Learning Model?
A real model learns from lots of examples. For this lesson, we’ll use a model that can recognize handwritten digits (numbers from 0 to 9).

### Step 2: Use a Pretrained Model
We’ll use a model from a library called scikit-learn. It’s already trained to recognize digits.

### Step 3: Connect the Model to Gradio
We’ll write a function that takes an image of a digit, uses the model to guess the number, and shows the result in the app.

### Full Code

```python
import gradio as gr
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier

# Load the digits dataset
digits = load_digits()
X, y = digits.data, digits.target

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Function to predict digit from image
def predict_digit(image):
    # Check if image is uploaded
    if image is None:
        return "No image uploaded."
    # Resize and flatten the image
    import numpy as np
    from skimage.transform import resize
    image = resize(image, (8, 8))
    image = image.reshape(1, -1) * 16  # Scale to match training data
    # Predict the digit
    prediction = model.predict(image)[0]
    return f"I think this digit is: {prediction}"

app = gr.Interface(
    fn=predict_digit,
    inputs=gr.Image(shape=(8, 8), label="Draw a digit (0-9)"),
    outputs="text",
    title="Digit Recognizer",
    description="Draw a number and the model will try to guess it!"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `from sklearn.datasets import load_digits`: Get the digits dataset.
- `from sklearn.ensemble import RandomForestClassifier`: Use a model to recognize digits.
- `digits = load_digits()`: Load the data.
- `model.fit(X, y)`: Train the model.
- `def predict_digit(image):`: Function to predict the digit from an image.
- `resize(image, (8, 8))`: Resize the image to match the model’s input.
- `model.predict(image)[0]`: Use the model to guess the digit.
- `app = gr.Interface(...)`: Build the app with an image input and text output.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to draw a digit. The app will use the model to guess what number you drew!

---

In the next lesson, we’ll learn how to deploy your Gradio app so anyone can use it online. For now, try using your app with different digits!
