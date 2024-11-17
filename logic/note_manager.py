from logic.note_logic import Note

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def remove_note_by_title(self, title):
        self.notes = [note for note in self.notes if note.title != title]

    def get_all_notes(self):
        return self.notes
