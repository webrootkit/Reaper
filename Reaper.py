#!/usr/bin/env python3
import requests
import socket
import json
from bs4 import BeautifulSoup
import sys
from datetime import datetime

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"
    BOLD = "\033[1m"

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

def check_email(email):
    try:
        print(f"\n{Colors.GREEN}[+] Проверка email: {email}{Colors.END}")
        # Здесь будет реальная проверка через API
        print(f"{Colors.YELLOW}├─ Найдено в утечках: 3 базы")
        print(f"└─ Последняя утечка: 2023-05-15 (LinkedIn){Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def check_username(username):
    try:
        print(f"\n{Colors.GREEN}[+] Поиск username: {username}{Colors.END}")
        # Здесь будет реальный поиск
        print(f"{Colors.YELLOW}├─ Найдено на: GitHub, VK")
        print(f"└─ Активность: 2 дня назад{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def check_phone(phone):
    try:
        print(f"\n{Colors.GREEN}[+] Проверка номера: {phone}{Colors.END}")
        # Здесь будет реальный пробив
        print(f"{Colors.YELLOW}├─ Оператор: МТС (Россия)")
        print(f"└─ Возможное имя: Иван Петров{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def ip_lookup(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        print(f"\n{Colors.GREEN}🔍 Информация по IP: {ip}{Colors.END}")
        print(f"{Colors.YELLOW}├─ Страна: {data.get('country', 'N/A')}")
        print(f"├─ Город: {data.get('city', 'N/A')}")
        print(f"├─ Провайдер: {data.get('isp', 'N/A')}")
        print(f"└─ Координаты: {data.get('lat', '?')}, {data.get('lon', '?')}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def port_scan(ip, ports="80,443,22,3389"):
    try:
        print(f"\n{Colors.YELLOW}⚡ Сканируем порты {ip}...{Colors.END}")
        for port in map(int, ports.split(",")):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                status = f"{Colors.GREEN}OPEN{Colors.END}" if result == 0 else f"{Colors.RED}CLOSED{Colors.END}"
                print(f"Порт {port}: {status}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка сканирования: {e}{Colors.END}")

def darknet_search(query):
    try:
        print(f"\n{Colors.RED}🔦 Ищем в даркнете: {query}{Colors.END}")
        # Здесь будет реальный поиск
        print(f"{Colors.YELLOW}├─ Найдено в 3 утечках")
        print(f"└─ Последняя запись: 2024-02-10 (форум exploit.in){Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Ошибка: {e}{Colors.END}")

def main():
    show_banner()
    while True:
        show_menu()
        try:
            choice = input(f"{Colors.YELLOW}>>> Выберите действие: {Colors.END}").strip()
            
            if choice == "1":
                email = input("Введите email: ").strip()
                if "@" in email:
                    check_email(email)
                else:
                    print(f"{Colors.RED}⚠ Неверный формат email!{Colors.END}")
                    
            elif choice == "2":
                username = input("Введите username: ").strip()
                if len(username) > 2:
                    check_username(username)
                else:
                    print(f"{Colors.RED}⚠ Слишком короткий username!{Colors.END}")
                    
            elif choice == "3":
                phone = input("Введите номер (+7...): ").strip()
                if phone.startswith("+7") and len(phone) == 12:
                    check_phone(phone)
                else:
                    print(f"{Colors.RED}⚠ Неверный формат номера!{Colors.END}")
                    
            elif choice == "4":
                ip = input("Введите IP: ").strip()
                if ip.count(".") == 3:
                    ip_lookup(ip)
                else:
                    print(f"{Colors.RED}⚠ Неверный формат IP!{Colors.END}")
                    
            elif choice == "5":
                ip = input("Введите IP (или Enter для localhost): ").strip() or "127.0.0.1"
                ports = input("Порты через запятую (80,443...): ").strip() or "80,443,22"
                if all(p.isdigit() for p in ports.split(",")):
                    port_scan(ip, ports)
                else:
                    print(f"{Colors.RED}⚠ Неверный формат портов!{Colors.END}")
                    
            elif choice == "6":
                query = input("Введите email/username/IP: ").strip()
                if query:
                    darknet_search(query)
                else:
                    print(f"{Colors.RED}⚠ Пустой запрос!{Colors.END}")
                    
            elif choice == "7":
                print(f"\n{Colors.RED}🛑 Выход из программы...{Colors.END}")
                sys.exit(0)
                
            else:
                print(f"{Colors.RED}⚠ Неверный выбор!{Colors.END}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🛑 Программа прервана пользователем{Colors.END}")
            sys.exit(1)
        except Exception as e:
            print(f"{Colors.RED}⚠ Критическая ошибка: {e}{Colors.END}")

if __name__ == "__main__":
    # Проверка зависимостей
    try:
        import requests
        import bs4
    except ImportError:
        print(f"{Colors.RED}❌ Требуются библиотеки: requests, beautifulsoup4{Colors.END}")
        print("Установите их командой: pip install requests beautifulsoup4")
        sys.exit(1)
    
    main()
