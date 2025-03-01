import gradio as gr

def square_numbers(x):
    return x**2

interface = gr.Interface(fn=square_numbers, inputs="number", outputs="number")

interface.launch()