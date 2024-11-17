import json
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self._title = title
        self._content = content

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Название не может быть пустым.")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not value:
            raise ValueError("Содержание не может быть пустым.")
        self._content = value


# Пример использования
note = Note("Пример заметки", "Текст заметки", ["Python", "Заметка"])
print(note.to_dict())
