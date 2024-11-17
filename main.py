from logic.data_serializer import DataSerializer
from logic.note_logic import Note

if __name__ == "__main__":
    note = Note("Пример заметки", "Текст заметки", ["Python", "заметка"])
    print(note.to_dict())

    notes = [note.to_dict()]
    DataSerializer.save_to_file(notes, "notes.json")

    loaded_notes = DataSerializer.load_from_file("notes.json")
    print(loaded_notes)
