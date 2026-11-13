
import secrets
import string
import hashlib

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich import box

console = Console()


def display_banner():
    console.print(
        Panel(
            "[bold cyan]PASSWORD GENERATOR & SHA-256 HASHER[/bold cyan]\n"
            "[white]Secure Password Generation & Cryptographic Hashing[/white]",
            border_style="cyan",
            box=box.DOUBLE
        )
    )


# Generate a secure random password
def generate_password(length):

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    # Guarantee at least one character from each category
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the remaining positions securely
    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Calculate SHA-256 hash
def calculate_hash(text):

    encoded_text = text.encode('utf-8')

    hash_object = hashlib.sha256(encoded_text)

    return hash_object.hexdigest()


# Main application
def main():

    display_banner()

    while True:

        console.print("\n[bold yellow]MAIN MENU[/bold yellow]")

        console.print("[cyan]1.[/cyan] Generate Secure Password")
        console.print("[cyan]2.[/cyan] Calculate SHA-256 Hash")
        console.print("[cyan]3.[/cyan] Exit")

        choice = Prompt.ask(
            "\n[bold green]Select an option[/bold green]",
            choices=["1", "2", "3"]
        )

        if choice == "1":

            length = IntPrompt.ask(
                "\n[bold]Enter password length[/bold]",
                default=16
            )

            if length < 4:
                console.print(
                    "[bold red]Error:[/bold red] Minimum length is 4."
                )
                continue

            password = generate_password(length)

            table = Table(
                title="Generated Secure Password",
                box=box.ROUNDED,
                border_style="green"
            )

            table.add_column("Property", style="cyan")
            table.add_column("Value", style="white")

            table.add_row("Password", f"[bold green]{password}[/bold green]")
            table.add_row("Length", str(length))

            console.print(table)

            console.print(
                "[green]Password generated successfully![/green]"
            )

        elif choice == "2":

            text = Prompt.ask(
                "\n[bold]Enter text to hash[/bold]",
                password=False
            )

            hash_value = calculate_hash(text)

            console.print(
                Panel(
                    f"[bold cyan]Original Text:[/bold cyan]\n{text}\n\n"
                    f"[bold yellow]SHA-256 Hash:[/bold yellow]\n"
                    f"[white]{hash_value}[/white]",
                    title="Hash Result",
                    border_style="cyan"
                )
            )

        elif choice == "3":

            console.print(
                "\n[bold green]Thank you for using the tool![/bold green]"
            )
            break


if __name__ == "__main__":
    main()
