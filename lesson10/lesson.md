# Lesson 10: Using Advanced Features in Gradio  

## Friendly Introduction

Welcome to Lesson 10! You’ve learned how to make your app helpful and friendly. Now, let’s explore some advanced features in Gradio. We’ll learn how to let users upload files and how to use multiple pages in your app. These features make your app more powerful and useful.

## What You Will Learn
- How to let users upload files
- How to use multiple pages (Tabs) in your app
- How to combine these features

## Real-Life Analogy
Imagine your app is like a library. People can bring their own books (files) and look at different sections (pages). This makes your app more flexible and fun!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app with two pages (Tabs):
- One page lets users upload a text file and shows the content.
- The other page lets users upload an image and shows the image.

### Step 2: Create Functions for Each Page
We need two functions:
- One for reading and showing text files.
- One for showing images.

### Step 3: Use Gradio Tabs
Gradio lets us organize the app into pages using Tabs.

### Full Code

```python
import gradio as gr

def show_text_file(file):
    # Read the text file and show its content
    if file is None:
        return "No file uploaded."
    content = file.read().decode("utf-8")
    return content

def show_image_file(image):
    # Just return the image
    return image

with gr.Tab("Text File"):
    text_interface = gr.Interface(
        fn=show_text_file,
        inputs=gr.File(label="Upload a Text File"),
        outputs="text",
        title="Show Text File Content"
    )

with gr.Tab("Image File"):
    image_interface = gr.Interface(
        fn=show_image_file,
        inputs=gr.Image(label="Upload an Image"),
        outputs=gr.Image(label="Here is your Image"),
        title="Show Image File"
    )

gr.TabbedInterface([text_interface, image_interface], ["Text File", "Image File"]).launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def show_text_file(file):`: Function to read and show text file content.
- `if file is None: ...`: If no file is uploaded, show a message.
- `content = file.read().decode("utf-8")`: Read and decode the file content.
- `def show_image_file(image):`: Function to show the uploaded image.
- `with gr.Tab(...)`: Create a page (Tab) for each feature.
- `gr.Interface(...)`: Build the app for each page.
- `gr.TabbedInterface(...)`: Combine the pages and launch the app.

### What Happens When We Run It
When you run this code, you’ll see two pages (Tabs): one for text files and one for images. Upload a file on each page and see the result. Your app is now more advanced and flexible!

---

Congratulations! You’ve finished the beginner Gradio course. You can now build, organize, and share your own Gradio apps. Try adding your own ideas and features!
