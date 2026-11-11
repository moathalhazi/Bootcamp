# Password Strength Checker (C)

## Overview
This project is a simple Password Strength Checker written in the C programming language. It evaluates a password based on basic criteria and determines whether it is strong.

## Features
- Accepts a password from the user.
- Checks password strength based on the implemented criteria.
- Displays the result as either strong or weak.
- Demonstrates basic C programming concepts, including functions, conditional statements, and string handling.

## Technologies Used
- **Language:** C
- **Compiler:** GCC
- **Development Environment:** Visual Studio Code
- **Toolchain:** MSYS2 UCRT64

## Project Structure
```text
c_assignment/
├── password_strength_checker.c
├── password_checker.exe
└── README.md
```

## How to Compile

Make sure GCC is installed and available in your terminal.

```bash
gcc password_strength_checker.c -o password_checker.exe
```

## How to Run

On Windows using the MSYS2 UCRT64 terminal:

```bash
password_checker.exe
```

## Example Output

```text
========== Password Strength Checker ==========
-> Enter your password: **********

========================================
[-] Password Length [21] Chars
[-] Password Contains [1] Upper Letters
[-] Password Contains [9] Lower Letters
[-] Password Contains [9] Numbers
[-] Password Contains [2] Symbols
[-] Your Password [**********] is Strong
[-] USE IT
========================================
```

*The output depends on the password entered and the criteria implemented in the source code.*

## Learning Objectives
- Practice writing and compiling C programs.
- Understand functions and conditional logic.
- Learn basic string handling in C.
- Use GCC to compile and run a C application.

## Author
**Eng. Moaz Al-Hazi**

---

*Developed as part of a programming training assignment.*
