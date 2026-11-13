import hashlib
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# Configuration
CHECK_INTERVAL = 3
CHUNK_SIZE = 4096


def calculate_sha256(file_path):
    """Calculate SHA-256 hash of a file using chunks."""

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(CHUNK_SIZE)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None

    except PermissionError:
        console.print("[red]Permission denied: Cannot read file.[/red]")
        return None

    except OSError as error:
        console.print(f"[red]File error: {error}[/red]")
        return None


def display_hash(label, hash_value):
    """Display hash information."""

    table = Table(box=box.ROUNDED)
    table.add_column("Information", style="cyan")
    table.add_column("Value", style="white")

    table.add_row(label, hash_value or "Unavailable")

    console.print(table)


def monitor_file(file_path):

    path = Path(file_path)

    # Validate file
    if not path.is_file():
        console.print("[red]Error: File does not exist![/red]")
        return

    console.print(
        Panel(
            "[bold cyan]FILE INTEGRITY MONITORING (FIM)[/bold cyan]\n"
            "[white]SHA-256 File Integrity Checker[/white]",
            border_style="cyan"
        )
    )

    # Create initial baseline
    baseline_hash = calculate_sha256(path)

    if baseline_hash is None:
        console.print("[red]Unable to create baseline.[/red]")
        return

    console.print("[green]Baseline created successfully![/green]")
    display_hash("Baseline SHA-256", baseline_hash)

    console.print(
        f"\n[yellow]Monitoring started... "
        f"Checking every {CHECK_INTERVAL} seconds.[/yellow]\n"
    )

    alert_active = False

    try:
        while True:

            time.sleep(CHECK_INTERVAL)

            current_hash = calculate_sha256(path)

            # Check if file was deleted or became inaccessible
            if current_hash is None:

                if path.exists():
                    console.print(
                        "[red]CRITICAL: Unable to read the file![/red]"
                    )
                elif not alert_active:
                    console.print(
                        Panel(
                            "[bold red]CRITICAL ALERT![/bold red]\n"
                            "The monitored file has been deleted!",
                            border_style="red"
                        )
                    )
                    alert_active = True

                continue

            # Compare current hash with baseline
            if current_hash != baseline_hash:

                if not alert_active:
                    console.print(
                        Panel(
                            "[bold red]CRITICAL SECURITY ALERT![/bold red]\n"
                            "File modification detected!\n"
                            f"File: {path}",
                            border_style="red"
                        )
                    )

                    display_hash("Original Hash", baseline_hash)
                    display_hash("Current Hash", current_hash)

                    alert_active = True

            else:

                if alert_active:
                    console.print(
                        "[green]File integrity restored to baseline.[/green]"
                    )
                    alert_active = False

                console.print(
                    f"[green]SECURE[/green] | "
                    f"{time.strftime('%H:%M:%S')} | "
                    "No changes detected."
                )

    except KeyboardInterrupt:
        console.print("\n[yellow]Monitoring stopped by user.[/yellow]")


if __name__ == "__main__":

    file_path = input("Enter file path to monitor: ").strip()

    monitor_file(file_path)
