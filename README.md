# SSH Brute Force and PCAP Analysis Lab

Small blue-team lab that uses Python to detect SSH brute-force activity from Linux `auth.log` and analyze basic network traffic patterns from PCAP captures.

## Features

- Parse Linux `auth.log` entries into timestamp, host, process, PID, and message fields using regular expressions.
- Count failed SSH logins per source IP and highlight suspected brute-force activity based on a configurable threshold.
- Load PCAP files with Scapy and count total packets as well as TCP, UDP, ICMP, and ARP.
- Generate a short security report summarizing findings and basic hardening recommendations.

## Layout

- `code/` – Python scripts for log parsing, brute-force detection, and PCAP analysis.
- `data/` – sample `auth.log` and PCAP files.
- `reports/` – security report template and generated report(s).

## Quickstart

```bash
git clone https://github.com/timkamba2002/ssh-bruteforce-and-pcap-analysis-lab.git
cd ssh-bruteforce-and-pcap-analysis-lab

pip install scapy

python code/pcap_analyzer.py
python code/ssh_bruteforce_detector.py
