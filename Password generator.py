import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create frame for password length input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

length_label = tk.Label(input_frame, text="Enter Password Length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(input_frame)
length_entry.pack(side=tk.LEFT)

# Create frame for button
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack()

# Create label to display generated password
password_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), pady=10)
password_label.pack()

# Configure window size and center it on screen
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) / 2
y_coordinate = (screen_height - window_height) / 2
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Run the Tkinter event loop
root.mainloop()
