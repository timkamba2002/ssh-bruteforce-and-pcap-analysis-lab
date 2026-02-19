# SSH Brute Force and PCAP Analysis Lab

Small blue-team lab that uses Python to detect SSH brute-force activity from Linux `auth.log` files and analyze basic network traffic patterns from PCAP captures.[file:1][file:5]

## Features

- Parse Linux `auth.log` entries into timestamp, host, process, PID, and message fields using regular expressions.[file:2][file:4]
- Count failed SSH logins per source IP and highlight suspected brute-force activity based on a configurable threshold.[file:1][file:3]
- Load PCAP files with Scapy and count total packets as well as TCP, UDP, ICMP, and ARP traffic.[file:5]
- Generate a security report summarizing findings from both the log and PCAP analysis plus basic hardening recommendations.[file:8]

## Project Layout

- `app/` – Python code:
  - `ssh_bruteforce_helpers.py` – logic to parse `auth.log` and aggregate failed SSH logins per IP.[file:1][file:3]
  - `pcap_analyzer.py` – functions to read PCAP files and compute protocol-level statistics.[file:5]
  - other helper scripts used during development.
- `data/` – sample `auth.log` and PCAP files used for analysis.[file:1][file:5]
- `reports/` – security report template and auto-generated report.
- `main.py` – orchestrates SSH log analysis and PCAP analysis, then writes a combined security report.[file:1][file:5][file:8]

## Quickstart

Clone the repository and move into it:

```bash
git clone https://github.com/timkamba2002/ssh-bruteforce-and-pcap-analysis-lab.git
cd ssh-bruteforce-and-pcap-analysis-lab
Install the required Python package:

bash
python -m pip install scapy
Run the combined analysis:

bash
python main.py
Review the generated report:

bash
cat reports/Security-Report-generated.txt
The report includes:

Total failed SSH login attempts and suspected brute-force source IPs.[file:1][file:3]

Total packets and basic protocol breakdown (TCP/UDP/ICMP/ARP) from the PCAP.[file:5]

High-level recommendations such as enabling MFA, disabling direct root login, and reviewing high-volume attacker IPs.[file:8]

Use Cases
Practice parsing Linux authentication logs for SSH security events.[file:1][file:2][file:3]

Build intuition around brute-force detection thresholds and attacker behavior.

Explore basic PCAP inspection workflows with Scapy from a blue-team perspective.[file:5]
