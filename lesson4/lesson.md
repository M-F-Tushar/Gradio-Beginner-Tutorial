# Lesson 4: Using Images in Your Gradio App

## Friendly Introduction

Welcome to Lesson 4! You’ve learned how to use text and numbers in your app. Now, let’s make your app work with pictures. This is fun and useful—many apps use images, like photo editors or games.

## What You Will Learn
- How to let users upload an image
- How to show the image in your app
- How to use the image in your function

## Real-Life Analogy
Imagine you’re showing a photo to a friend. Your app can do the same! It can look at a picture and show it back to you, just like sharing photos on your phone.

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that lets the user upload a picture. The app will show the same picture back. Later, you can make apps that do more with images, like drawing or changing colors.

### Step 2: Change the Function
We need a function that takes an image and returns it. This is like a mirror—it shows back what you give it.

### Step 3: Add an Image Input Box
Gradio lets us use an image input. The user can upload a photo.

### Full Code

```python
import gradio as gr

def show_image(image):
    # Just return the image as it is
    return image

app = gr.Interface(
    fn=show_image,
    inputs=gr.Image(label="Upload an Image"),
    outputs=gr.Image(label="Here is your Image")
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def show_image(image):`: Make a function that takes an image.
- `return image`: Give back the same image.
- `app = gr.Interface(...)`: Build the app.
    - `inputs=gr.Image(label="Upload an Image")`: The user can upload a picture.
    - `outputs=gr.Image(label="Here is your Image")`: The app shows the picture back.
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a box to upload an image. Pick a photo from your computer and press submit. The app will show your photo back to you!

---

In the next lesson, we’ll learn how to use sliders and other controls. For now, try uploading different images and see what happens!