
import socket
import ipaddress
import time

from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box


# ================= CONFIGURATION =================

TIMEOUT = 5
BUFFER_SIZE = 1024

PORTS = [21, 22, 25, 80, 139, 445, 443, 8080]

console = Console()


# ================= BANNER CLEANING =================

def clean_banner(raw_data):

    text = raw_data.decode("utf-8", errors="ignore")

    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


# ================= SERVICE IDENTIFICATION =================

def extract_service_info(port, banner):

    
    services = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        80: "HTTP",
        139: "NetBIOS-SSN",
        445: "SMB",
        443: "HTTPS",
        8080: "HTTP-Proxy"
    }

    service = services.get(port, "Unknown")
    version = "Not Disclosed"

    for line in banner:

        lower_line = line.lower()

        if any(name in lower_line for name in [
            "openssh", "apache", "nginx",
            "vsftpd", "proftpd"
        ]):
            version = line
            break

        if lower_line.startswith("server:"):
            version = line.split(":", 1)[1].strip()
            break

        if port == 21 and line.startswith("220 "):
            version = line
            break

    return service, version


# ================= BANNER GRABBING =================

def grab_banner(target, port):

    try:

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(TIMEOUT)

            sock.connect((target, port))

            banner = b""

            try:
                banner = sock.recv(BUFFER_SIZE)

            except socket.timeout:
                pass

            # HTTP request for web services
            if not banner and port in [80, 8080]:

                request = (
                    f"HEAD / HTTP/1.1\r\n"
                    f"Host: {target}\r\n"
                    f"Connection: close\r\n\r\n"
                )

                sock.sendall(request.encode("utf-8"))

                try:
                    banner = sock.recv(BUFFER_SIZE)

                except socket.timeout:
                    pass

            # HTTPS requires TLS handshake
            elif not banner and port == 443:

                return {
                    "port": port,
                    "service": "HTTPS",
                    "version": "TLS handshake required",
                    "status": "No Banner"
                }

            lines = clean_banner(banner)

            if lines:

                service, version = extract_service_info(
                    port, lines
                )

                status = "Open"

            else:
                service = {
                    21: "FTP",
                    22: "SSH",
                    25: "SMTP",
                    80: "HTTP",
                    139: "NetBIOS-SSN",
                    445: "SMB",
                    443: "HTTPS",
                    8080: "HTTP-Proxy"
                }.get(port, "Unknown")

                version = "Not Disclosed"
                status = "No Banner"

            return {
                "port": port,
                "service": service,
                "version": version,
                "status": status
            }

    except ConnectionRefusedError:

        status = "Closed"

    except socket.timeout:

        status = "Timeout"

    except OSError:

        status = "Error"

    return {
        "port": port,
        "service": "Unknown",
        "version": "N/A",
        "status": status
    }


# ================= DISPLAY RESULTS =================

def display_results(target, results, duration):

    table = Table(
        title="Discovered Services",
        box=box.ROUNDED,
        show_lines=True
    )

    table.add_column("PORT", justify="center")
    table.add_column("SERVICE", justify="center")
    table.add_column("VERSION")
    table.add_column("STATUS", justify="center")

    for result in results:

        status = result["status"]

        if status == "Open":
            color = "green"

        elif status == "Closed":
            color = "red"

        elif status == "Timeout":
            color = "yellow"

        else:
            color = "cyan"

        table.add_row(
            str(result["port"]),
            result["service"],
            result["version"],
            f"[{color}]{status}[/{color}]"
        )

    open_ports = sum(
        1 for item in results
        if item["status"] in ["Open", "No Banner"]
    )

    identified = sum(
        1 for item in results
        if item["version"] != "Not Disclosed"
        and item["version"] != "N/A"
        and item["version"] != "TLS handshake required"
    )

    console.print(
        Panel(
            f"[bold cyan]Target:[/bold cyan] {target}\n"
            f"[bold cyan]Scan Type:[/bold cyan] TCP Banner Grabbing\n"
            f"[bold cyan]Scan Date:[/bold cyan] {datetime.now()}\n"
            f"[bold cyan]Duration:[/bold cyan] {duration:.2f} seconds\n"
            f"[bold cyan]Open Ports:[/bold cyan] {open_ports}/{len(results)}\n"
            f"[bold cyan]Identified Services:[/bold cyan] {identified}",
            title="[bold white]SCAN INFORMATION[/bold white]",
            border_style="cyan"
        )
    )

    console.print(table)


# ================= MAIN =================

def main():

    console.print(
        Panel(
            "[bold cyan]BANNER GRABBING TOOL[/bold cyan]\n"
            "[white]TCP Service Fingerprinting & Reconnaissance[/white]",
            border_style="cyan"
        )
    )

    target = console.input(
        "[bold green]Enter Target IPv4: [/bold green]"
    ).strip()

    try:
        ipaddress.IPv4Address(target)

    except ValueError:
        console.print("[bold red]Invalid IPv4 address![/bold red]")
        return

    console.print(
        f"\n[cyan]Starting scan on {target}...[/cyan]\n"
    )

    results = []

    start_time = time.perf_counter()

    for port in PORTS:

        console.print(
            f"[dim]Scanning port {port}...[/dim]"
        )

        result = grab_banner(target, port)

        results.append(result)

    duration = time.perf_counter() - start_time

    console.print("\n[bold green]Scan Completed![/bold green]\n")

    display_results(target, results, duration)


if __name__ == "__main__":
    main()
