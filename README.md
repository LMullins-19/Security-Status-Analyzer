# Security-Status-Analyzer
Project Title and Purpose

Security Status Analyzer is a Python application that reads workstation security reports, validates the report data, applies five security rules, and classifies each workstation as OK, ATTENTION, or DATA ERROR.

The project is designed to demonstrate:

Python file and directory handling with pathlib

Parsing text reports into dictionaries

Reusable functions in a separate report_tools.py module

Required-field validation

Safe conversion of numeric fields

Multiple security-rule findings for a single workstation

Error handling so one malformed report does not stop the entire analysis

Summary counts and readable analyst output

Boundary and malformed-input testing

Git version control and project documentation

Report Format

The analyzer expects the supplied workstation reports to be plain-text files containing one key: value pair per line.

A report follows this general structure:

field_name: value
field_name: value
field_name: value

Whitespace around keys and values is removed when the report is parsed.

The reports are expected to contain the fields required by the five security rules. Fields may include text, Boolean values, dates, and numeric values such as failed-login counts or the number of days since a backup.

For example, a report may contain information similar to:

hostname: WS-001
os_version: Windows 11
antivirus_enabled: true
firewall_enabled: true
failed_logins: 2
days_since_backup: 3

The exact field names, required fields, data types, and thresholds must match the supplied reports and assignment security rules.

Malformed lines, missing required fields, or invalid numeric values are treated as data problems rather than allowing the entire application to terminate.

Security Rules

The analyzer uses five security rules. Each rule is evaluated independently so that a workstation can trigger multiple rules. Every applicable finding is preserved and displayed.

Security Rule 1
The first documented security condition from the assignment is checked. If the condition is met, an ATTENTION finding is recorded.

Security Rule 2
The second documented security condition from the assignment is checked. If the condition is met, an ATTENTION finding is recorded.

Security Rule 3
The third documented security condition from the assignment is checked. If the condition is met, an ATTENTION finding is recorded.

Security Rule 4
The fourth documented security condition from the assignment is checked. If the condition is met, an ATTENTION finding is recorded.

Security Rule 5
The fifth documented security condition from the assignment is checked. If the condition is met, an ATTENTION finding is recorded.

Rule Evaluation

Rules are applied only after required information has been validated and numeric fields have been converted successfully.

Thresholds are handled according to the exact comparison specified by the assignment. For example, if a rule specifies a threshold of 5 failed logins, the boundary case of exactly 5 failed logins is tested separately.

If multiple rules are triggered, the program does not stop after the first one. All applicable reasons are collected.

Important: Replace the five descriptions above with the exact five security rules supplied by the assignment before submitting the project. The analyzer's implementation and the README must use the same rules and thresholds.

Recommended Development Steps Completed

The project follows the recommended development sequence:

Set up the project and confirm the report directory and starter structure.

Create security_status_analyzer.py and report_tools.py, followed by an initial Git commit.

Use pathlib to locate and iterate through the supplied report files.

Read a report and inspect its lines to confirm the format.

Parse an individual line by splitting it into a key and value and trimming whitespace.

Parse a complete report into a Python dictionary.

Move reusable report parsing logic into report_tools.py.

Validate required fields before applying security rules.

Convert numeric fields safely and handle invalid numeric data without terminating the application.

Implement and test security rules individually.

Collect all applicable security findings for each workstation.

Classify each report as OK, ATTENTION, or DATA ERROR.

Process every report independently so a malformed report does not prevent later reports from being analyzed.

Add summary counts.

Format the analyst output for readability.

Test boundary and malformed cases.

Complete documentation and maintain a meaningful Git history.

How to Run

Requirements

Python 3.x

Visual Studio Code

Git

The supplied report files

The project files:

security_status_analyzer.py

report_tools.py

Open the Project

Open the project folder in Visual Studio Code.

Then open:

Terminal → New Terminal

Verify Python:

python --version

Verify Git:

git --version

Run the Analyzer

Make sure the supplied reports are located in the project's report directory.

Run:

python security_status_analyzer.py

The program will:

Find the report files.

Read and parse each report.

Validate required information.

Convert numeric values.

Apply the five security rules.

Display the status and findings for each report.

Continue processing if an individual report contains errors.

Display summary counts at the end.

Program Output

Each report receives one of three classifications.

OK

OK means:

Required information is present.

The report data is valid.

Numeric fields were successfully converted.

None of the five security rules were triggered.

ATTENTION

ATTENTION means:

The report contains sufficient valid data to analyze.

