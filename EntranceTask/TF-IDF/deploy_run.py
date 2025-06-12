# deploy_run.py
import subprocess
import os
from pathlib import Path

# Constants
CONTAINER_NAME = "tfidf_app"
IMAGE_NAME = "tfidf_image"
IMAGE_TAG = "latest"
HOST_PORT = 9000
CONTAINER_PORT = 9000
CONTAINER_ID_FILE = ".container_id"
PROJECT_DIR = Path(__file__).parent.resolve()

def run_command(command, cwd=None):
    print(f"> Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd or PROJECT_DIR)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}")

def main():
    print("🔧 Starting deployment...")

    # Step 1: Create .env file
    run_command("python3 setup_env.py")

    # Step 2: Initialize the database
    run_command("python3 -m db_schema.db_create")

    # Step 3: Build Docker image
    run_command(f"docker build -t {IMAGE_NAME}:{IMAGE_TAG} .")

    # Step 4: Run container
    run_command(
        f"docker run --name {CONTAINER_NAME} "
        f"-p {HOST_PORT}:{CONTAINER_PORT} "
        f"-d {IMAGE_NAME}:{IMAGE_TAG}"
    )

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
# python3 deploy_run.py
