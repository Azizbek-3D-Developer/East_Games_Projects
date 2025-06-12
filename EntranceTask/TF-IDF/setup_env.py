import os

env_content = """APP_PORT=7500
UPLOAD_DIR=uploads
TOP_K_WORDS=50
APP_VERSION=3.0.0

DATABASE_URL=sqlite:///./tf_idf.db

DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=mypassword
DB_NAME=mydb
"""

env_path = os.path.join(os.path.dirname(__file__), ".env")

with open(env_path, "w") as f:
    f.write(env_content)

print(f".env file created at: {env_path}")

# python setup_env.py
