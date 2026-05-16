import time

from app.simulator.threat_simulator import generate_fake_alert
from app.analyzer.ai_engine import analyze_alert
from app.database.save_threat import save_threat


for i in range(20):

    alert = generate_fake_alert()

    print(f"Generating threat: {alert['event_type']}")

    ai_analysis = analyze_alert(alert)

    save_threat(alert, ai_analysis)

    time.sleep(1)
    