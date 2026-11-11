# 🔍 Banner Grabbing Tool

A Python-based TCP Banner Grabbing Tool designed for active network reconnaissance and service fingerprinting.

The tool connects to specified TCP ports, captures service banners, analyzes received responses, and identifies service information such as service names and software versions when disclosed by the target server.

It provides a professional terminal interface using the Rich library, displaying scan information, discovered services, port statuses, and scan statistics.

## 🚀 Features

- **TCP Connection:** Establishes TCP connections to specified target ports.

- **Banner Grabbing:** Captures service banners from responsive servers.

- **Service Identification:** Identifies common services such as FTP, SSH, SMTP, HTTP, and HTTPS based on port numbers.

- **Version Detection:** Extracts software and service version information from received banners.

- **HTTP Request Handling:** Sends HTTP HEAD requests to web servers that do not automatically disclose banners.

- **Banner Cleaning:** Decodes received data and removes unnecessary whitespace and empty lines.

- **Timeout Handling:** Handles connection timeouts and refused connections.

- **IPv4 Validation:** Validates the target IPv4 address before scanning.

- **Professional CLI:** Displays structured scan results using the Rich library.

- **Scan Statistics:** Reports scan duration, open ports, and identified services.

## 🛠️ Technologies Used

| Technology  | Purpose |
|---|---|
| Python 3  | Core programming language |
| Socket | TCP network communication |
| Rich | Terminal interface and result visualization |
| IPAddress | IPv4 address validation |
| Datetime | Scan timestamp |
| Time | Scan duration measurement |


## 📋 Requirements

- Python 3.8 or later

- Rich library

- Network connectivity to the authorized target

▶️ Usage

Run the grabber:

```text
python banner_grabber.py
```


📊 Sample Output

```text
╭──────────────────────────────────────────────────────────────────────────╮
│ BANNER GRABBING TOOL                                                     │
│ TCP Service Fingerprinting & Reconnaissance                              │
╰──────────────────────────────────────────────────────────────────────────╯
Enter Target IPv4: 172.100.100.116

Starting scan on 172.100.100.116...

Scanning port 21...
Scanning port 22...
Scanning port 25...
Scanning port 80...
Scanning port 139...
Scanning port 445...
Scanning port 443...
Scanning port 8080...

Scan Completed!

╭──────────────────────────────────────── SCAN INFORMATION ────────────────────────────────────╮
│ Target: 172.100.100.116                                                                      |
│ Scan Type: TCP Banner Grabbing                                                               |
│ Scan Date: 2026-11-12 02:19:20.401479                                                        |
│ Duration: 22.20 seconds                                                                      |
│ Open Ports: 2/8                                                                              |
│ Identified Services: 0                                                                       |
╰──────────────────────────────────────────────────────────────────────────────────────────────╯ 
     Discovered Services  
╭──────┬─────────────┬───────────────┬───────────╮
│ PORT │   SERVICE   │ VERSION       │  STATUS   │
├──────┼─────────────┼───────────────┼───────────┤
│  21  │   Unknown   │ N/A           │  Closed   │
├──────┼─────────────┼───────────────┼───────────┤
│  22  │   Unknown   │ N/A           │  Closed   │
├──────┼─────────────┼───────────────┼───────────┤
│  25  │   Unknown   │ N/A           │  Closed   │
├──────┼─────────────┼───────────────┼───────────┤
│  80  │   Unknown   │ N/A           │  Closed   │
├──────┼─────────────┼───────────────┼───────────┤
│ 139  │ NetBIOS-SSN │ Not Disclosed │ No Banner │
├──────┼─────────────┼───────────────┼───────────┤
│ 445  │     SMB     │ Not Disclosed │ No Banner │
├──────┼─────────────┼───────────────┼───────────┤
│ 443  │   Unknown   │ N/A           │  Closed   │
├──────┼─────────────┼───────────────┼───────────┤
│ 8080 │   Unknown   │ N/A           │  Closed   │
╰──────┴─────────────┴───────────────┴───────────╯
```

## 👨‍💻 Author

**Eng. Moath Al-Hazi**