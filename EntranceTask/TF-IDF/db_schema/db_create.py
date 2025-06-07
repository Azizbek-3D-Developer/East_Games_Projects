from api.db import engine, metadata
from models import *

if __name__ == "__main__":
    metadata.create_all(engine)
    print("✅ Tables created")


# Runing command from the Project Root Folder
# python -m db_schema.db_create