# Here begins a new world ...

import sys
from pathlib import Path
from typing import List, Dict


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }


def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Failed to read the file: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts):
        print(f"{level:<17} | {counts[level]}")


def display_logs_by_level(logs: List[dict], level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in filter_logs_by_level(logs, level):
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile> [level]")
        sys.exit(1)

    log_path = Path(sys.argv[1])
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(str(log_path))
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        display_logs_by_level(logs, level_filter)


if __name__ == "__main__":
    main()
