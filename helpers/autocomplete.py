from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from contacts.models import AddressBook
from helpers.constants import COMMANDS

style = Style.from_dict({
    "completion-menu.completion": "bg:#21252b #abb2bf",
    "completion-menu.completion.current": "bg:#61afef #000000 bold",
})

command_completer = WordCompleter(COMMANDS, ignore_case=True)
session = PromptSession(completer=command_completer, style=style)

def get_user_command():
    return session.prompt(">> Введіть команду: ")

def get_name_completer(book: AddressBook):
    names = list(book.data.keys())
    return WordCompleter(names, ignore_case=True)

def get_phone_completer(book: AddressBook, name: str):
    phones = []
    record = book.find(name.lower())
    if record:
        phones = [p.value for p in record.phones]
    return WordCompleter(phones, ignore_case=True)

def get_prompt(completer, message="Введіть значення: "):
    local_session = PromptSession(completer=completer, style=style)
    return local_session.prompt(message)
