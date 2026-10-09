# Create the calculator's main window locally rather than importing an
# incomplete/abstract root object from another module.
import tkinter as tk

root = tk.Tk()

# Main window
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


def click(value: str) -> None:
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        expression = expression.replace("×", "*").replace("÷", "/")
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    ["C", "%", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".",]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "C":
            command = clear
        elif button == "=":
            command = calculate
        else:
            command = lambda x=button: click(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=2,
            pady=2
        )

root.mainloop()