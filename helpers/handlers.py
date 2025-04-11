
from rich.prompt import Prompt
from helpers.rich_output import success_message,info_message, error_message
from contacts.contacts_commands import change_contact, add_email, add_birthday, add_contact, add_phone_command, show_phone, show_birthday
from helpers.autocomplete import get_prompt, get_name_completer, get_phone_completer

def handle_add_birthday(book):
    name = get_prompt(get_name_completer(book), "Введіть ім'я контакту: ")
    
    while True:
        bday = Prompt.ask("Введіть дату народження (ДД.ММ.РРРР)")
        result = add_birthday([name, bday], book)
        if "Додано день народження" in result:
            success_message(result)
            return
        else:
            error_message(result)


def handle_show_birthday(book):
    name = get_prompt(get_name_completer(book), "Введіть ім'я контакту: ")
    result = show_birthday([name], book)
    info_message(result)

def handle_show_phone(book):
    name = get_prompt(get_name_completer(book), "Введіть ім'я контакту: ")
    result = show_phone([name], book)
    info_message(result)

def handle_update_phone(book):
    name = get_prompt(get_name_completer(book), "Введіть ім'я: ")
    old_phone = get_prompt(get_phone_completer(book, name), "Введіть старий номер телефону: ")
    new_phone = Prompt.ask("Введіть новий номер телефону ")
    result = change_contact([name, old_phone, new_phone], book)
    success_message(result)

def handle_update_email(book):
    name = get_prompt(get_name_completer(book), "Введіть ім'я контакту: ")
    while True:
        email = Prompt.ask("Введіть новий email")
        result = add_email([name, email], book)
        if "Email" in result:
            success_message(result)
            return
        else:
            error_message(result)

def handle_add_phone(book):
    name = get_prompt(get_name_completer(book), "Введіть ім’я контакту, до якого додати номер:")
    while True:
        phone = Prompt.ask("Введіть новий номер телефону")
        result = add_phone_command([name, phone], book)
        if "Додано" in result:
            success_message(result)
            return
        else:
            error_message(result)