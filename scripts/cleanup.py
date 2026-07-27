"""Remove old temporary files."""
from datetime import datetime, timedelta
from pathlib import Path

def remove_old_files(directory: Path, retention_days: int = 14) -> int:
    if not directory.exists():
        return 0
    cutoff = datetime.now() - timedelta(days=retention_days)
    removed = 0
    for item in directory.iterdir():
        if item.is_file() and datetime.fromtimestamp(item.stat().st_mtime) < cutoff:
            item.unlink()
            removed += 1
    return removed
