from classes import *
from helpers import input_error

def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 1:
        return "Error: Please provide a name and phone number along with command (e.g. add Jane 8099640..)."
    name, phone,*_ = args
    name = name.strip().lower()
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact '{name}' added with phone number '{phone}'."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    if len(args) != 3:
        return "Error: Please provide a name old phone and new phone number along with command (e.g. change Jane 0123456789 0987654321..)."
    name, old_phone, new_phone = args
    name = name.strip().lower()
    record = book.find(name)
    if record:
        if record.edit_phone(old_phone, new_phone):
            return f"Updated {name}'s phone from {old_phone} to {new_phone}."
        else:
            return f"Phone number {old_phone} not found for {name}."
    else:
        return f"Contact '{name}' not found."
        
@input_error
def show_phone(args, book):
    if len(args) != 1:
        return "Error: Please provide the contact name."
    name = args[0].strip().lower()
    record = book.find(name)
    if record:
        return f"{name}: {'; '.join(p.value for p in record.phones)}"
    else:
        return f"Contact '{name}' not found."


@input_error
def show_all(book):
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book):
    name, b_day = args
    name = name.strip().lower()
    record = book.find(name)
    if record:
        record.add_birthday(b_day)
        return f"Birthday for {name} added."
    return f"Contact '{name}' not found."


@input_error
def show_birthday(args, book):
    name = args[0]
    name = name.strip().lower()
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
    return f"No birthday set for {name}"
   

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No bithdays this week"
    return "\n".join([f"{item['name']}: {item['congratulation_date']}" for item in upcoming])
