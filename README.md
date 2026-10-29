# fok-leak
Local, free, action-oriented leak checker. No cloud, no signup, no telemetry. Проверь, не слили ли твои данные.
# FOK LEAK 🔍

> Check if your data has been leaked — right now, locally, for free, and in Russian.

With a single command, you can find out which services have leaked your data, whether your password appears in any databases, and what steps you should take first.

[Author's channel](https://t.me/avatatkok/386)

---

## 🚀 Quick Start

### 1. Install Python

If you haven't already, download it from [python.org](https://python.org).  
**On Windows, make sure to check the "Add Python to PATH" box during installation.**

Verify that Python is installed:
```bash
python --version
```

### 2. Install dependencies

```bash
pip install rich httpx
```

### 3. Download the file

Create a file named **`leak.py`** and paste the code from the repository into it.  
Alternatively, download it directly:
```bash
git clone https://github.com/you/fok-leak.git
cd fok-leak
```

### 4. Run it

```bash
python leak.py
```

A menu will appear — select an option by entering the corresponding number and pressing Enter.

---

## 📋 All Commands

### Check an email address
```bash
python leak.py check you@example.com
```

What it checks:
- HIBP — data breaches associated with the email
- GitHub — whether the email appears in public commits
- DuckDuckGo — mentions across the open web

### Check a phone number
```bash
python leak.py check +79001234567
```

### Check a password (anonymously)
```bash
python leak.py password "your_password"
```

Your password is **never sent** — only the first 5 characters of its SHA-1 hash are used.  If found in any data leaks, it will show how many times.

### Add to watchlist
```bash
python leak.py watch add you@example.com
python leak.py watch add +79001234567
```

### Run watchlist check
```bash
python leak.py watch
```

This will check all added email addresses/phone numbers.  
If a new leak is detected, it will be highlighted in red.

### Main menu (no arguments)
```bash
python leak.py
```

---

## 🖥 Installation on various systems

### Windows

1. Download Python from [python.org](https://python.org); during installation, make sure to select **"Add Python to PATH"**.
2. Open the **Command Prompt** (Win+R → `cmd` → Enter).
3. Run:
```bash
pip install rich httpx
python leak.py
```

If `python` is not found, try `py leak.py` or `python3 leak.py`.

### Linux (Ubuntu / Debian / Mint)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install rich httpx
python3 leak.py
```

### macOS

```bash
brew install python
pip3 install rich httpx
python3 leak.py
```

### Termux (Android)

```bash
pkg update
pkg install python
pip install rich httpx
python leak.py
```
