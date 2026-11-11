🔍 Multithreaded Port Scanner

A Python-based TCP Port Scanner that uses Multithreading to scan network ports efficiently and identify active services on a target IPv4 address.

The tool provides a professional terminal interface using the Rich library, displaying scan progress, open ports, service names, and detailed statistics.

🚀 Features

Multithreading: Uses ThreadPoolExecutor with up to 50 concurrent workers.

TCP Port Scanning: Checks TCP ports using Python's socket library.

Timeout Handling: Prevents long waiting times when connecting to unresponsive ports.

Real-Time Progress: Displays a progress bar during scanning.

Professional Interface: Uses Rich for colored output, tables, and panels.

Port Identification: Displays common service names associated with open ports.

Scan Statistics: Reports open, closed, and filtered/no-response ports.

CSV Export: Saves scan results to a CSV file.

IP Validation: Validates the target IP address before scanning.

🛠️ Technologies Used

Technology

Purpose

Python 3

Programming Language

Socket

TCP Network Connections

Concurrent Futures

Multithreading

ThreadPoolExecutor

Thread Management

Rich

Professional Terminal Interface

CSV

Exporting Scan Results

IPAddress

IP Address Validation

Time

Measuring Execution Time

📁 Project Structure

Multithreaded-Port-Scanner/
│
├── port_scanner.py
├── requirements.txt
├── README.md
└── scan_127_0_0_1.csv

⚙️ Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/Multithreaded-Port-Scanner.git

2. Navigate to the project directory

cd Multithreaded-Port-Scanner

3. Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the scanner:

python port_scanner.py

Enter the target IPv4 address when prompted:

Enter Target IP: 127.0.0.1

The scanner will automatically scan ports from 1 to 1024 using 50 concurrent workers.

📊 Sample Output

╔══════════════════════════════════════════╗
║       MULTITHREADED PORT SCANNER         ║
║     Network Security & Reconnaissance    ║
╚══════════════════════════════════════════╝

SCAN CONFIGURATION

Target IP       127.0.0.1
Port Range      1-1024
Total Ports     1024
Max Threads     50
Timeout         1 second
Protocol        TCP

[+] Starting port scan...

Scanning ports... ━━━━━━━━━━━━━━━━━━ 100%

OPEN PORTS DISCOVERED

┌──────┬──────────┬────────┐
│ PORT │ SERVICE  │ STATUS │
├──────┼──────────┼────────┤
│  80  │ HTTP     │ OPEN   │
│ 443  │ HTTPS    │ OPEN   │
└──────┴──────────┴────────┘

SCAN SUMMARY

Total Scanned          1024
Open Ports                2
Closed Ports           1020
Filtered / No Response    2
Threads Used             50
Time Elapsed          2.45 seconds

SCAN COMPLETED SUCCESSFULLY
Results saved to: scan_127_0_0_1.csv

Note: Sample output is illustrative. Actual results and execution time depend on the target and network conditions.

🧠 How It Works

Target Validation: Validates the entered IPv4 address.

Socket Creation: Creates a TCP socket for each port.

Timeout Configuration: Sets a connection timeout.

Port Scanning: Uses connect_ex() to check whether a TCP connection succeeds.

Multithreading: Distributes scanning tasks across multiple worker threads.

Result Collection: Collects and classifies connection results.

Statistics: Calculates scan duration and summarizes the results.

CSV Export: Saves the collected results for later analysis.

🔐 Port Status Explanation

Status

Description

OPEN

TCP connection successfully established.

CLOSED

Connection was refused by the target.

FILTERED / NO RESPONSE

Connection failed or timed out; filtering may be involved.

🧪 Local Testing

You can test the scanner on your own machine.

Start a local HTTP server:

python -m http.server 8000 --bind 127.0.0.1

Temporarily change the scanning range in port_scanner.py:

START_PORT = 8000
END_PORT = 8000

Run the scanner and enter:

127.0.0.1

Expected result:

PORT    SERVICE    STATUS
8000    Unknown    OPEN

⚙️ Configuration

You can customize the scanning settings in the source code:

START_PORT = 1
END_PORT = 1024
MAX_WORKERS = 50
TIMEOUT = 1

⚠️ Disclaimer

This tool is developed for educational purposes and authorized network security testing only.

Scan only systems you own or have explicit permission to test.

Unauthorized port scanning may violate applicable laws or organizational policies.

This tool performs TCP scanning only; UDP ports are not supported.

A failed connection does not always mean that a port is closed.

👨‍💻 Author

Moath Al-Hazi

Cybersecurity Student | Network Security Enthusiast

GitHub: Moath Al-Hazi

Developed as the Fifth Programming Assignment – Multithreaded Port Scanner.
