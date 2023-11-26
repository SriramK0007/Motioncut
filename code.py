import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.completed_tasks = []

        # Task Entry Frame
        entry_frame = ttk.Frame(self.root, padding="10")
        entry_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Task Entry Widgets
        ttk.Label(entry_frame, text="Task Description:").grid(row=0, column=0, sticky=tk.W)
        self.task_description_entry = ttk.Entry(entry_frame, width=40)
        self.task_description_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(entry_frame, text="Due Date:").grid(row=1, column=0, sticky=tk.W)
        self.due_date_entry = ttk.Entry(entry_frame, width=20)
        self.due_date_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(entry_frame, text="Priority:").grid(row=2, column=0, sticky=tk.W)
        self.priority_entry = ttk.Entry(entry_frame, width=20)
        self.priority_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Button(entry_frame, text="Add Task", command=self.add_task).grid(row=3, column=1, sticky=tk.E)

        # Task List Treeview
        columns = ("Description", "Due Date", "Priority", "Status")
        self.task_tree = ttk.Treeview(self.root, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.task_tree.heading(col, text=col)
        self.task_tree.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Buttons for Mark as Completed, Update, and Remove
        action_frame = ttk.Frame(self.root, padding="10")
        action_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

        ttk.Button(action_frame, text="Mark as Completed", command=self.mark_completed).grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text="Update Task", command=self.update_task).grid(row=0, column=1, padx=5)
        ttk.Button(action_frame, text="Remove Task", command=self.remove_task).grid(row=0, column=2, padx=5)

        # Task List Treeview for Completed Tasks
        columns_completed = ("Description", "Due Date", "Priority", "Status")
        self.completed_tree = ttk.Treeview(self.root, columns=columns_completed, show="headings", selectmode="browse")
        for col in columns_completed:
            self.completed_tree.heading(col, text=col)
        self.completed_tree.grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        # Add a heading for completed tasks
        self.completed_tree.insert("", "end", values=("Completed Tasks", "", "", ""), tags=('heading',))

        # Button to Restore Completed Task
        ttk.Button(action_frame, text="Restore Completed Task", command=self.restore_completed_task).grid(row=0, column=3, padx=5)

    def add_task(self):
        description = self.task_description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        new_task = Task(description, due_date, priority)
        self.tasks.append(new_task)
        self.update_task_list()
        self.clear_entry_fields()

    def update_task_list(self):
        self.task_tree.delete(*self.task_tree.get_children())

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            self.task_tree.insert("", "end", values=(task.description, task.due_date, task.priority, status))

    def clear_entry_fields(self):
        self.task_description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = self.task_tree.index(selected_item)
            task = self.tasks[index]
            task.completed = not task.completed
            if task.completed:
                self.completed_tasks.append(task)
                del self.tasks[index]
            self.update_task_list()
            self.update_completed_task_list()

    def update_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = self.task_tree.index(selected_item)
            description = self.task_description_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()
            self.tasks[index].description = description
            self.tasks[index].due_date = due_date
            self.tasks[index].priority = priority
            self.update_task_list()
            self.clear_entry_fields()

    def remove_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = self.task_tree.index(selected_item)
            del self.tasks[index]
            self.update_task_list()

    def update_completed_task_list(self):
        # Remove the previous completed tasks
        for item in self.completed_tree.get_children():
            self.completed_tree.delete(item)

        # Add a heading for completed tasks
        self.completed_tree.insert("", "end", values=("Completed Tasks", "", "", ""), tags=('heading',))

        # Add completed tasks
        for task in self.completed_tasks:
            status = "Completed"
            self.completed_tree.insert("", "end", values=(task.description, task.due_date, task.priority, status))

    def restore_completed_task(self):
        selected_item = self.completed_tree.selection()
        if selected_item:
            index = self.completed_tree.index(selected_item)
            task = self.completed_tasks[index]
            task.completed = False
            del self.completed_tasks[index]
            self.tasks.append(task)
            self.update_task_list()
            self.update_completed_task_list()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
