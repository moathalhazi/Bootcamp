
import socket
import time
import ipaddress
import csv
import errno

from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich import box


console = Console()

# Scanner configuration
START_PORT = 1
END_PORT = 1024
MAX_WORKERS = 50
TIMEOUT = 1

# Common TCP services
SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-ALT",
}


def display_banner():
    console.print(
        Panel(
            "[bold cyan]MULTITHREADED PORT SCANNER[/bold cyan]\n"
            "[dim]Network Security & Reconnaissance Tool[/dim]\n"
            "[green]TCP Port Scanning[/green]",
            border_style="cyan",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )


def scan_port(target, port):
    """Scan one TCP port and return its status."""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((target, port))

            if result == 0:
                return port, "OPEN"

            if result == errno.ECONNREFUSED or result == 10061:
                return port, "CLOSED"

            return port, "FILTERED"

    except (socket.timeout, TimeoutError):
        return port, "FILTERED"

    except OSError:
        return port, "FILTERED"


def get_service(port):
    """Return the common service name."""
    return SERVICES.get(port, "Unknown")


def save_results(target, results):
    """Export scan results to CSV."""

    filename = f"scan_{target.replace('.', '_')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Port", "Service", "Status"])

        for port, status in sorted(results):
            writer.writerow([
                port,
                get_service(port),
                status
            ])

    return filename


def main():

    display_banner()

    target = console.input(
        "\n[bold yellow][?] Enter Target IP: [/bold yellow]"
    ).strip()

    # Validate target
    try:
        ipaddress.ip_address(target)

    except ValueError:
        console.print(
            "\n[bold red][!] Invalid IP address![/bold red]"
        )
        return

    total_ports = END_PORT - START_PORT + 1

    # Display scan configuration
    config = Table(
        title="SCAN CONFIGURATION",
        box=box.ROUNDED,
        border_style="cyan",
    )

    config.add_column("Setting", style="bold cyan")
    config.add_column("Value", style="white")

    config.add_row("Target IP", target)
    config.add_row("Port Range", f"{START_PORT}-{END_PORT}")
    config.add_row("Total Ports", str(total_ports))
    config.add_row("Max Threads", str(MAX_WORKERS))
    config.add_row("Timeout", f"{TIMEOUT} second(s)")
    config.add_row("Protocol", "TCP")

    console.print(config)

    console.print(
        "\n[bold green][+] Starting port scan...[/bold green]\n"
    )

    start_time = time.perf_counter()

    results = []

    open_count = 0
    closed_count = 0
    filtered_count = 0

    # Parallel scanning with progress bar
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        futures = {
            executor.submit(scan_port, target, port): port
            for port in range(START_PORT, END_PORT + 1)
        }

        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("({task.completed}/{task.total})"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:

            task = progress.add_task(
                "Scanning ports...",
                total=total_ports
            )

            for future in as_completed(futures):

                port, status = future.result()

                results.append((port, status))

                if status == "OPEN":
                    open_count += 1

                elif status == "CLOSED":
                    closed_count += 1

                else:
                    filtered_count += 1

                progress.advance(task)

    elapsed_time = time.perf_counter() - start_time

    # Display open ports
    console.print("\n")

    open_table = Table(
        title="OPEN PORTS DISCOVERED",
        box=box.ROUNDED,
        border_style="green",
    )

    open_table.add_column("PORT", justify="center", style="bold cyan")
    open_table.add_column("SERVICE", style="white")
    open_table.add_column("STATUS", justify="center")

    for port, status in sorted(results):

        if status == "OPEN":
            open_table.add_row(
                str(port),
                get_service(port),
                "[bold green]OPEN[/bold green]"
            )

    if open_count == 0:
        open_table.add_row("-", "-", "[yellow]No open ports[/yellow]")

    console.print(open_table)

    # Final statistics
    summary = Table(
        title="SCAN SUMMARY",
        box=box.DOUBLE_EDGE,
        border_style="cyan",
    )

    summary.add_column("Metric", style="bold cyan")
    summary.add_column("Result", justify="center")

    summary.add_row("Total Scanned", str(total_ports))
    summary.add_row("Open Ports", f"[bold green]{open_count}[/bold green]")
    summary.add_row("Closed Ports", f"[red]{closed_count}[/red]")
    summary.add_row("Filtered / No Response", f"[yellow]{filtered_count}[/yellow]")
    summary.add_row("Threads Used", str(MAX_WORKERS))
    summary.add_row("Time Elapsed", f"{elapsed_time:.2f} seconds")

    console.print(summary)

    # Save CSV
    filename = save_results(target, results)

    console.print(
        Panel(
            f"[bold green]SCAN COMPLETED SUCCESSFULLY[/bold green]\n\n"
            f"[cyan]Results saved to:[/cyan] {filename}",
            border_style="green",
            box=box.ROUNDED,
        )
    )


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        console.print("\n[bold red][!] Scan interrupted by user.[/bold red]")
