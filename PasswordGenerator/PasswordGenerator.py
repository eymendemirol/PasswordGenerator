# -------------------- Libraries --------------------
from tkinter import *
from pathlib import Path
import sys
import os
import string
import secrets
import random
import pyperclip
from tkinter import ttk

# -------------------- Resource Path Function --------------------
def resource_path(relative_path):
    """ Get the correct path for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# -------------------- Main window settings --------------------
root = Tk()
root.title("Password Generator")
root.geometry("400x380")

MAX_LENGTH = 128

# -------------------- Theme colors --------------------
dark_mode =  False
current_bg = "#ffffff"
current_fg = "black"
current_btn_bg = "#e0e0e0"
current_btn_fg = "black"

style = ttk.Style()
style.theme_use('clam')

style.configure("green.Horizontal.TProgressbar", troughcolor="#f0f0f0", background="#4CAF50")

# -------------------- Path setup --------------------
icon_path = resource_path("icon.png")

# -------------------- Load icon --------------------
try:
    icon = PhotoImage(file=str(icon_path))
    root.iconphoto(False, icon)
except:
    print("Icon could not be loaded")

# -------------------- Functions --------------------
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        update_result_text(result_text, "Please enter a number")
        return
    if length > MAX_LENGTH:
        update_result_text(result_text, f"Maximum password length is {MAX_LENGTH}")
        return
    
    selected_sets = []
    if lower.get():
        selected_sets.append(string.ascii_lowercase)
    if upper.get():
        selected_sets.append(string.ascii_uppercase)
    if digits.get():
        selected_sets.append(string.digits)
    if symbols.get():
        selected_sets.append("@!%$#&*-?")

    if not selected_sets:
        update_result_text(result_text, "You must choose at least one option!")
        return
    if length < len(selected_sets):
        update_result_text(result_text, "The length is too short!")
        return
    
    password_chars = [secrets.choice(s) for s in selected_sets]
    combined = "".join(selected_sets)
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(combined))
    random.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)
    update_result_text(result_text, password)

    strength = check_strength(password)
    strength_bar["value"] = strength

    if strength < 40:
        strength_label.config(text="Strength: Weak", fg="red")
    elif strength < 70:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 20
    if len(password) >=12:
        score += 20
    if any(c.islower() for c in password):
        score += 15
    if any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15
    if any(c in "@!%$#&*-?" for c in password):
        score += 15
    return min(score, 100)

def copy_password(widget):
    password = widget.get("1.0", END).strip()
    if password and "Password" not in password:
        pyperclip.copy(password)
        widget.config(state="normal")
        widget.delete("1.0", END)
        widget.insert("1.0", "Password Copied Successfully")
        widget.config(state="disabled")

def theme():
    global dark_mode, current_bg, current_fg, current_btn_bg, current_btn_fg
    if dark_mode:
        current_bg, current_fg, current_btn_bg, current_btn_fg = "#ffffff", "black", "#e0e0e0", "black"
        bar_trough = "#f0f0f0"
        dark_mode = False
    else:
        current_bg, current_fg, current_btn_bg, current_btn_fg = "#222222", "white", "#444444", "white"
        bar_trough = "#3e3e3e"
        dark_mode = True

    root.config(bg=current_bg)
    for widget in all_widgets:
        try:
            if isinstance(widget, Checkbutton):
                widget.config(bg=current_bg, fg=current_fg, selectcolor=current_bg)
            elif isinstance(widget, Button):
                widget.config(bg=current_btn_bg, fg=current_btn_fg)
            else:
                widget.config(bg=current_bg, fg=current_fg)
        except:
            pass

    style.configure("green.Horizontal.TProgressbar", troughcolor=bar_trough, background="#4CAF50")

def update_result_text(widget, text):
    widget.config(state="normal")
    widget.delete("1.0", END)
    widget.insert("1.0", text)
    widget.config(state="disabled")

# -------------------- Widgets --------------------
length_label = Label(root, text="Required Password length", font=("Roboto",10))
length_label.pack(pady=5)

length_entry = Entry(root,width=10, font=("Roboto",10))
length_entry.pack(pady=5)

result_text = Text(root, height=3, width=40, font=("Roboto",10), wrap="word")
result_text.insert("1.0", "Recommended Password Will Appear Here")
result_text.config(state="disabled")
result_text.pack(pady=5)

strength_label = Label(root, text="Strength: -", font=("Roboto",10))
strength_label.pack(pady=5)

strength_bar = ttk.Progressbar(root, length=200, mode="determinate", maximum=100, style="green.Horizontal.TProgressbar")
strength_bar.pack(pady=5)

copy_button = Button(root, text="Copy to Clipboard", command=lambda:copy_password(result_text), font=("Roboto",10))
copy_button.pack(pady=5)

lower = BooleanVar(value=True)
upper = BooleanVar(value=True)
digits = BooleanVar(value=True)
symbols = BooleanVar(value=False)

lower_check = Checkbutton(root, text="Lower Case", variable=lower, font=("Roboto",10))
lower_check.pack(anchor="w", padx=20)
upper_check = Checkbutton(root, text="Upper Case", variable=upper, font=("Roboto",10))
upper_check.pack(anchor="w", padx=20)
digits_check = Checkbutton(root, text="Digits", variable=digits, font=("Roboto",10))
digits_check.pack(anchor="w", padx=20)
symbols_check = Checkbutton(root, text="Symbols", variable=symbols, font=("Roboto",10))
symbols_check.pack(anchor="w", padx=20)

generate_button = Button(root, text="Generate Password", command=generate_password, font=("Roboto",10))
generate_button.pack(pady=5)

theme_button = Button(root, text="Toggle Theme", command=theme, font=("Roboto",10))
theme_button.place(x=305, y=4)

# -------------------- Collect all widgets for theme toggle --------------------
all_widgets = [length_label, length_entry, result_text, strength_label, copy_button, lower_check, upper_check, digits_check, symbols_check, generate_button, theme_button]


# -------------------- Start program --------------------
root.mainloop()