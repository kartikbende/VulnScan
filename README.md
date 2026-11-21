# VulnScan 🔍
            
**A Python-Based Network Vulnerability Scanner**

VulnScan is a Python-based cybersecurity project designed to identify open TCP ports, detect running services, extract service version information, and identify potential security vulnerabilities by mapping detected versions against known CVE records.

The project demonstrates fundamental concepts of network scanning, service enumeration, banner grabbing, regular expressions, vulnerability assessment, and security reporting.

## 🎯 Project Objectives

- Identify open TCP ports on authorized target systems.
- Detect services running on discovered ports.
- Retrieve service banners and version information.
- Extract product and version details using regular expressions.
- Map detected software versions against a local CVE database.
- Generate structured vulnerability assessment reports.

## ⚙️ Planned Features

- [ ] TCP port scanning
- [ ] Multi-threaded scanning
- [ ] Service detection
- [ ] Banner grabbing
- [ ] Software version extraction using Regex
- [ ] Local CVE database integration
- [ ] Vulnerability matching engine
- [ ] CVE severity classification
- [ ] JSON report generation
- [ ] Command-line interface

## 🏗️ Architecture

```text
Target IP
    |
    v
Port Scanner
    |
    v
Service Detection
    |
    v
Banner Grabbing
    |
    v
Version Extraction (Regex)
    |
    v
CVE Matching Engine
    |
    v
Vulnerability Assessment
    |
    v
Report Generation
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Socket | TCP port scanning |
| Threading | Concurrent scanning |
| Regex | Version extraction and matching |
| JSON | Local CVE database |
| NVD CVE Database | Vulnerability reference data |
| Git & GitHub | Version control and documentation |

## 📁 Project Structure

```text
VulnScan/
├── vulnscan/
├── database/
├── reports/
├── tests/
├── docs/
├── screenshots/
├── README.md
├── requirements.txt
└── LICENSE
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/kartikbende/VulnScan.git
cd VulnScan
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

Usage instructions and command-line examples will be added as the scanner implementation progresses.

## 📊 Vulnerability Identification Methodology

VulnScan uses service and version information collected during scanning to identify potential vulnerabilities.

The initial matching methodology uses regular expressions and a locally maintained CVE dataset.

A version match indicates a potential vulnerability and requires further validation against vendor advisories and vulnerability conditions.

## ⚠️ Limitations

- Detection depends on available service banners and version information.
- Initial CVE matching relies on a limited local dataset.
- Regex-based matching may produce false positives or false negatives.
- Backported security patches may not be recognized from version strings alone.
- A matching CVE does not establish exploitability.

## 🔐 Legal Disclaimer

VulnScan is developed for educational and authorized security assessment purposes only.

Only scan systems that you own or have explicit permission to assess.

The developer is not responsible for misuse of this tool.

## 👨‍💻 Author

**Kartik Bende**

- GitHub: [@kartikbende](https://github.com/kartikbende)
- LinkedIn: [Kartik Bende](https://www.linkedin.com/in/kartikbende/)

---

*VulnScan — Understand your network. Identify potential vulnerabilities.*
