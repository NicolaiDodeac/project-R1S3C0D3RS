from notes.models import Note
from datetime import datetime
from rich.prompt import Prompt
from storage.file_handler_notes import save_notes, load_notes
from rich.console import Console
from rich.table import Table
from helpers.rich_output import console


notes = load_notes()


def add_notes():
    name_note = Prompt.ask("[bold green]Введіть назву нотатки[/bold green]")
    body_note = Prompt.ask("[bold blue]Введіть текст нотатки[/bold blue]")
    tag_note = Prompt.ask("[bold green]Введіть тег або 'skip'[/bold green]")

    if tag_note.lower() == "skip":
        tag_note = None
    else:
        tag_note = tag_note.strip()
        if not tag_note.startswith("#"):
            tag_note = f"#{tag_note}"

    note = Note(name_note, body_note, tag_note)
    notes.append(note)
    save_notes(notes)
    return f"Нотатку '{name_note}' успішно додано!"


def show_notes():
    if not notes:
        return "У тебе ще немає жодної нотатки"

    table = Table(title="Перелік твоїх нотаток", show_lines=True)

    table.add_column("№п/п", style="white", justify="center")
    table.add_column("Назва", style="cyan", justify="center")
    table.add_column("Текст", style="white", justify="center")
    table.add_column("Тег", style="blue", justify="center")
    table.add_column("Дата створення", style="green", justify="center")

    for index, note in enumerate(notes, start=1):
        table.add_row(
            str(index),
            note.name_note,
            note.body_note,
            note.tag_note if note.tag_note else "-",
            note.date_created.strftime("%d.%m.%Y"),
        )

    return table

def find_note():
    keyword = Prompt.ask("[bold green]Введіть ключове слово або #тег[/bold green]").lower()

    found = []
    for note in notes:
        if (
            keyword in note.name_note.lower()
            or keyword in note.body_note.lower()
            or (note.tag_note and keyword in note.tag_note.lower())
        ):
            found.append(note)

    if not found:
        return "🔍 За запитом нічого не знайдено."

    table = Table(title=f"🔎 Результати пошуку за '{keyword}'", show_lines=True)
    table.add_column("№", style="white", justify="center")
    table.add_column("Назва", style="cyan", justify="center")
    table.add_column("Текст", style="white", justify="center")
    table.add_column("Тег", style="blue", justify="center")
    table.add_column("Дата створення", style="green", justify="center")

    for idx, note in enumerate(found, start=1):
        table.add_row(
            str(idx),
            note.name_note,
            note.body_note,
            note.tag_note or "-",
            note.date_created.strftime("%d.%m.%Y"),
        )
    return table
