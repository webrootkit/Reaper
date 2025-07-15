#!/usr/bin/env python3
import requests
import argparse
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime
import stem.process
from stem.util import term

class WebrootkitOSINT:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Webrootkit OSINT Tool)"}
        self.colors = {
            "red": term.Color.RED,
            "green": term.Color.GREEN,
            "yellow": term.Color.YELLOW,
            "reset": term.Color.RESET
        }
        self.report = []

    def print_banner(self):
        banner = f"""
        {self.colors['red']}
         ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ 
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
        ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
        ▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
         ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀ 
        {self.colors['yellow']}
                WEBROOTKIT OSINT TOOL v2.0
                github.com/webrootkit
        {self.colors['reset']}
        """
        print(banner)

    def check_pwned(self, email):
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                breaches = response.json()
                self.report.append(f"🔥 Утечек найдено: {len(breaches)}")
                for breach in breaches:
                    self.report.append(f"├─ {breach['Name']} ({breach['BreachDate']})")
                    self.report.append(f"└─ Утекло: {', '.join(breach['DataClasses'])}")
            else:
                self.report.append("✅ Email не найден в утечках.")
        except Exception as e:
            self.report.append(f"❌ Ошибка: {e}")

    def phone_lookup(self, phone):
        try:
            url = f"https://api.truecaller.com/v1/search?phone={phone}"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                self.report.append(f"📞 Информация по номеру {phone}:")
                self.report.append(f"├─ Имя: {data.get('name', 'N/A')}")
                self.report.append(f"├─ Страна: {data.get('country', 'N/A')}")
                self.report.append(f"└─ Email: {data.get('email', 'N/A')}")
            else:
                self.report.append("❌ Номер не найден в Truecaller.")
        except:
            self.report.append("❌ Ошибка Truecaller API.")

    def save_report(self, filename="osint_report.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.report))
        print(f"{self.colors['green']}✅ Отчет сохранен в {filename}{self.colors['reset']}")

if __name__ == "__main__":
    tool = WebrootkitOSINT()
    tool.print_banner()
    
    parser = argparse.ArgumentParser(description="Webrootkit OSINT Tool")
    parser.add_argument("--email", help="Проверить email в утечках")
    parser.add_argument("--phone", help="Пробить номер телефона")
    args = parser.parse_args()

    if args.email:
        tool.check_pwned(args.email)
    if args.phone:
        tool.phone_lookup(args.phone)
    
    tool.save_report()