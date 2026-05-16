from scapy.all import sniff, IP
from rich import print

from app.monitor.anomaly_detector import detect_port_scan
from app.incidents.json_generator import create_alert
from app.analyzer.ai_engine import analyze_alert
from app.database.save_threat import save_threat


def process_packet(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        print(f"[green][PACKET][/green] {src} -> {dst}")

        suspicious = detect_port_scan(src)

        if suspicious:

            print(f"[bold red][ALERT][/bold red] Possible port scan from {src}")

            alert = create_alert(
                event_type="PORT_SCAN",
                source_ip=src,
                severity="HIGH"
            )

            ai_response = analyze_alert(alert)

            print("\n[bold cyan]AI ANALYSIS[/bold cyan]")
            print(ai_response)

            save_threat(alert, ai_response)
def start_sniffer():

    print("[bold blue]Starting packet sniffer...[/bold blue]")

    sniff(
        prn=process_packet,
        store=False
    )
