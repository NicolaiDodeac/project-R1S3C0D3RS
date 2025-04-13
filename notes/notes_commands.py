from notes.models import Note
from datetime import datetime
from rich.prompt import Prompt
from storage.file_handler_notes import save_notes, load_notes
from rich.console import Console
from rich.table import Table
from helpers.rich_output import console
from helpers.rich_output import error_message, success_message, info_message


notes = load_notes()


def add_notes():
    while True:
        name_note = Prompt.ask("[bold green]Введіть назву нотатки[/bold green]")
        for note in notes: #Перевірка на унікальеість імені
            if note.name_note.lower() == name_note.lower():
                error_message (f"Нотатка з назвою {name_note} вже існує, введіть інше імя")
                break
        else:
            break
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

def dell_note(): #видаляти нотатку модна по назві
    keyword = Prompt.ask("[bold green]Введіть назву нотатки[/bold green]").lower()
    for note in notes:
        if keyword in note.name_note.lower():
            confirm = Prompt.ask(f"[bold red]Ви точно хочете видалити '{note.name_note}'? (Y/N)[/bold red]")
            if confirm.lower() == "y":
                notes.remove(note)
                save_notes(notes)
                success_message(f"Нотатка з ім\'м {keyword} видалена зі списку нотаток")
                return
            else:
                info_message("Видалення скасовано")
                return
    info_message(f"Нотатка з назвою {keyword} не існує")

def change_note():
    question = Prompt.ask("[bold green]За яким параметром будемо шукати нотатку? Натиcни за назвою - 1. За тегом - 2[/bold green]")
    if question == "1":
        answer_1 = Prompt.ask("[bold green]Введіть назву нотатки[/bold green]")
        for note in notes:
            if answer_1 in note.name_note.lower():
                info_message(f"Знайдено нотатку з назвою: {note.name_note}")
                new_body = Prompt.ask("Введіть новий текст нотатки:")
                note.body_note = new_body
                save_notes(notes)
                success_message(f"Нотатка з ім\'м {answer_1} умпішно відредаговано")
                return
        info_message("Нотатки за такою назвою не існує. Ти можеш створти нову нотатку. Скористайся відповідною командою ")
    
    elif question == "2":
        answer_2 = Prompt.ask("[bold green]Введіть тег починаючи з #[/bold green]")
        result = []
        for note in notes:
            if note.tag_note and answer_2 == note.tag_note:
                result.append(note)
        
        if not result:
            info_message("Нотаток з таким тегом не знайдено.")
            return
        

        # Виводимо знайдені нотатки в таблиці
        table = Table(title="Знайдені нотатки", show_lines=True)
        table.add_column("№", justify="center")
        table.add_column("Назва", style="cyan")
        table.add_column("Текст", style="white")

        for idx, note in enumerate(result, start=1):
            table.add_row(str(idx), note.name_note, note.body_note)

        console.print(table)

        # Запит номера нотатки для редагування
        number = Prompt.ask("[bold green]Введіть номер нотатки для редагування[/bold green]")

        try:
            note_to_edit = result[int(number) - 1]
        except (ValueError, IndexError):
            error_message("Некоректний номер нотатки.")
            return

        new_body = Prompt.ask("[bold green]Введіть новий текст нотатки[/bold green]")
        note_to_edit.body_note = new_body
        save_notes(notes)
        success_message(f"Нотатка з імʼям '{note_to_edit.name_note}' успішно відредагована!")

    else:
        error_message("Введено некоректний параметр. Спробуйте ще раз.")
        return