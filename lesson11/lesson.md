# Lesson 11: Customizing Your Gradio App with Themes 

## Friendly Introduction

Welcome to Lesson 11! Now that you know how to build and organize Gradio apps, let’s learn how to make your app look unique and beautiful. Gradio lets you change the colors and style of your app using themes.

## What You Will Learn
- How to use Gradio themes
- How to change the look of your app
- How to make your app stand out

## Real-Life Analogy
Think of your app like a room. You can paint the walls, change the furniture, and add decorations to make it feel special. Themes are like paint and decorations for your app!

## Step-by-Step Explanation

### Step 1: Plan What the App Will Do
Let’s make an app that greets the user and lets them pick a theme. The app will change its look based on the theme you choose.

### Step 2: Add a Theme
Gradio has built-in themes you can use. You just add a theme when you create your app.

### Full Code

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

app = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs="text",
    title="Themed Greeting App",
    description="Type your name and see the app in different themes!",
    theme="soft"
)
app.launch()
```

### Explanation of the Code Line by Line

- `import gradio as gr`: Bring in Gradio tools.
- `def greet(name):`: Make a function that takes a name.
- `app = gr.Interface(...)`: Build the app.
    - `theme="soft"`: Sets the app’s theme to "soft". You can try other themes like "monochrome", "peach", or "default".
- `app.launch()`: Start the app.

### What Happens When We Run It
When you run this code, you’ll see a greeting app with a new look. Try changing the theme to see different styles. Your app can look modern, colorful, or simple!

---

In the next lesson, we’ll learn how to connect Gradio to a machine learning model. For now, try customizing your app with different themes!
