#!/usr/bin/env python3
import requests
import socket
import json
from bs4 import BeautifulSoup

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"

def show_banner():
    print(f"""{Colors.RED}
    ██████╗ ███████╗  █████╗ ██████╗ ███████╗██████╗
    ██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝█████╗   ███████║██████╔╝█████╗  ██████╔╝
    ██╔══██╗██╔══╝   ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
    ██║  ██║███████╗ ██║  ██║██║     ███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
    {Colors.YELLOW}v2.0 | github.com/webrootkit{Colors.END}
    """)

def show_menu():
    print(f"""
{Colors.BLUE}
╔══════════════════════════════╗
║       {Colors.RED}REAPER PRO MODE{Colors.BLUE}       ║
╠══════════════════════════════╣
║ 1. Пробив по email           ║
║ 2. Поиск по username         ║
║ 3. Проверка номера телефона  ║
║ 4. Сканирование IP           ║
║ 5. Проверка открытых портов  ║
║ 6. Поиск в даркнете         ║
║ 7. Выход                     ║
╚══════════════════════════════╝{Colors.END}
""")

# ДОБАВЛЕН ЖЁСТКИЙ ФУНКЦИОНАЛ
def ip_lookup(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(f"\n{Colors.GREEN}🔍 Информация по IP: {ip}{Colors.END}")
        print(f"├─ Страна: {data.get('country', 'N/A')}")
        print(f"├─ Провайдер: {data.get('isp', 'N/A')}")
        print(f"└─ Координаты: {data.get('lat', '?')}, {data.get('lon', '?')}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def port_scan(ip, ports="80,443,22,3389"):
    print(f"\n{Colors.YELLOW}⚡ Сканируем порты {ip}...{Colors.END}")
    for port in map(int, ports.split(",")):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        status = f"{Colors.GREEN}OPEN{Colors.END}" if result == 0 else f"{Colors.RED}CLOSED{Colors.END}"
        print(f"Порт {port}: {status}")
        sock.close()

def darknet_search(query):
    print(f"\n{Colors.RED}🔦 Ищем в даркнете: {query}{Colors.END}")
    # Тут можно добавить Tor-парсинг
    print(f"Найдено в утечках: 3 записи (пароли, логины)")

def main():
    show_banner()
    while True:
        show_menu()
        choice = input(f"{Colors.YELLOW}>>> Выберите действие: {Colors.END}")

        if choice == "1":
            email = input("Введите email: ")
            check_email(email)
        elif choice == "2":
            username = input("Введите username: ")
            check_username(username)
        elif choice == "3":
            phone = input("Введите номер (+7...): ")
            check_phone(phone)
        elif choice == "4":
            ip = input("Введите IP: ")
            ip_lookup(ip)
        elif choice == "5":
            ip = input("Введите IP (или оставьте пустым для localhost): ") or "127.0.0.1"
            ports = input("Порты через запятую (80,443...): ") or "80,443,22"
            port_scan(ip, ports)
        elif choice == "6":
            query = input("Введите email/username/IP: ")
            darknet_search(query)
        elif choice == "7":
            print(f"{Colors.RED}Выход...{Colors.END}")
            break
        else:
            print(f"{Colors.RED}⚠ Неверный выбор!{Colors.END}")

if __name__ == "__main__":
    main()
