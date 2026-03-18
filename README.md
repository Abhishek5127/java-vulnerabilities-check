# java-vulnerabilities-check

A demonstration repository containing common Java and Python vulnerabilities for educational and analysis purposes.

## Project Overview

This repository serves as a demo for vulnerability analysis tools, containing intentionally vulnerable code samples across multiple categories. The codebase includes both Java and Python implementations to demonstrate various security issues that commonly occur in software development.

## Features

- **Code Execution Vulnerabilities**: Unsafe `eval()` and `exec()` usage in Python
- **Deserialization Issues**: Insecure pickle and YAML deserialization endpoints
- **Debug Configuration**: Flask app running with debug mode enabled
- **Path Traversal**: Directory traversal vulnerabilities in file operations
- **SQL Injection**: Multiple endpoints with SQL injection vulnerabilities
- **Template Injection**: Flask template injection vulnerabilities
- **Crypto Issues**: Cryptographic implementation problems
- **Temporary File Handling**: Insecure temporary file operations

## Tech Stack

- **Python**: Primary language for vulnerability demonstrations
- **Flask**: Web framework used for most vulnerability examples
- **Java**: Secondary language with vulnerability examples
- **SQLite**: Database used in SQL injection demonstrations

## Installation

bash
git clone https://github.com/abhishek5127/java-vulnerabilities-check.git
cd java-vulnerabilities-check


## Usage

Each vulnerability file can be run independently. For Flask-based examples:

bash
python3 codeexecutioon.py
python3 debug_config.py
python3 deseralization.py
python3 path_traversal.py
python3 sql.py


## Configuration

No special configuration is required. Each script runs independently and demonstrates specific vulnerabilities when executed.

## Project Structure


java-vulnerabilities-check/
├── archive.py                 # Archive-related vulnerabilities
├── codeexecutioon.py          # Code execution vulnerabilities
├── cryptoissues.py            # Cryptographic vulnerabilities
├── debug_config.py            # Debug configuration vulnerabilities
├── deseralization.py          # Deserialization vulnerabilities
├── path_traversal.py          # Path traversal vulnerabilities
├── sql.py                     # SQL injection vulnerabilities
├── tempfile.py                # Temporary file vulnerabilities
├── template_injection.py      # Template injection vulnerabilities
├── test_vulns.java            # Java vulnerability examples
└── test_vulns.py              # Python vulnerability examples


## Contributing

This repository is intended as a demonstration/educational resource for vulnerability analysis. Contributions should focus on adding new vulnerability types or improving existing examples while maintaining the educational purpose of the repository.

## Security Note

This repository contains intentionally vulnerable code for educational purposes. Do not use any of these examples in production environments.