import tkinter as tk
from tkinter import messagebox, scrolledtext


# Create the main window with black background
window = tk.Tk()
window.title("Calculator")
window.config(bg="#121212")  # Dark background
window.geometry("400x500")

# History of calculations
history = []
expression = ""


def press(num):
    """Handles button presses for numbers and operators."""
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    """Evaluates the current expression."""
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        history.append(f"{expression} = {total}")
        expression = total
    except Exception:
        equation.set("Error")
        expression = ""


def clear():
    """Clears the current expression."""
    global expression
    expression = ""
    equation.set("")


def backspace():
    """Deletes the last character in the expression."""
    global expression
    expression = expression[:-1]
    equation.set(expression)


def show_history():
    """Displays the calculation history."""
    if not history:
        messagebox.showinfo("History", "No calculations yet.")
    else:
        history_window = tk.Toplevel(window)
        history_window.title("History")
        history_window.geometry("300x400")
        history_window.config(bg="#1e1e1e")
        tk.Label(history_window, text="Calculation History", bg="#1e1e1e", fg="white", font=("Arial", 14)).pack(pady=10)

        history_text = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, width=35, height=15, font=("Arial", 12), bg="#252525", fg="white")
        history_text.insert(tk.END, "\n".join(history))
        history_text.configure(state='disabled')
        history_text.pack(padx=10, pady=10)


def exit_app():
    """Exits the application."""
    window.quit()


# UI Components
equation = tk.StringVar()
entry = tk.Entry(
    window,
    textvariable=equation,
    font=("Arial", 20),
    borderwidth=2,
    relief="solid",
    justify="right",
    bg="#3e3e3e",
    fg="white",
)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Buttons configuration
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), bg="#4caf50", fg="white", command=equalpress)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), bg="#424242", fg="white", command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Additional buttons: Clear, Backspace, History, and Exit
clear_b = tk.Button(window, text="AC", width=5, height=2, font=("Arial", 14), bg="#f44336", fg="white", command=clear)
clear_b.grid(row=1, column=0, padx=5, pady=10)

backspace_b = tk.Button(window, text="⌫", width=5, height=2, font=("Arial", 14), bg="#ff9800", fg="white", command=backspace)
backspace_b.grid(row=1, column=1, padx=5, pady=10)

history_b = tk.Button(window, text="History", width=5, height=2, font=("Arial", 14), bg="#2196f3", fg="white", command=show_history)
history_b.grid(row=1, column=2, padx=5, pady=10)

exit_b = tk.Button(window, text="Exit", width=5, height=2, font=("Arial", 14), bg="#9c27b0", fg="white", command=exit_app)
exit_b.grid(row=1, column=3, padx=5, pady=10)

window.mainloop()
