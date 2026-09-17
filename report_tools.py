from pathlib import Path


def find_reports(report_directory):
    """Return all report files in the supplied directory."""
    return sorted(Path(report_directory).glob("*.txt"))

def parse_line(line):
    """Split a report line into a key and value."""
    key, value = line.split(":", 1)
    return key.strip(), value.strip()


def parse_report(report_path):
    """Read a complete report into a dictionary."""
    report = {}

    with report_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            key, value = parse_line(line)
            report[key] = value

    return report