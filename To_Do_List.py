import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from JSON
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save tasks to JSON
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List Application")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.tasks = load_tasks()

        self.task_listbox = tk.Listbox(root, width=70, height=20, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="➕ Add Task", width=15, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="✏️ Edit Task", width=15, command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="✅ Mark Completed", width=15, command=self.mark_completed).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="🗑️ Delete Task", width=15, command=self.delete_task).grid(row=0, column=3, padx=5)

        self.load_tasks_into_listbox()

    def load_tasks_into_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✅" if task['completed'] else "❌"
            priority = task.get('priority', 'Medium')
            display = f"{status} {task['title']} | Priority: {priority} - {task['description']}"
            self.task_listbox.insert(tk.END, display)

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter task title:")
        if not title:
            return

        description = simpledialog.askstring("Task Description", "Enter task description (optional):")
        priority = simpledialog.askstring("Task Priority", "Enter priority (High, Medium, Low):")

        if not priority:
            priority = "Medium"

        priority = priority.capitalize()
        if priority not in ['High', 'Medium', 'Low']:
            priority = "Medium"

        new_task = {
            "title": title,
            "description": description or "",
            "priority": priority,
            "completed": False
        }

        self.tasks.append(new_task)
        save_tasks(self.tasks)
        self.load_tasks_into_listbox()

    def edit_task(self):
        index = self.task_listbox.curselection()
        if not index:
            messagebox.showwarning("Select a Task", "Please select a task to edit.")
            return

        i = index[0]
        task = self.tasks[i]

        new_title = simpledialog.askstring("Edit Title", "Edit task title:", initialvalue=task['title'])
        new_description = simpledialog.askstring("Edit Description", "Edit task description:", initialvalue=task['description'])
        new_priority = simpledialog.askstring("Edit Priority", "Edit priority (High, Medium, Low):", initialvalue=task['priority'])

        if new_title:
            task['title'] = new_title
        if new_description is not None:
            task['description'] = new_description
        if new_priority:
            new_priority = new_priority.capitalize()
            if new_priority in ['High', 'Medium', 'Low']:
                task['priority'] = new_priority

        save_tasks(self.tasks)
        self.load_tasks_into_listbox()

    def mark_completed(self):
        index = self.task_listbox.curselection()
        if not index:
            messagebox.showwarning("Select a Task", "Please select a task to mark as completed.")
            return

        i = index[0]
        self.tasks[i]['completed'] = True
        save_tasks(self.tasks)
        self.load_tasks_into_listbox()

    def delete_task(self):
        index = self.task_listbox.curselection()
        if not index:
            messagebox.showwarning("Select a Task", "Please select a task to delete.")
            return

        i = index[0]
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
        if confirm:
            del self.tasks[i]
            save_tasks(self.tasks)
            self.load_tasks_into_listbox()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

