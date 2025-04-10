from notes.models import Note
from datetime import datetime
from rich.prompt import Prompt
from storage.file_handler_notes import save_notes, load_notes
from rich.console import Console

console = Console()
notes = load_notes()

def add_notes ():
    name_note = Prompt.ask("[bold green]Введіть назву нотатки:[/bold green]")
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
    save_notes(notes)

    return f"✅ Нотатку '{name_note}' успішно збережено!"

def show_notes():
    if not notes:
        print("У тебе ще немає жодної нотатки")
    else:
        for note in notes: print(note)