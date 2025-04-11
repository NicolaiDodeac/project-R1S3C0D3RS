from contacts.models import AddressBook, Record
from helpers.decorators import input_error
from rich.console import Console
from rich.table import Table
from helpers.rich_output import success_message, error_message
from datetime import datetime

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

def add_phone_command(args, book: AddressBook):
    name, new_phone = args
    record = book.find(name.lower())
    if not record:
        return f"Контакт '{name}' не знайдено"
    try:
        record.add_phone(new_phone)
        return f"📞 Додано номер {new_phone} до {name}"
    except ValueError:
        return "❌ Номер телефону повинен містити 10 цифр"


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
        if record and record.phones
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


def add_email(args, book):
    name, email = args
    record = book.find(name.lower())
    if not record:
        return f"Контакт '{name}' не знайдено"
    
    try:
        record.add_email(email)
        return f"📧 Email для {name} оновлено: {email}"
    except ValueError as e:
        return str(e)


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name.lower())
    return (
        f"{name}: {record.birthday.value.strftime('%d.%m.%Y')}"
        if record and record.birthday
        else f"Немає дати народження"
    )

def get_day_word(n):
    return "день" if n == 1 else "дні" if 2 <= n <= 4 else "днів"

@input_error
def birthdays(args, book):
    days = int(args[0]) if args else 7
    today = datetime.today().date()
    result = book.get_upcoming_birthdays(days=days)

    if not result:
        return "Немає днів народження найближчим часом"

    formatted = []
    for item in result:
        real_birthday = item["original_birthday"]
        congratulation_date = datetime.strptime(item["congratulation_date"], "%d.%m.%Y").date()
        delta_days = (congratulation_date - today).days
        day_word = get_day_word(delta_days)
        formatted.append(
            f"{item['name']}: {item['original_birthday'].strftime('%d.%m.%Y')} — День народження через {delta_days} {day_word}"
        )

    return "\n".join(formatted)


@input_error
def findOne(dataFind, param, book):
    record = None
    match param:
        case "1":
            res = []
            res.append(book.find(dataFind.lower()))
            record = res
        case "2":
            res = []
            for contact in book.data.values():
                if any(dataFind in phone.value for phone in contact.phones):
                    res.append(contact)
                record = res
        case "3":
            res = []
            for contact in book.data.values():
                if dataFind in contact.email:
                    print(contact.email)
                    res.append(contact)

                record = res
        case "4":
            res = []
            for contact in book.data.values():
                if (
                    contact.birthday
                    and contact.birthday.value.strftime("%d.%m.%Y") == dataFind
                ):

                    res.append(contact)
            record = res

        case _:
            return "❌ Невірний параметр для пошуку"
    table = Table(title="📒 Список контактів", show_lines=True)
    table.add_column("Ім’я", style="bold magenta")
    table.add_column("Телефони", style="green")
    table.add_column("День народження", style="cyan")
    table.add_column("Email", style="blue")
    if isinstance(record, list):
        if record:
            for r in record:
                name = r.name.value.capitalize()
                phones = "; ".join(p.value for p in r.phones)
                bday = r.birthday.value.strftime("%d.%m.%Y") if r.birthday else "—"
                email = r.email if r.email else "—"
                table.add_row(name, phones, bday, email)
            return table
        return f"Контакти з параметром '{dataFind}' не знайдено"
    else:
        return (
            f"Контакт знайдено: {record}"
            if record
            else f"Контакт з параметром '{dataFind}' не знайдено"
        )


@input_error
def deleteOne(param, book, name):
    match param:
        case "1":
            del book.data[name.lower()]
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
