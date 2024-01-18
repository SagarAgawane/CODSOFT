import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x600")

        self.tasks = []

        # Create and set up the listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create and set up the entry widget
        self.task_entry = tk.Entry(root, font=("Helvetica", 12))
        self.task_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create and set up buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="green", fg="Black")
        self.add_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="orange", fg="Black")
        self.remove_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="Black")
        self.quit_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        # Load existing tasks
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file if line.strip()]
            self.update_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            self.update_listbox()
            messagebox.showinfo("Task Removed", f"Task '{removed_task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
