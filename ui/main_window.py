import tkinter as tk
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        self.geometry("800x600")

        # Меню
        menu = tk.Menu(self)
        self.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Add Note", command=self.add_note)
        edit_menu.add_command(label="Edit Note", command=self.edit_note)
        edit_menu.add_command(label="Remove Note", command=self.remove_note)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Левая панель (список заметок)
        self.notes_listbox = tk.Listbox(self, width=30)
        self.notes_listbox.pack(side=tk.LEFT, fill=tk.Y)

        # Правая панель (детали заметки)
        self.details_text = tk.Text(self, wrap=tk.WORD)
        self.details_text.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Нижние кнопки
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(bottom_frame, text="Add Note", command=self.add_note).pack(side=tk.LEFT)
        tk.Button(bottom_frame, text="Edit Note", command=self.edit_note).pack(side=tk.LEFT)
        tk.Button(bottom_frame, text="Remove Note", command=self.remove_note).pack(side=tk.LEFT)

    def add_note(self):
        messagebox.showinfo("Add Note", "Functionality to be implemented")

    def edit_note(self):
        messagebox.showinfo("Edit Note", "Functionality to be implemented")

    def remove_note(self):
        messagebox.showinfo("Remove Note", "Functionality to be implemented")

    def show_about(self):
        messagebox.showinfo("About", "NoteApp v1.0\nAuthor: Бармотин Станислав\nGroup: ДМП-203уит")
