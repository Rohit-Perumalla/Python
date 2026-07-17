import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Global variable to store expression
expression = ""

# Function to update the expression in the text entry box
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))  # eval is used to calculate string expressions
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar() to update text in entry box
equation = tk.StringVar()

# Entry widget for showing expressions
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry_field.grid(row=0, column=0, columnspan=5)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Creating buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 12), bg='yellow',
                  command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=95, pady=20, font=('Arial', 12), bg='darkred',
                  command=clear).grid(row=row, column=col, columnspan=3)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 12),
                  command=lambda t=text: press(t)).grid(row=row, column=col)

# Run the application
root.mainloop()
