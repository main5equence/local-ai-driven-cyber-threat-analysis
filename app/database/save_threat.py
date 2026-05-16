from app.database.db import SessionLocal
from app.database.models import Threat


def save_threat(alert, ai_analysis):

    print("Saving threat to database...")

    db = SessionLocal()

    threat = Threat(
        timestamp=alert["timestamp"],
        event_type=alert["event_type"],
        source_ip=alert["source_ip"],
        severity=alert["severity"],
        ai_analysis=ai_analysis
    )

    db.add(threat)

    db.commit()

    db.close()

    print("Threat saved.")
    