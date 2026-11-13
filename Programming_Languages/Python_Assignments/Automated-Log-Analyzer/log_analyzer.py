
import re
from collections import Counter

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from rich.text import Text
from rich import box


# ==========================================
# AUTOMATED LOG ANALYZER
# Python Security Log Analysis Tool
# ==========================================

console = Console()

LOG_FILE = "access.log"


# Attack Detection Patterns
PATTERNS = {
    "SQL Injection": [
        re.compile(r"union\s+select", re.IGNORECASE),
        re.compile(
            r"'\s*or\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+",
            re.IGNORECASE
        ),
        re.compile(r"information_schema", re.IGNORECASE),
    ],

    "Path Traversal": [
        re.compile(r"\.\./", re.IGNORECASE),
        re.compile(r"%2e%2e%2f", re.IGNORECASE),
        re.compile(r"/etc/passwd", re.IGNORECASE),
    ],

    "Command Injection": [
        re.compile(
            r";\s*(cat|whoami|id|uname)\b",
            re.IGNORECASE
        ),
        re.compile(
            r"\|\s*(cat|whoami|id)\b",
            re.IGNORECASE
        ),
    ],

    "XSS": [
        re.compile(r"<script\b", re.IGNORECASE),
        re.compile(r"javascript\s*:", re.IGNORECASE),
        re.compile(r"onerror\s*=", re.IGNORECASE),
    ],

    "Sensitive File Access": [
        re.compile(r"/\.env(?:\b|[/?])", re.IGNORECASE),
        re.compile(r"wp-config\.php", re.IGNORECASE),
    ]
}


# ==========================================
# Extract IP Address
# ==========================================

def extract_ip(line):

    match = re.search(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        line
    )

    return match.group() if match else "Unknown"


# ==========================================
# Detect Attacks
# ==========================================

def detect_attacks(line):

    detected_attacks = []

    for attack_type, patterns in PATTERNS.items():

        for pattern in patterns:

            if pattern.search(line):
                detected_attacks.append(attack_type)
                break

    return detected_attacks


# ==========================================
# Display Header
# ==========================================

def display_header():

    console.print(
        Panel(
            Text(
                "AUTOMATED LOG ANALYZER",
                justify="center",
                style="bold cyan"
            ),
            subtitle="[bold white]Python Security Analysis Tool[/bold white]",
            border_style="bright_blue",
            padding=(1, 2)
        )
    )


# ==========================================
# Analyze Log File
# ==========================================

def analyze_logs(filename):

    attack_counter = Counter()
    total_lines = 0
    total_attacks = 0
    alerts = []

    try:

        with open(
            filename,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as log_file:

            lines = log_file.readlines()

        total_lines = len(lines)

        if total_lines == 0:
            console.print(
                "\n[bold yellow][!] Log file is empty.[/bold yellow]"
            )
            return

        console.print(
            f"\n[cyan]Target File:[/cyan] [white]{filename}[/white]"
        )

        console.print(
            f"[cyan]Total Lines:[/cyan] [white]{total_lines}[/white]\n"
        )

        # Scan logs with progress bar
        for line_number, line in enumerate(
            track(
                lines,
                description="[bold cyan]Analyzing Logs...",
                console=console
            ),
            start=1
        ):

            detected_attacks = detect_attacks(line)

            for attack_type in detected_attacks:

                ip = extract_ip(line)

                attack_counter[attack_type] += 1
                total_attacks += 1

                alerts.append({
                    "line": line_number,
                    "ip": ip,
                    "attack": attack_type
                })

        # Display Security Alerts
        console.print("\n")

        if alerts:

            alert_table = Table(
                title="SECURITY ALERTS",
                box=box.ROUNDED,
                border_style="red",
                header_style="bold white on dark_red"
            )

            alert_table.add_column("No.", justify="center")
            alert_table.add_column("Line Number", justify="center")
            alert_table.add_column("Source IP", style="cyan")
            alert_table.add_column("Attack Type", style="bold red")

            for index, alert in enumerate(alerts, start=1):

                alert_table.add_row(
                    str(index),
                    str(alert["line"]),
                    alert["ip"],
                    alert["attack"]
                )

            console.print(alert_table)

        else:

            console.print(
                Panel(
                    "[bold green]No suspicious activities detected![/bold green]",
                    title="Security Status",
                    border_style="green"
                )
            )

        # ==================================
        # Final Statistics
        # ==================================

        summary = Table(
            title="ANALYSIS SUMMARY",
            box=box.DOUBLE_EDGE,
            border_style="bright_blue",
            header_style="bold cyan"
        )

        summary.add_column("Metric", style="white")
        summary.add_column("Value", justify="center", style="bold green")

        summary.add_row("Total Lines Scanned", str(total_lines))
        summary.add_row("Total Attacks Detected", str(total_attacks))
        summary.add_row("Unique Attack Types", str(len(attack_counter)))

        console.print("\n")
        console.print(summary)

        # Attack Statistics
        if attack_counter:

            stats = Table(
                title="ATTACK DISTRIBUTION",
                box=box.ROUNDED,
                border_style="yellow"
            )

            stats.add_column("Attack Type", style="cyan")
            stats.add_column("Count", justify="center", style="bold red")

            for attack, count in attack_counter.most_common():

                stats.add_row(
                    attack,
                    str(count)
                )

            console.print("\n")
            console.print(stats)

        console.print(
            Panel(
                "[bold green]Log Analysis Completed Successfully[/bold green]",
                border_style="green"
            )
        )

    except FileNotFoundError:

        console.print(
            Panel(
                f"[bold red]Log file not found: {filename}[/bold red]",
                title="File Error",
                border_style="red"
            )
        )

    except PermissionError:

        console.print(
            "[bold red][!] Permission denied while reading log file.[/bold red]"
        )

    except OSError as error:

        console.print(
            f"[bold red][!] File error: {error}[/bold red]"
        )


# ==========================================
# Main
# ==========================================

def main():

    console.clear()

    display_header()

    console.print(
        "[bold yellow]Starting Security Log Analysis...[/bold yellow]\n"
    )

    analyze_logs(LOG_FILE)


if __name__ == "__main__":
    main()
