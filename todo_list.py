import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x800")
        self.root.title("To Do List")
        self.root.attributes('-topmost', 1)

        #define tasks
        self.tasks = []
        self.completed_tasks = []

        #create widgets
        ttk.Label(self.root, text="New Task:").pack(pady=5)
        self.task_name_entry = ttk.Entry(self.root)
        self.task_name_entry.pack(pady=5)

        ttk.Button(self.root, text="Add New Task", command=self.add_task).pack(pady=5)

        ttk.Label(self.root, text="Tasks").pack(pady=5)
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

        ttk.Button(self.root, text="Move to Completed", command=self.move_to_completed).pack(pady=5)

        ttk.Label(self.root, text="Completed").pack(pady=5)
        self.completed_listbox = tk.Listbox(self.root, width=50, height=10)
        self.completed_listbox.pack(pady=10)

        ttk.Button(self.root, text="Delete Task", command=self.delete_task).pack(pady=5)

        self.always_on_top = tk.BooleanVar(self.root, False)
        self.always_on_top_button = ttk.Checkbutton(self.root, text="Toggle Always on Top", variable=self.always_on_top, command=self.toggle_always_on_top)
        self.always_on_top_button.pack(pady=5)

        self.dark_mode = tk.BooleanVar(self.root, True)
        self.toggle_dark_mode = ttk.Checkbutton(self.root, text="Dark Mode", variable=self.dark_mode, command=self.toggle_theme)
        self.toggle_dark_mode.pack(pady=5)

        self.toggle_theme()

    def toggle_always_on_top(self):
        self.root.attributes('-topmost', self.always_on_top.get())

    def toggle_theme(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Ensure the theme supports custom styling
        if self.dark_mode.get():
            self.root.configure(bg='#2E2E2E')  # Dark grey background for the root window
            self.style.configure('TLabel', background='#2E2E2E', foreground='white')
            self.style.configure('TButton', background='#4D4D4D', foreground='white')
            self.style.map('TButton', background=[('active', '#5E5E5E')], foreground=[('active', 'white')])
            self.style.configure('TEntry', fieldbackground='#4D4D4D', foreground='white')
            self.style.configure('TCheckbutton', background='#2E2E2E', foreground='white')
            self.tasks_listbox.configure(bg='#4D4D4D', fg='white', selectbackground='#6E6E6E', selectforeground='white')
            self.completed_listbox.configure(bg='#4D4D4D', fg='white', selectbackground='#6E6E6E', selectforeground='white')
        else:
            self.root.configure(bg='#f7f7f7')  # Light background for the root window
            self.style.configure('TLabel', background='white', foreground='black')
            self.style.configure('TButton', background='white', foreground='black')
            self.style.map('TButton', background=[('active', '#E0E0E0')], foreground=[('active', 'black')])
            self.style.configure('TEntry', fieldbackground='white', foreground='black')
            self.style.configure('TCheckbutton', background='white', foreground='black')
            self.tasks_listbox.configure(bg='white', fg='black', selectbackground='#D3D3D3', selectforeground='black')
            self.completed_listbox.configure(bg='white', fg='black', selectbackground='#D3D3D3', selectforeground='black')

    def add_task(self):
        new_task = self.task_name_entry.get()
        if new_task:
            print(new_task, "was added to the tasks list!")
            self.task_name_entry.delete(0, tk.END)
            self.tasks.append(new_task)
            self.update_tasks_listbox()
        else:
            tk.messagebox.showwarning("Input Error", "Task name cannot be empty.")

    def move_to_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            cur_task = self.tasks[index]
            self.completed_tasks.append(cur_task)
            del self.tasks[index]
            self.update_tasks_listbox()
            self.update_completed_listbox()
        else:
            tk.messagebox.showwarning("Selection Error", "No task selected.")

    def delete_task(self):
        selected_task_index = self.completed_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.completed_tasks[index]
            self.update_completed_listbox()
        else:
            tk.messagebox.showwarning("Selection Error", "No task selected.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, str(task))

    def update_completed_listbox(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, str(task))
    

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()