from notes.models import Note
from datetime import datetime

notes = []

def add_notes ():
    name_note = input("Введіть назву нотатки: ")
    body_note = input("Введіть текст нотатки: ")
    tag_note = input("Чи хочете додати тег для своєї нотакти? Y/N: ")

    if tag_note.lower() == "y":
        tag_note = input(f"Введіть світ тег для нотатки {name_note} ")
    else:
        tag_note = None

    # note_dict ={"Ім'я нотатки": name_note,
    #             "Нотатка": body_note,
    #             "Тег": tag_note,
    #             "Додано": datetime.now()
    # }
    # notes.append(note_dict)
    note = Note(name_note, body_note, tag_note)
    notes.append(note)

def show_notes():
    if not notes:
        print("У тебе ще немає жодної нотатки")
    else:
        for note in notes: print(note)