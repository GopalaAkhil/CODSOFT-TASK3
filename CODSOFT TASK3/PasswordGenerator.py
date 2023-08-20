import random
import string
import pyperclip
from tkinter import *
from tkinter import messagebox

# Initialize Window
root = Tk()
root.geometry("400x400")  # size of the window by default
root.title("Random Password Generator")
#root.iconbitmap("password.ico")

# ------------------- Random Password generator function
output_pass = StringVar()

def randPassGen():
    password = ""
    complexity = complexity_var.get()

    all_chars = ""
    if 'lowercase' in complexity:
        all_chars += string.ascii_lowercase
    if 'uppercase' in complexity:
        all_chars += string.ascii_uppercase
    if 'digits' in complexity:
        all_chars += string.digits
    if 'special_chars' in complexity:
        all_chars += string.punctuation

    if not all_chars:
        messagebox.showerror("Error", "Please select at least one complexity option.")
        return

    for y in range(pass_len.get()):
        char_type = random.choice(all_chars)
        password += char_type

    output_pass.set(password)

# ----------- Copy to clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

# -----------------------GUI
pass_head = Label(root, text='Password Length', font='arial 12 bold')
pass_head.pack(pady=10)  # to generate label heading

pass_len = IntVar()  # integer variable to store the input of length of the password wanted
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font='arial 16')
length.pack()

# Complexity options dialog
complexity_var = StringVar()
complexity_options = [('Lowercase Letters', 'lowercase'), ('Uppercase Letters', 'uppercase'),
                      ('Digits (0-9)', 'digits'), ('Special Characters', 'special_chars')]

complexity_frame = LabelFrame(root, text="Password Complexity", font="arial 12 bold")
complexity_frame.pack(pady=10, padx=10)

for text, value in complexity_options:
    checkbox = Checkbutton(complexity_frame, text=text, variable=complexity_var, onvalue=value, offvalue="", font=("Helvetica", 12))
    checkbox.pack(anchor="w", padx=20)

# Generate password button
Button(root, command=randPassGen, text="Generate Password", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

pass_label = Label(root, text='Random Generated Password', font='arial 12 bold')
pass_label.pack(pady="15 10")
Entry(root, textvariable=output_pass, width=24, font='arial 16').pack()

# Copy to clipboard button
Button(root, text='Copy to Clipboard', command=copyPass, font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()
