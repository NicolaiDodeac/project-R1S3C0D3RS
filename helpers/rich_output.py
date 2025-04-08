from rich import print
from rich.panel import Panel
from rich.console import Console

console = Console()

def success_message(message: str):
    print(Panel(f"[green]{message}[/green]", title="✅ Успіх"))

def error_message(message: str):
    print(Panel(f"[red]{message}[/red]", title="❌ Помилка"))

def info_message(message: str):
    print(Panel(f"[cyan]{message}[/cyan]", title="📌 Інфо"))

def print_title(title: str):
    console.rule(f"[bold magenta]{title}[/bold magenta]")
