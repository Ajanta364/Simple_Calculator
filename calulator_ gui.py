import tkinter as tk
import math

def click(event):
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            expr = entry.get()
            expr = expr.replace("^", "**")
            expr = expr.replace("π", str(math.pi)).replace("e", str(math.e))

            # Allow safe functions
            result = eval(expr, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "log": math.log10,
                "ln": math.log,
                "abs": abs
            })
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "C":
        entry.delete(0, tk.END)

    elif button_text == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])

    elif button_text == "√":
        entry.insert(tk.END, "sqrt(")

    elif button_text in ("sin", "cos", "tan", "log", "ln"):
        entry.insert(tk.END, button_text + "(")

    elif button_text in ("π", "e"):
        entry.insert(tk.END, button_text)

    else:
        entry.insert(tk.END, button_text)

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font="Arial 24", bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['C', '⌫', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
    ['π', 'e', '^', '√'],
    ['sin', 'cos', 'tan', '='],
    ['log', 'ln']
]

# Add buttons to the window
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RIDGE, bd=4)
        btn.pack(side=tk.LEFT, expand=True, fill='both')
        btn.bind("<Button-1>", click)

# Run app
root.mainloop()

