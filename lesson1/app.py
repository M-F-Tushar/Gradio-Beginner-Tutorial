# This line brings in Gradio so we can use it in our code
# "import" means "get this tool for me"
# "as gr" means "let me call it 'gr' for short"
import gradio as gr

# This is our function - a small program that does one specific job
# It takes a name (whatever someone types) and returns a greeting
def greet(name):
    # "return" means "give back this result"
    # We're gluing together "Hello ", the person's name, and "!"
    return "Hello " + name + "!"

# This line creates our app's interface (the buttons and boxes people see)
# fn=greet means "use the greet function to do the work"
# inputs="text" means "let people TYPE something"
# outputs="text" means "show TEXT as the result"
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# This line starts the app and opens it in your web browser
# It's like pressing the "power on" button!
demo.launch()
