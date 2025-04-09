from contacts.models import AddressBook, Record
from helpers.decorators import input_error
from rich.console import Console
from rich.table import Table
from helpers.rich_output import success_message, error_message

console = Console()


def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 1:
        return "Введіть ім'я і телефон"
    name, phone, *_ = args
    record = book.find(name.lower())
    message = "Контакт оновлено."
    if not record:
        record = Record(name.capitalize())
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
    return (
        f"{name}: {'; '.join(p.value for p in record.phones)}"
        if record
        else f"Контакт '{name}' не знайдено"
    )


@input_error
def show_all(book):
    if not book.data:
        console.print("[bold red]📭 Контакти відсутні[/bold red]")
        return

    table = Table(title="📒 Список контактів", show_lines=True)
    table.add_column("Ім’я", style="bold magenta")
    table.add_column("Телефони", style="green")
    table.add_column("День народження", style="cyan")
    table.add_column("Email", style="blue")

    for record in book.data.values():
        try:
            name = record.name.value.capitalize()
            phones = "; ".join(p.value for p in record.phones)
            bday = (
                record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "—"
            )
            email = record.email if record.email else "—"
            table.add_row(name, phones, bday, email)
        except Exception as e:
            console.print(f"[bold red]⚠️ Помилка при обробці запису: {e}[/bold red]")

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
def add_email(args, book):
    name, email = args
    record = book.find(name.lower())
    if record:
        record.add_email(email)
        return f"📧 Email для {name} оновлено: {email}"
    return f"Контакт '{name}' не знайдено"


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name.lower())
    return (
        f"{name}: {record.birthday.value.strftime('%d.%m.%Y')}"
        if record and record.birthday
        else f"Немає дати народження"
    )


@input_error
def birthdays(args, book):
    days = int(args[0]) if args else 7
    result = book.get_upcoming_birthdays(days=days)
    return (
        "\n".join(f"{i['name']}: {i['congratulation_date']}" for i in result)
        or "Немає днів народження найближчим часом"
    )


@input_error
def findOne(dataFind, param, book):
    record = None
    match param:
        case "1":
            record = book.find(dataFind.lower())
        case "2":
            for contact in book.data.values():
                if any(dataFind in phone.value for phone in contact.phones):
                    record = contact
                    break
        case "3":
            for contact in book.data.values():
                if dataFind in contact.email:
                    print(contact.email)
                    record = contact
                    break
        case "4":
            for contact in book.data.values():
                if (
                    contact.birthday
                    and contact.birthday.value.strftime("%d.%m.%Y") == dataFind
                ):

                    record = contact
                    break
        case _:
            return "❌ Невірний параметр для пошуку"

    return (
        f"Контакт знайдено: {record}"
        if record
        else f"Контакт з параметром '{dataFind}' не знайдено"
    )


@input_error
def deleteOne(param, book, name):
    match param:
        case "1":
            del book.data[name]
            success_message(f"✅ Контакт {name} успішно видалено!")
        case "2":
            record = book.find(name.lower())
            phone = input("Введіть номер телефону для видалення: ")
            for record in book.data.values():
                if any(phone.value in phone.value for phone in record.phones):
                    try:
                        record.remove_phone(phone)
                        success_message(f"✅ Номер {phone} успішно видалено у {name}!")
                    except ValueError:
                        error_message(f"❌ Номер {phone} не знайдено у {name}!")
                    break
        case "3":
            record = book.find(name.lower())
            for record in book.data.values():
                record.remove_email()
            success_message(f"✅ Пошти у {name} немає!")
        case "4":
            record = book.find(name.lower())
            for record in book.data.values():
                record.remove_birthday()
            success_message(f"✅ День народження у {name} не записаний!")
