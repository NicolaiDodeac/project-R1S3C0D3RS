from contacts.contacts_commands import *
from storage.file_handler_contacts import load_data, save_data
from helpers.rich_output import (
    success_message,
    error_message,
    info_message,
    print_title,
)
from rich.prompt import Prompt
from helpers.help_text import show_help
from contacts.contact_flow import ask_name_and_phone, ask_birthday, ask_email
from notes.notes_commands import add_notes, show_notes


def main():
    book = load_data()
    print_title("📔 Welcome to the assistant bot!")

    while True:
        user_input = Prompt.ask("[bold green]Введіть команду[/bold green]")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            save_data(book)
            success_message("👋 До побачення!")
            break

        elif command == "hello":
            info_message("🖐 Як я можу вам допомогти?")

        elif command == "add":
            action = (
                Prompt.ask(
                    "[bold green]Що ви хочете додати? ('contact' або 'note')[/bold green]"
                )
                .strip()
                .lower()
            )

            if action == "note":
                result = add_notes()
                info_message(result)

            if action == "contact":
                name, phone = ask_name_and_phone()
                if not name:
                    continue

                record = book.find(name.lower())
                if not record:
                    record = Record(name)
                    book.add_record(record)
                record.add_phone(phone)

                birthday = ask_birthday()
                if birthday:
                    record.add_birthday(birthday.strftime("%d.%m.%Y"))

                email = ask_email()
                if email:
                    record.add_email(email)

                save_data(book)  # Одразу зберігаємо після успішного додавання
                success_message(f"✅ Контакт {name} успішно збережено!")
            else:
                error_message("⚠️ Доступні варіанти: 'contact' або 'note'")

        elif command == "update-phone":
            result = change_contact(args, book)
            success_message(result)

        elif command == "phone":
            result = show_phone(args, book)
            info_message(result)

        elif command == "all":
            show_all(book)

        elif command == "update-birthday":
            result = add_birthday(args, book)
            success_message(result)

        elif command == "update-email":
            result = add_email(args, book)
            success_message(result)

        elif command == "show-birthday":
            result = show_birthday(args, book)
            info_message(result)

        elif command == "birthdays":
            result = birthdays(args, book)
            info_message(result)
        elif command == "find":
            table = Table(title="Доступні параметри для пошуком:", show_lines=True)
            table.add_column("Номер команди", style="bold cyan", justify="left")
            table.add_column("Опис", style="white", justify="left")
            table.add_row("1", "Пошук за іменем або частиною імені (name)")
            table.add_row("2", "Пошук за номером телефону або частиною номера (phone)")
            table.add_row("3", "Пошук за поштою або частиною пошти (email)")
            table.add_row("4", "Пошук за днем народження (birthday)")
            console.print(table)
            param = input("Введіть параметр для пошуку: ")
            if not param or param not in ["1", "2", "3", "4"]:
                error_message("❌ Невірний параметр. Спробуйте ще раз.")
                continue
            dataFind = input("Введіть дані для пошуку: ")
            result = findOne(dataFind, param, book)
            console.print(result)
        elif command == "delete":
            name = input("Введіть ім'я контакту для взаємодії: ")
            record = book.find(name.lower())
            if record:
                table = Table(
                    title="Доступні параметри для видалення:", show_lines=True
                )
                table.add_column("Номер команди", style="bold cyan", justify="left")
                table.add_column("Опис", style="white", justify="left")
                table.add_row("1", "Видалити цілий контакт")
                table.add_row("2", "Видалити номер телефону")
                table.add_row("3", "Видалити пошту")
                table.add_row("4", "Видалити день народження")
                console.print(table)
                param = input("Введіть параметр для видалення: ")
                if not param or param not in ["1", "2", "3", "4"]:
                    error_message("❌ Невірний параметр. Спробуйте ще раз.")
                    continue
                deleteOne(param, book, name)
                if not name:
                    error_message("❌ Введіть ім'я контакту для видалення.")
                    continue
            else:
                error_message(f"❌ Контакт {name} не знайдено.")
        #  Oleksandr_add_notes
        elif command == "note":
            result = add_notes()
            info_message(result)

        elif command == "show-note":
            result = show_notes()
            info_message(result)

        elif command == "help":
            show_help()

        else:
            error_message("❌ Невідома команда. Напишіть 'help' для списку команд.")


if __name__ == "__main__":

    main()