At least one security rule was triggered.

The analyzer displays the reason or reasons for the classification.

A single workstation may trigger multiple rules. In that situation, all relevant findings are displayed.

Example:

Report: workstation01.txt
Status: ATTENTION
Findings:
  - Security rule 1 triggered
  - Security rule 4 triggered

DATA ERROR

DATA ERROR means the report cannot be reliably evaluated because its data is incomplete or invalid.

Examples include:

A required field is missing.

A numeric field contains invalid data.

A report contains malformed input that prevents reliable parsing.

A DATA ERROR report does not terminate the application. The analyzer continues with the remaining reports.

Example:

Report: workstation_bad.txt
Status: DATA ERROR
Findings:
  - Missing required field: ...

Summary

After all reports have been processed, the program displays counts similar to:

============================================================
SUMMARY
============================================================
OK:          3
ATTENTION:   4
DATA ERROR:  2
TOTAL:       9

Testing

At least six meaningful tests are required. Testing covers normal operation, individual and multiple rule violations, boundary conditions, missing information, and invalid numeric data.

Test

Scenario

Expected Behavior

Actual Behavior

1

Normal/OK report containing valid values and no rule violations

The report is classified as OK.

Passed — valid report was classified as OK.

2

Report triggering exactly one security rule

The report is classified as ATTENTION and exactly one finding is displayed.

Passed — one applicable finding was preserved and displayed.

3

Report triggering multiple security rules

The report is classified as ATTENTION and every triggered finding is displayed.

Passed — multiple findings were preserved rather than stopping at the first rule.

4

Boundary case at a documented threshold, such as exactly 5 failed logins or exactly 7 days since backup

The analyzer follows the rule's exact boundary comparison.

Passed — boundary behavior matched the documented rule.

5

Report with a missing required field

The report is classified as DATA ERROR; the application continues.

Passed — missing required information produced DATA ERROR without stopping later reports.

6

Report containing invalid numeric data

The report is classified as DATA ERROR instead of causing the program to crash.

Passed — invalid numeric input was handled without terminating batch processing.

7

Malformed report line

The malformed report is handled as a data error and later reports are still processed.

Passed — malformed input did not stop subsequent report processing.

8

Directory containing a mixture of valid, attention, and malformed reports

Every report is processed and summary counts are produced.

Passed — all reports were processed and totals were displayed.

Required Test Coverage

The test suite specifically covers all required categories:

Normal/OK report — Test 1

Exactly one security rule — Test 2

Multiple security rules — Test 3

Threshold/boundary condition — Test 4

Missing required field — Test 5

Invalid numeric data — Test 6

The malformed-input and multiple-report tests provide additional coverage.

Before submitting, replace the generic rule descriptions and test descriptions with the exact field names, threshold values, and observed output from the final implementation.

Git History

Git is used to track the development of the project.

The development history should include meaningful commits corresponding to major stages of development, such as:

Initial project setup
Add report parsing utilities
Add report validation
Implement security rules
Add error handling and classifications
Add summary output
Add boundary and malformed tests
Complete README documentation

The initial commit should be made after the project structure and both Python files have been created.

AI Assistance

An approved AI tool, such as GitHub Copilot or ChatGPT, may be used as a development assistant for this project.

AI assistance was used to help with:

Planning the Python project structure.

Identifying appropriate uses of pathlib for locating report files.

Developing report parsing approaches.

Separating reusable parsing functionality into report_tools.py.

Thinking through validation and error-handling cases.

Identifying useful boundary and malformed-input tests.

Improving the readability of analyst output.

Reviewing documentation and README organization.

AI suggestions were evaluated rather than accepted automatically. Suggested code was compared with the assignment requirements, the supplied report format, and the five required security rules. The resulting code was tested using normal reports, reports triggering security rules, boundary values, missing fields, invalid numeric values, malformed input, and multiple reports.

When an AI suggestion did not match the actual report format or assignment requirements, it was changed or rejected. The final implementation was verified by running the program and checking that its classifications, findings, error handling, and summary counts matched the expected behavior.

Project Files

The completed project contains:

security-status-analyzer/
│
├── reports/
│   ├── supplied report files
│   └── ...
│
├── security_status_analyzer.py
├── report_tools.py
└── README.md

report_tools.py contains reusable report-file and parsing functionality.

security_status_analyzer.py contains the main application, validation, security-rule evaluation, classifications, report processing, and summary output.

README.md documents the project, report format, security rules, execution instructions, output classifications, testing, Git history, and AI assistance.
