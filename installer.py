import os
import subprocess
import sys
from textwrap import dedent

# Create calculator.py
calculator_code = dedent("""
import tkinter as tk
import sys
import ctypes

# Hide terminal for windows
try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except:
    pass

def on_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False, False)

entry = tk.Entry(root, width=15, font=("Arial", 24), justify="right")
entry.pack(pady=10, padx=10, fill="x")

# Buttons layout
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

for r, row in enumerate(buttons):
    for c, b in enumerate(row):
        button = tk.Button(
            frame,
            text=b,
            font=("Arial", 18),
            command=lambda x=b: on_click(x)
        )
        button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# Make it fit OwO
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)

# Exit on calc close
def on_close():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
""")

calculator_path = os.path.join(os.path.dirname(__file__), "calculator.py")

with open(calculator_path, "w", encoding="utf-8") as f:
    f.write(calculator_code)

print(f"Created calculator.py at: {calculator_path}")

# Run calculator
print("Launching calculator...")
subprocess.run([sys.executable, calculator_path])
