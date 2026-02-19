import os
from datetime import datetime

from app.ssh_bruteforce_helpers import analyze_auth_log
from app.pcap_analyzer import count_packets_by_protocol  # [file:5]

AUTH_LOG_PATH = os.path.join("data", "auth.log")
PCAP_PATH = os.path.join("data", "network_sec_monitoring2.pcap")
REPORT_OUT = os.path.join("reports", "Security-Report-generated.txt")


def analyze_pcap(path: str):
    return count_packets_by_protocol(path)  # returns dict with total/tcp/udp/icmp/arp [file:5]


def write_report(auth_results: dict, pcap_results: dict, out_path: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("Security Report\n")
        f.write(f"Generated: {now}\n")
        f.write("Analyst: Timothy Kamba\n\n")

        # Findings
        f.write("Findings:\n")
        f.write(
            f"1. Failed Logins: Detected {auth_results['total_failed']} failed SSH login attempts "
            f"across {len(auth_results['per_ip'])} unique source IPs.\n"
        )

        if auth_results["suspected_bruteforce"]:
            f.write(
                f"   - Suspected brute-force activity from the following IPs "
                f"(>= {auth_results['threshold']} failed attempts):\n"
            )
            for ip, count in sorted(
                auth_results["suspected_bruteforce"].items(),
                key=lambda x: x[1],
                reverse=True,
            ):
                f.write(f"       • {ip}: {count} failed attempts\n")
        else:
            f.write(
                "   - No IPs exceeded the brute-force threshold during the analyzed period.\n"
            )

        f.write(
            f"2. Network Anomalies: PCAP contains {pcap_results['total']} packets "
            f"(TCP={pcap_results['tcp']}, UDP={pcap_results['udp']}, "
            f"ICMP={pcap_results['icmp']}, ARP={pcap_results['arp']}).\n"
        )

        f.write("3. System Status: Log and PCAP data reviewed for SSH and basic L3/L4 activity.\n\n")

        # Recommendations [file:8]
        f.write("Recommendations:\n")
        f.write("- Enable multi-factor authentication (MFA) for SSH where possible.\n")
        f.write("- Disable direct root login over SSH and enforce key-based authentication.\n")
        f.write("- Investigate and, if appropriate, block IPs showing sustained brute-force behavior.\n")
        f.write("- Maintain regular system updates and log/PCAP review procedures.\n")


def main():
    print("[*] Analyzing auth.log for failed SSH logins...")
    auth_results = analyze_auth_log(AUTH_LOG_PATH)

    print("[*] Analyzing PCAP for protocol statistics...")
    pcap_results = analyze_pcap(PCAP_PATH)

    print(f"[*] Writing report to {REPORT_OUT} ...")
    write_report(auth_results, pcap_results, REPORT_OUT)

    print("[+] Done.")
    print(f"    Failed SSH attempts: {auth_results['total_failed']}")
    print(f"    Suspected brute-force IPs: {len(auth_results['suspected_bruteforce'])}")
    print(f"    Total packets in PCAP: {pcap_results['total']}")


if __name__ == "__main__":
    main()
