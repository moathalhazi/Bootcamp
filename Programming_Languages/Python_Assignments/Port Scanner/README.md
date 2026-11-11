# 🔍 Multithreaded Port Scanner

A Python-based TCP Port Scanner that uses **Multithreading** to scan network ports efficiently and identify active services on a target IPv4 address.

The tool provides a professional terminal interface using the **Rich** library, displaying scan progress, discovered open ports, service names, and detailed scanning statistics.

## 🚀 Features

- **Multithreading:** Uses `ThreadPoolExecutor` with up to 50 concurrent workers.
- **TCP Port Scanning:** Checks TCP ports using Python's `socket` library.
- **Timeout Handling:** Prevents excessive waiting when connecting to unresponsive ports.
- **Real-Time Progress:** Displays a progress bar during scanning.
- **Professional Interface:** Uses Rich for colored output, tables, and panels.
- **Port Identification:** Displays common service names associated with open ports.
- **Scan Statistics:** Reports open, closed, and filtered/no-response ports.
- **CSV Export:** Saves scan results to a CSV file.
- **IP Validation:** Validates the target IP address before scanning.

## 🛠️ Technologies Used


| Technology | Purpose |
|---|---|
| Python 3 | Programming Language |
| Socket | TCP Network Connections |
| Concurrent Futures | Concurrent Task Execution |
| ThreadPoolExecutor | Thread Management |
| Rich | Professional Terminal Interface |
| CSV | Exporting Scan Results |
| IPAddress | IP Address Validation |
| Time | Measuring Execution Time |

## 📁 Project Structure

```text
port_scanner/
│
├── port_scanner.py
├── README.md
└── scan_172_100_100_116.csv
```
## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/moathalhazi/Bootcamp/Programming_Languages/Python_Assignments/port_scanner
```
2. Navigate to the project directory
```bash
cd port_scanner
```
3. Install dependencies
```bash
pip install rich
```

▶️ Usage

Run the scanner:

```text
python port_scanner.py
```

Enter the target IPv4 address when prompted:
```text
╔══════════════════════════════════════════════════════════════════════╗
║  MULTITHREADED PORT SCANNER                                          ║
║  Network Security & Reconnaissance Tool                              ║ 
║  TCP Port Scanning                                                   ║
╚══════════════════════════════════════════════════════════════════════╝

Enter Target IP: 172.100.100.116
```

The scanner will automatically scan ports from 1 to 1024 using 50 concurrent workers.

📊 Sample Output

```text
       SCAN CONFIGURATION
╭─────────────┬─────────────────╮
│ Setting     │ Value           │
├─────────────┼─────────────────┤
│ Target IP   │ 172.100.100.116 │
│ Port Range  │ 1-1024          │
│ Total Ports │ 1024            │
│ Max Threads │ 50              │
│ Timeout     │ 1 second(s)     │
│ Protocol    │ TCP             │
╰─────────────┴─────────────────╯

[+] Starting port scan...

 Scanning ports... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% (1024/1024) 0:00:21

  OPEN PORTS DISCOVERED
╭──────┬─────────┬────────╮
│ PORT │ SERVICE │ STATUS │
├──────┼─────────┼────────┤
│ 135  │ Unknown │  OPEN  │
│ 139  │ Unknown │  OPEN  │
│ 445  │ SMB     │  OPEN  │
│ 903  │ Unknown │  OPEN  │
│ 913  │ Unknown │  OPEN  │
╰──────┴─────────┴────────╯

              SCAN SUMMARY
╔════════════════════════╤═══════════════╗
║ Metric                 │    Result     ║
╟────────────────────────┼───────────────╢
║ Total Scanned          │     1024      ║
║ Open Ports             │       5       ║
║ Closed Ports           │       0       ║
║ Filtered / No Response │     1019      ║
║ Threads Used           │      50       ║
║ Time Elapsed           │ 21.22 seconds ║
╚════════════════════════╧═══════════════╝

╭───────────────────────────────────────────────────────────────────────────────╮
│ SCAN COMPLETED SUCCESSFULLY                                                   │
│                                                                               │
│ Results saved to: scan_172_100_100_116.csv                                    │
╰───────────────────────────────────────────────────────────────────────────────╯
```

*Note: Actual results and execution time depend on the target system and network conditions.*

## 🧠 How It Works

1. **Target Validation:** Validates the entered IPv4 address.
2. **Socket Creation:** Creates a TCP socket for each port.
3. **Timeout Configuration:** Sets a connection timeout.
4. **Port Scanning:** Uses `connect_ex()` to check whether a TCP connection succeeds.
5. **Multithreading:** Distributes scanning tasks across multiple worker threads.
6. **Result Collection:** Collects and classifies connection results.
7. **Statistics:** Calculates scan duration and summarizes the results.
8. **CSV Export:** Saves scan results for later analysis.

## 🔐 Port Status Explanation

| Status | Description |
|---|---|
| OPEN | TCP connection successfully established. |
| CLOSED | Connection was actively refused by the target. |
| FILTERED / NO RESPONSE | Connection failed or timed out; filtering may be involved. |

## ⚠️ Disclaimer

This tool is developed for educational purposes and authorized network security testing only.

- Scan only systems you own or have explicit permission to test.
- Unauthorized port scanning may violate applicable laws or organizational policies.
- This tool performs TCP scanning only; UDP scanning is not supported.
- A failed connection does not always mean that a port is closed.
- Filtered/no-response results do not conclusively identify the presence of a firewall.

## 👨‍💻 Author

**Eng. Moath Al-Hazi**
