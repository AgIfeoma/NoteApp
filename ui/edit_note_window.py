import tkinter as tk
from tkinter import messagebox

class EditNoteWindow(tk.Toplevel):
    def __init__(self, master, note=None):
        super().__init__(master)
        self.title("Add/Edit Note")
        self.geometry("500x400")

        # Поля ввода
        tk.Label(self, text="Title:").pack(anchor=tk.W, padx=10, pady=5)
        self.title_entry = tk.Entry(self, width=50)
        self.title_entry.pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(self, text="Category:").pack(anchor=tk.W, padx=10, pady=5)
        self.category_entry = tk.Entry(self, width=50)
        self.category_entry.pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(self, text="Content:").pack(anchor=tk.W, padx=10, pady=5)
        self.content_text = tk.Text(self, wrap=tk.WORD, height=10)
        self.content_text.pack(anchor=tk.W, padx=10, pady=5)

        # Кнопки
        tk.Button(self, text="Save", command=self.save_note).pack(side=tk.RIGHT, padx=10, pady=10)
        tk.Button(self, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=10, pady=10)

        # Если редактируем существующую заметку, заполняем данные
        if note:
            self.title_entry.insert(0, note.get("title", ""))
            self.category_entry.insert(0, note.get("category", ""))
            self.content_text.insert(1.0, note.get("content", ""))

    def save_note(self):
        messagebox.showinfo("Save Note", "Note saved successfully!")
        self.destroy()

    def cancel(self):
        self.destroy()
