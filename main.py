import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    if not password:
        return "No password entered"
    
    strength = 0
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    strength = sum(criteria.values())
    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

def check_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {result}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

root.mainloop()
