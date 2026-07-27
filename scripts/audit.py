from pathlib import Path

LOG_DIR = Path("logs")

def audit_logs():
    """Display available log files."""
    if not LOG_DIR.exists():
        print("No log directory found.")
        return

    for logfile in LOG_DIR.glob("*.log"):
        print(logfile.name)

if __name__ == "__main__":
    audit_logs()