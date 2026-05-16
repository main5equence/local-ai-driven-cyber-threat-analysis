from collections import defaultdict
import time

connection_tracker = defaultdict(list)


def detect_port_scan(src_ip):
    current_time = time.time()

    connection_tracker[src_ip].append(current_time)

    recent_connections = [
        t for t in connection_tracker[src_ip]
        if current_time - t < 10
    ]

    connection_tracker[src_ip] = recent_connections

    if len(recent_connections) > 20:
        return True

    return False
