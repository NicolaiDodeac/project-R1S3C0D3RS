from processing import *
from data import *
from classes import *

def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))# добавити валідацію

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "help":
            print("""
Available commands:
  add [name] [phone] - Add new contact
  change [name] [old phone] [new phone] - Edit phone number
  phone [name] - Show phone numbers for contact
  all - Show all contacts
  add-birthday [name] [DD.MM.YYYY] - Add birthday
  show-birthday [name] - Show contact's birthday
  birthdays - List upcoming birthdays
  hello - Say hello
  exit / close - Exit the program
    """)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


