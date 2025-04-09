from rich.table import Table
from rich.console import Console

console = Console()

def show_help():
    table = Table(title="📚 Довідка: доступні команди", show_lines=True)
    table.add_column("Команда", style="bold cyan", justify="left")
    table.add_column("Опис", style="white", justify="left")

    table.add_row("add name phone", "Додати новий контакт або телефон до існуючого")
    table.add_row("change [name] [old_phone] [new_phone]", "Змінити номер телефону")
    table.add_row("phone [name]", "Показати номери телефону для контакту")
    table.add_row("all", "Показати всі контакти")
    table.add_row("add-birthday [name] [DD.MM.YYYY]", "Додати дату народження")
    table.add_row("show-birthday [name]", "Показати день народження контакту")
    table.add_row("birthdays", "Показати дні народження на наступному тижні")
    table.add_row("hello", "Привітатися з ботом")
    table.add_row("exit / close", "Вийти з програми")
    table.add_row("add-email [name] [email] — додати або змінити email")

    console.print(table)
