import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        message_label.config(text="Password length must be at least 4.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    if password in password_history:
        message_label.config(text="Generated password already exists in history.")
        return

    password_history.append(password)


    password_text.delete(1.0, tk.END)
    password_text.insert(tk.END, password)


    message_label.config(text="Generated password: " + password)


root = tk.Tk()
root.geometry("600x300")



length_label = tk.Label(root, text="Password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack()

password_text = tk.Text(root, height=4, width=20)
password_text.pack()

message_label = tk.Label(root, text="")
message_label.pack()

password_history = []

root.mainloop()