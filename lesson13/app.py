# This app uses a real machine learning model to recognize handwritten digits!
# Draw a number and the model will try to guess it.

import gradio as gr  # Bring in Gradio tools
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

# Create the app with an image input and text output
app = gr.Interface(
    fn=predict_digit,
    inputs=gr.Image(shape=(8, 8), label="Draw a digit (0-9)"),
    outputs="text",
    title="Digit Recognizer",
    description="Draw a number and the model will try to guess it!"
)

# Start the app
app.launch()