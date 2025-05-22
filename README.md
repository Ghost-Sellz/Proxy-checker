# Proxy Checker | 10 STARS FOR V2
yes i made chatgpt write this cuz i was too lazy...
## Overview
🔱 **Proxy Checker** is a Python-based utility for validating proxies. It supports multiple proxy types (HTTP, HTTPS, SOCKS4, SOCKS5) and saves valid proxies into corresponding files. A potential scraper may be added in a future version.

## Features
- Checks proxies for validity.
- Supports multiple proxy types:
  - HTTP
  - HTTPS
  - SOCKS4
  - SOCKS5
- Saves valid proxies into respective files (`http.txt`, `https.txt`, `socks4.txt`, `socks5.txt`).
- Easy-to-use graphical file selection for proxy lists using a Tkinter file explorer.

## Requirements
To use this tool, make sure the following dependencies are installed:

```
requests
colorama
tkinter
```

Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

## How to Use
1. Download the program
   ```bash
   git clone https://github.com/Ghost-Sellz/Proxy-checker
   ```
2. Run the script by executing the following command:
   ```bash
   python main.py
   ```
3. Select option `1` from the menu to start the proxy checker.
4. Choose the type of proxy you want to check (HTTP, HTTPS, SOCKS4, or SOCKS5).
5. Use the file explorer to select your proxy file (must be a `.txt` file with proxies listed line by line).
6. The script will validate the proxies and save the valid ones into corresponding files.

## File Structure
- `http.txt`: Contains valid HTTP proxies.
- `https.txt`: Contains valid HTTPS proxies.
- `socks4.txt`: Contains valid SOCKS4 proxies.
- `socks5.txt`: Contains valid SOCKS5 proxies.

## Example Proxy Format
Your proxy file should list proxies in the following format:

```
127.0.0.1:8080
192.168.1.1:1080
```

## Future Enhancements
- **Proxy Scraper**: Automatically scrape proxies from online sources.
- **Multi-threading Enhancements**: Improved performance with advanced threading.

## License
This project is open-source and available under the MIT License.
