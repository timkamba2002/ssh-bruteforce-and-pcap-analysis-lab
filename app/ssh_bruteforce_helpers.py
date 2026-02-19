import re
from collections import Counter

AUTH_LOG_PATH = "data/auth.log"

SSH_FAILED_PATTERN = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")
# [file:3]
def analyze_auth_log(path: str = AUTH_LOG_PATH, brute_force_threshold: int = 10):
    ip_counts = Counter()
    total_failed = 0

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = SSH_FAILED_PATTERN.search(line)
            if match:
                ip = match.group(1)
                ip_counts[ip] += 1
                total_failed += 1

    suspected_bruteforce = {
        ip: count for ip, count in ip_counts.items() if count >= brute_force_threshold
    }

    return {
        "total_failed": total_failed,
        "per_ip": dict(ip_counts),
        "suspected_bruteforce": suspected_bruteforce,
        "threshold": brute_force_threshold,
    }
