from contacts.contacts_commands import *
from storage.file_handler_contacts import load_data, save_data
from helpers.rich_output import success_message, error_message, info_message, print_title
from rich.prompt import Prompt
from helpers.help_text import show_help

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
            result = add_contact(args, book)
            success_message(result)

        elif command == "change":
            result = change_contact(args, book)
            success_message(result)

        elif command == "phone":
            result = show_phone(args, book)
            info_message(result)

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":
            result = add_birthday(args, book)
            success_message(result)

        elif command == "show-birthday":
            result = show_birthday(args, book)
            info_message(result)

        elif command == "birthdays":
            result = birthdays(args, book)
            info_message(result)

        elif command == "help":
            show_help()
        else:
            error_message("❌ Невідома команда. Напишіть 'help' для списку команд.")


if __name__ == "__main__":
    main()
