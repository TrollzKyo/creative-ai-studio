from pathlib import Path
from datetime import datetime


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def log(message: str):

    today = datetime.now().strftime("%Y-%m-%d")

    logfile = LOG_DIR / f"{today}.log"

    now = datetime.now().strftime("%H:%M:%S")

    with logfile.open("a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")