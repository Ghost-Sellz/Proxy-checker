import random
import threading
import requests
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor
from tkinter import Tk, filedialog
import os

init(autoreset=True)

write_lock = threading.Lock()

def validate_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies=proxy, timeout=5)
        if response.status_code == 200:
            return True
    except Exception:
        return False

def save_proxy(proxy, proxy_type):
    filename = f"{proxy_type}.txt"
    with write_lock:
        with open(filename, "a") as file:
            file.write(proxy + "\n")

def check_proxy(proxy, proxy_type):
    proxy = proxy.strip()
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    if validate_proxy(proxy_dict):
        print(Fore.GREEN + f"{proxy_type.upper()} Proxy: {proxy} is valid.")
        save_proxy(proxy, proxy_type)
    else:
        print(Fore.RED + f"Invalid Proxy: {proxy}")

def process_proxies(proxy_type, proxy_file_path):
    print(Fore.MAGENTA + "🔱Proxy Checker\n-Checks proxies\n-saves into http,https,socks4,socks5.txt\n-maybe a scraper in v2")

    with open(proxy_file_path, "r") as file:
        proxies = file.readlines()

    with ThreadPoolExecutor(max_workers=10) as executor:
        for proxy in proxies:
            executor.submit(check_proxy, proxy, proxy_type)

def main():
    while True:
        print(Fore.CYAN + "Menu:")
        print("1. Start proxy checker")
        print("2. Exit")
        choice = input(Fore.CYAN + "Enter your choice: ").strip()

        if choice == "1":
            print(Fore.CYAN + "Select proxy type:")
            print("1. HTTP")
            print("2. HTTPS")
            print("3. SOCKS4")
            print("4. SOCKS5")
            proxy_choice = input(Fore.CYAN + "Enter your choice: ").strip()

            proxy_type = ""
            if proxy_choice == "1":
                proxy_type = "http"
            elif proxy_choice == "2":
                proxy_type = "https"
            elif proxy_choice == "3":
                proxy_type = "socks4"
            elif proxy_choice == "4":
                proxy_type = "socks5"
            else:
                print(Fore.RED + "Invalid proxy type choice. Returning to main menu.")
                continue

            print(Fore.CYAN + "Please select your proxy file:")
            proxy_file_path = filedialog.askopenfilename(title="Select Proxy File", filetypes=[("Text Files", "*.txt")])

            if not proxy_file_path:
                print(Fore.RED + "No file selected. Returning to main menu.")
                continue

            print(Fore.CYAN + f"Starting proxy checker for {proxy_type.upper()} proxies...")
            process_proxies(proxy_type, proxy_file_path)
            print(Fore.CYAN + "Proxy checking finished.")
        elif choice == "2":
            print(Fore.CYAN + "Exiting program. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()
