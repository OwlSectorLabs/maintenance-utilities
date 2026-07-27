import shutil
from pathlib import Path

def backup(source, destination):
    """Copy files from the source folder to the destination."""
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(f"Backup completed: {source} -> {destination}")

if __name__ == "__main__":
    backup("data", "backups")