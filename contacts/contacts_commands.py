from contacts.models import AddressBook, Record
from helpers.decorators import input_error
from rich.console import Console
from rich.table import Table

def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Введіть ім'я і телефон"
    name, phone, *_ = args
    record = book.find(name.lower())
    message = "Контакт оновлено."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = f"Додано новий контакт {name}"
    record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name.lower())
    if record and record.edit_phone(old_phone, new_phone):
        return f"Оновлено номер для {name}"
    return f"Контакт або номер не знайдено"

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name.lower())
    return f"{name}: {'; '.join(p.value for p in record.phones)}" if record else f"Контакт '{name}' не знайдено"

from rich.console import Console
from rich.table import Table

console = Console()

@input_error
def show_all(book):
    if not book.data:
        console.print("[bold red]📭 Контакти відсутні[/bold red]")
        return

    table = Table(title="📒 Список контактів", show_lines=True)

    table.add_column("Ім’я", style="bold magenta")
    table.add_column("Телефони", style="green")
    table.add_column("День народження", style="cyan")

    for record in book.data.values():
        name = record.name.value
        phones = "; ".join(p.value for p in record.phones)
        bday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "—"
        table.add_row(name, phones, bday)

    console.print(table)

@input_error
def add_birthday(args, book):
    name, bday = args
    record = book.find(name.lower())
    if record:
        record.add_birthday(bday)
        return f"Додано день народження для {name}"
    return f"Контакт '{name}' не знайдено"

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name.lower())
    return f"{name}: {record.birthday.value.strftime('%d.%m.%Y')}" if record and record.birthday else f"Немає дати народження"

@input_error
def birthdays(args, book):
    result = book.get_upcoming_birthdays()
    return "\n".join(f"{i['name']}: {i['congratulation_date']}" for i in result) or "Немає днів народження найближчим часом"
