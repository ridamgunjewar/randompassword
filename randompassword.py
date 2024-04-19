import random
import string
from tkinter import messagebox
import tkinter as tk

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_prompt():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Password Generator")

    # Function to generate the password
    def generate():
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    # Label and entry for password length
    length_label = tk.Label(window, text="Password Length:")
    length_label.pack()
    length_entry = tk.Entry(window)
    length_entry.pack()

    # Checkboxes for character types
    letters_var = tk.BooleanVar()
    letters_check = tk.Checkbutton(window, text="Letters", variable=letters_var)
    letters_check.pack()
    numbers_var = tk.BooleanVar()
    numbers_check = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
    numbers_check.pack()
    symbols_var = tk.BooleanVar()
    symbols_check = tk.Checkbutton(window, text="Symbols", variable=symbols_var)
    symbols_check.pack()

    # Button to generate password
    generate_button = tk.Button(window, text="Generate Password", command=generate)
    generate_button.pack()

    # Entry to display the generated password
    password_entry = tk.Entry(window, width=30)
    password_entry.pack()

    # Run the Tkinter event loop
    window.mainloop()

generate_password_prompt()
