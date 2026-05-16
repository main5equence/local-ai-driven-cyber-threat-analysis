import json
from datetime import datetime


def create_alert(event_type, source_ip, severity):

    alert = {
        "timestamp": str(datetime.now()),
        "event_type": event_type,
        "source_ip": source_ip,
        "severity": severity
    }

    filename = f"alerts/{event_type}_{source_ip}.json"

    with open(filename, "w") as file:
        json.dump(alert, file, indent=4)

    return alert
