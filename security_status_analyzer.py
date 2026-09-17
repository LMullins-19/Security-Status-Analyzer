from pathlib import Path

from report_tools import find_reports, parse_report


def analyze_report(report):
    reasons = []
    data_errors = []

    # Required-field validation
    required_fields = [
        # Add fields from the supplied reports here
    ]

    for field in required_fields:
        if field not in report or not report[field]:
            data_errors.append(f"Missing required field: {field}")

    if data_errors:
        return "DATA ERROR", data_errors

    # Security rules go here, one at a time.
    # Every triggered rule appends a reason instead of replacing
    # an earlier finding.

    if reasons:
        return "NEEDSATTENTION", reasons

    return "GOOD", []


def main():
    report_directory = Path("reports")
    reports = find_reports(report_directory)

    counts = {
        "GOOD": 0,
        "NEEDS ATTENTION": 0,
        "DATA ERROR": 0,
    }

    print("-" * 40)
    print("SECURITY STATUS ANALYZER")
    print("-" * 40)

    for report_path in reports:
        try:
            report = parse_report(report_path)
            status, reasons = analyze_report(report)

        except Exception as error:
            status = "DATA ERROR"
            reasons = [f"Unable to process report: {error}"]

        counts[status] += 1

        print(f"\nReport: {report_path.name}")
        print(f"Status: {status}")

        if reasons:
            print("Findings:")
            for reason in reasons:
                print(f"  - {reason}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"GOOD: {counts['GOOD']}")
    print(f"NEEDS ATTENTION: {counts['NEEDS ATTENTION']}")
    print(f"DATA ERROR: {counts['DATA ERROR']}")
    print(f"TOTAL: {sum(counts.values())}")


if __name__ == "__main__":
    main()