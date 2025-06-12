# deploy_stop.py
import os
import subprocess
from pathlib import Path

CONTAINER_NAME = "tfidf_app"
CONTAINER_ID_FILE = ".container_id"

def run_command(command):
    print(f"> Running: {command}")
    subprocess.run(command, shell=True)

def main():
    if not Path(CONTAINER_ID_FILE).exists():
        print("❌ No container info found (.container_id file is missing). Trying to stop by name...")

        # Try stopping by container name
        run_command(f"docker stop {CONTAINER_NAME}")
        run_command(f"docker rm {CONTAINER_NAME}")
        return

    with open(CONTAINER_ID_FILE, "r") as f:
        container_id = f.read().strip()

    if not container_id:
        print("⚠️ Container ID is empty in .container_id file. Trying to stop by name...")
        run_command(f"docker stop {CONTAINER_NAME}")
        run_command(f"docker rm {CONTAINER_NAME}")
        return

    # Stop and remove container using ID
    run_command(f"docker stop {container_id}")
    run_command(f"docker rm {container_id}")

    # Cleanup
    os.remove(CONTAINER_ID_FILE)
    print(f"✅ Container {container_id} stopped and removed.")

if __name__ == "__main__":
    main()

# Run with:
# python3 deploy_stop.py
