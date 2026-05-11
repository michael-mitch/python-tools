![Release](https://img.shields.io/github/v/release/YOUR_USERNAME/python-tools?label=hash-checker)

# Hash Checker

Hash Checker is a lightweight, dependency‑free Python command‑line tool for computing cryptographic hashes and verifying file integrity. It supports a wide range of hashing algorithms, including SHA‑2, SHA‑3, and SHAKE, and provides a clean, menu‑driven interface suitable for both beginners and experienced users.

This tool is part of the **Python Tools Suite**, a collection of small, focused utilities designed for learning, productivity, and portfolio development.

---

## Features

- Menu‑driven command‑line interface  
- Compute hashes for any file  
- Supports multiple algorithms:
  - MD5  
  - SHA‑1  
  - SHA‑224  
  - SHA‑256  
  - SHA‑384  
  - SHA‑512  
  - SHA‑3 (256)  
  - SHAKE‑128 (variable length)  
  - SHAKE‑256 (variable length)
- Optional known‑hash comparison  
- Error handling for:
  - Missing files  
  - Invalid input  
  - Unsupported algorithms
- No external dependencies  
- Works on Windows, macOS, and Linux  

---

## Usage

Run the tool from the command line:

```bash
python3 hash_checker.py
```

You will see:

```
===========================
     HASH CHECKER TOOL
===========================

1) Hash a File
2) Exit
```

Select an algorithm, choose a file, and optionally enter a known hash to compare.

---

## File Structure

```
hash-checker/
│
├── hash_checker.py
└── README.md
```

---

## Roadmap

Planned improvements for future versions:

- Folder hashing (hash all files in a directory)  
- File‑to‑file comparison  
- Save results to a text or log file  
- Recursive hashing option  
- Settings menu for default algorithm, output format, etc.  

---

## Versioning

This project follows **Semantic Versioning (SemVer)**:

- **MAJOR** — Breaking changes  
- **MINOR** — New features  
- **PATCH** — Bug fixes  

Current version: **v1.0.0**

---

## License

MIT License — see the LICENSE file in the root of the repository.
