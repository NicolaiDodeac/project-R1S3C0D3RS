from rich.prompt import Prompt
from helpers.rich_output import success_message, error_message, info_message
from contacts.models import Record, Phone, Birthday
from .validation import is_valid_email


def ask_name_and_phone():
    while True:
        response = Prompt.ask("[bold green]Введіть ім'я та номер телефону (10 цифр), або 'exit' для виходу[/bold green]")
        if response.lower() == "exit":
            return None, None
        try:
            name, phone = response.strip().split()
            phone_obj = Phone(phone)  # Валідатор спрацює тут
            return name.capitalize(), phone_obj.value
        except ValueError:
            error_message("Невірне значення. Телефон має містити 10 цифр.")

def ask_birthday():
    while True:
        response = Prompt.ask("[bold green]Введіть день народження (ДД.ММ.РРРР) або 'skip'[/bold green]")
        if response.lower() == "skip":
            return None
        try:
            bday_obj = Birthday(response)
            return bday_obj.value
        except ValueError:
            error_message("Невірний формат. Введіть у форматі ДД.ММ.РРРР.")

def ask_email():
    while True:
        response = Prompt.ask("[bold green]Введіть email або 'skip'[/bold green]")
        if response.lower() == "skip":
            return None
        if is_valid_email(response):
            return response
        else:
            error_message("Невірний email. Спробуйте ще раз.")
