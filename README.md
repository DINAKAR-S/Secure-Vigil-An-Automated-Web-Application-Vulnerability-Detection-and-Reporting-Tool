# Secure Vigil
Secure Vigil is a Python application that analyzes code files for vulnerabilities. It helps identify potential security issues such as code injection, SQL injection, LFI (Local File Inclusion) and RFI (Remote File Inclusion).

## Features
- Supports various programming languages including Python, Java, JavaScript, C, C++, Ruby, HTML, and PHP.
- Analyzes code files for vulnerabilities.
- Displays vulnerability details including type, pattern, and line number.
- Provides a user-friendly graphical interface for file selection and displaying results.

## Installation
To use Secure Vigil, follow the steps below:
```
Install the required dependencies:

```
pip install re
pip install tkinter
pip install Pillow
pip install ttkthemes
pip install atheris
```
## Usage
To run Secure Vigil, execute the following command:
```
python detector.py
```
The Secure Vigil window will appear, allowing you to perform the following actions:
- Click the "Attach File" (Attach File) button to select a code file for analysis.
- Once the file is selected, Secure Vigil will analyze it for vulnerabilities.
- If vulnerabilities are found, they will be displayed in the application window, showing the type, pattern, and line number of each vulnerability.
- If no vulnerabilities are found, a message indicating this will be displayed.

Please note that Secure Vigil supports the following file extensions: `.py`, `.java`, `.js`, `.c`, `.cpp`, `.html`, and `.php`.

## Vulnerability Detection
Secure Vigil detects the following types of vulnerabilities:
- Code Injection: It searches for patterns such as eval(, exec(, os.system(, subprocess.run(, $(, and `.*` in the code.
- SQL Injection: It identifies patterns such as SELECT *, DROP TABLE, and DELETE FROM in the code (case-insensitive).
- LFI (Local File Inclusion) and RFI (Remote File Inclusion).


