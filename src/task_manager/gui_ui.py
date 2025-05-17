import tkinter as tk
from tkinter import simpledialog, messagebox
from .auth import login, register
from .tasks import add_task, view_tasks, mark_complete, delete_task

def run_gui():
    root = tk.Tk()
    root.withdraw()

    while True:
        action = simpledialog.askstring("Task Manager", "Type 'login', 'register', or 'exit':")
        if action == 'exit':
            break
        if action == 'register':
            register()
        elif action == 'login':
            user = login()
            if user:
                show_menu(user)
        else:
            messagebox.showerror("Error", "Invalid input")

def show_menu(username):
    while True:
        choice = simpledialog.askstring("Menu", "Choose: add/view/mark/delete/logout")
        if choice == 'add':
            add_task(username)
        elif choice == 'view':
            view_tasks(username, gui=True)
        elif choice == 'mark':
            mark_complete(username)
        elif choice == 'delete':
            delete_task(username)
        elif choice == 'logout':
            break
