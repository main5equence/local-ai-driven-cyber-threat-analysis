from app.database.db import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

print("Database created.")
