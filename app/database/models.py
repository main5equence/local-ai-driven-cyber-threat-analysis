from sqlalchemy import Column, Integer, String, DateTime

from app.database.db import Base


class Threat(Base):

    __tablename__ = "threats"

    id = Column(Integer, primary_key=True)

    timestamp = Column(String)
    event_type = Column(String)
    source_ip = Column(String)
    severity = Column(String)
    ai_analysis = Column(String)
    