# Hexadecimal Viewer (Hex Viewer)

A command-line tool developed in **C Programming** to read and inspect binary files by displaying their contents in both **Hexadecimal (HEX)** and **ASCII** formats.

## 📌 Project Description

The Hexadecimal Viewer is a simple tool designed to help cybersecurity students and analysts inspect raw binary data, examine file headers, and identify file signatures (Magic Numbers).

The program reads binary files in chunks of 16 bytes and displays each byte in hexadecimal format alongside its corresponding printable ASCII character.

## ✨ Features

- Read binary files using `fopen()` in `rb` mode.
- Process file data in 16-byte chunks using `fread()`.
- Display byte values in hexadecimal format (`%02X`).
- Display printable ASCII characters.
- Replace non-printable characters with dots (`.`).
- Display file offsets for each row.
- Handle missing files and file reading errors.
- Automatically close files using `fclose()`.

## 🛠️ Technologies Used

- **Programming Language:** C
- **Compiler:** GCC
- **Development Environment:** MSYS2 UCRT64
- **Standard:** C11

## 📂 Project Structure

```text
Hexadecimal-Viewer/
│
├── Effective_commonications.png
├── Framework_vs_Library_Arabic_Infographic.png
├── hex_viewer.c
├── hex_viewer.exe
├── simplewall-3.8.7-setup.exe
├── test.txt
└── README.md
```

## ⚙️ Compilation

Compile the source code using GCC:

```bash
gcc hex_viewer.c -o hex_viewer.exe
```

## ▶️ Usage

Run the program and provide the target file as a command-line argument:

```bash
./hex_viewer.exe <filename>
```

### Examples

Read a text file:

```bash
./hex_viewer.exe test.txt
```

Read an image file:

```bash
./hex_viewer.exe Effective_commonications.png
```

Read an executable file:

```bash
./hex_viewer.exe simplewall-3.8.7-setup.exe
```

## 📊 Sample Output

```text
Offset      Hexadecimal Bytes                                ASCII
------------------------------------------------------------------------------
00000000    48 65 78 61 64 65 63 69 6D 61 6C 20 56 69 65 77  Hexadecimal View
00000010    65 72 20 41 20 63 6F 6D 6D 61 6E 64 2D 6C 69 6E  er A command-lin
00000020    65 20 74 6F 6F 6C 20 64 65 76 65 6C 6F 70 65 64  e tool developed
00000030    20 75 73 69 6E 67 20 43 20 74 6F 20 72 65 61 64   using C to read
00000040    20 62 69 6E 61 72 79 20 66 69 6C 65 73 20 61 6E   binary files an
00000050    64 20 64 69 73 70 6C 61 79 20 74 68 65 69 72 20  d display their 
00000060    63 6F 6E 74 65 6E 74 73 20 69 6E 20 48 65 78 61  contents in Hexa
00000070    64 65 63 69 6D 61 6C 20 61 6E 64 20 41 53 43 49  decimal and ASCI
00000080    49 20 66 6F 72 6D 61 74 73 2E 20 54 68 65 20 70  I formats. The p
00000090    72 6F 67 72 61 6D 20 72 65 61 64 73 20 64 61 74  rogram reads dat
000000A0    61 20 69 6E 20 67 72 6F 75 70 73 20 6F 66 20 31  a in groups of 1
000000B0    36 20 62 79 74 65 73 2C 20 68 65 6C 70 69 6E 67  6 bytes, helping
000000C0    20 75 73 65 72 2E                                 user.

------------------------------------------------------------------------------
-> File reading completed [successfully].
```

## 🎯 Learning Objectives

This assignment demonstrates practical understanding of:

- File handling in C.
- Binary file reading.
- Command-line arguments (`argc` and `argv`).
- Arrays and loops.
- ASCII character representation.
- Hexadecimal number formatting.
- Error handling and resource management.

## 🔐 Cybersecurity Applications

Hexadecimal viewers are useful in cybersecurity and digital forensics for:

- Inspecting file headers.
- Identifying file signatures (Magic Numbers).
- Examining raw binary data.
- Investigating suspicious files.
- Understanding file structures.

## 👨‍💻 Author

**Eng. Moath Al-Hazi**

---

*Developed as part of a programming training assignment.*
