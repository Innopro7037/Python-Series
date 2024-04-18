import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(var.get()))
    output.config(text = password)
    output.config(text = password, font=('Ubuntu', 20), justify = 'center')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output['text'])

root = ThemedTk(theme="arc")
root.title('Password Generator')
root.geometry('600x500')

var = tk.IntVar()
var.set(8)

dropdown = ttk.Combobox(root, textvariable=var, values=[8,9,10,11,12,13,14,15,16,17,18,19,20])
dropdown.pack(pady=5)

generate_button = ttk.Button(root, text='Generate', command=generate_password)
generate_button.pack(pady=5)

copy_button = ttk.Button(root, text='Copy', command=copy_to_clipboard)
copy_button.pack(pady=5)

output = ttk.Label(root)
output.pack(pady=20)

input = ttk.Entry(root, width=50)
input.pack()

root.mainloop()