from rich.table import Table
from rich.console import Console

console = Console()


def show_help():
    table = Table(title="📚 Довідка: доступні команди", show_lines=True)
    table.add_column("Команда", style="bold cyan", justify="left")
    table.add_column("Опис", style="white", justify="left")

    table.add_row("hello", "Привітатися з ботом")
    table.add_row("add", "Додати новий контакт або нотатку")
    table.add_row("add-phone", "Додати новий або додатковий номер телефону")
    table.add_row("update-phone", "Змінити номер телефону")
    table.add_row("phone [name]", "Показати номери телефону для контакту")
    table.add_row("update-birthday [name] [DD.MM.YYYY]", "Додати дату народження")
    table.add_row("show-birthday [name]", "Показати день народження контакту")
    table.add_row("birthdays", "Показати дні народження на наступному тижні")
    table.add_row("update-email [name] [email]", "Додати або змінити email")
    table.add_row("all", "Показати всі контакти")
    table.add_row("find", "Пошук за якимось одним з параметрів")
    table.add_row("find-note", "Пошук нотаток за ключем або тегом")
    table.add_row("delete", "Видалити нотатку, контакт цілком чи окремий параметр")
    table.add_row("note", "Створити нотатку")
    table.add_row("change-note", "Змінити нотатку")
    table.add_row("exit / close", "Вийти з програми")

    console.print(table)
