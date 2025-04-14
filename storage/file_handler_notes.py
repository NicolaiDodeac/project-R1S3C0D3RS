import os
import csv
from notes.models import Note
from datetime import datetime

FILENAME = os.path.join("storage", "data", "notes.csv")


def save_notes(notes, filename=FILENAME):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ✅ Гарантує шлях

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Назва", "Нотатка", "Тег", "Дата"])
        for note in notes:
            writer.writerow([
                note.name_note,
                note.body_note,
                note.tag_note or "",
                note.date_created.strftime("%Y-%m-%d %H:%M")
            ])

def load_notes(filename=FILENAME):
    notes = []
    if not os.path.exists(filename):
        return notes
    with open(filename, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            note = Note(
                name_note=row["Назва"],
                body_note=row["Нотатка"],
                tag_note=row["Тег"] if row["Тег"] else None
            )
            note.date_created = datetime.strptime(row["Дата"], "%Y-%m-%d %H:%M")
            notes.append(note)
    return notes
