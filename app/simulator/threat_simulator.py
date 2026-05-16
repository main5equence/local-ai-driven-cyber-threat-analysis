import random
from datetime import datetime

THREAT_TYPES = [
    "PORT_SCAN",
    "BRUTE_FORCE",
    "DNS_TUNNELING",
    "MALWARE_TRAFFIC",
    "DATA_EXFILTRATION",
    "BEACONING",
    "DDOS_ATTEMPT",
    "SUSPICIOUS_DEVICE"
]

SEVERITIES = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]


def generate_fake_alert():

    return {
        "timestamp": str(datetime.now()),
        "event_type": random.choice(THREAT_TYPES),
        "source_ip": f"192.168.0.{random.randint(1, 255)}",
        "severity": random.choice(SEVERITIES)
    }
