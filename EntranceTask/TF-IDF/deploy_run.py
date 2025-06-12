# deploy_run.py
import subprocess
import os
from pathlib import Path

# Constants
CONTAINER_NAME = "tfidf_app"
CONTAINER_ID_FILE = ".container_id"
PROJECT_DIR = Path(__file__).parent.resolve()

def run_command(command, cwd=None):
    print(f"> Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd or PROJECT_DIR)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}")

def main():
    print("🔧 Starting deployment...")

    # Step 1: Install dependencies
    run_command("pip install -r requirements.txt")

    # Step 2: Create .env
    run_command("python setup_env.py")

    # Step 3: Create database
    run_command("python -m db_schema.db_create")

    # Step 4: Build and run Docker
    run_command(f"docker compose build")
    run_command(f"docker compose up -d --force-recreate")

    # Step 5: Save container ID
    container_id = subprocess.check_output(
        f"docker ps -qf name={CONTAINER_NAME}", shell=True
    ).decode("utf-8").strip()

    if container_id:
        with open(CONTAINER_ID_FILE, "w") as f:
            f.write(container_id)
        print(f"✅ Container '{CONTAINER_NAME}' is running with ID: {container_id}")
    else:
        print("⚠️ Could not find running container.")

if __name__ == "__main__":
    main()

# Run with:
# python deploy_run.py
