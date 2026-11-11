"""
RECORD CHECK  -  my version
===========================

Name  : Bushra Mateen
Lane  : Cyber 
Date  : 11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """Cleaning and converting one raw cybersecurity record into a dictionary."""

    raw_line = raw_line.strip().lower()

    fields = raw_line.split(",")

    record = {}

    for field in fields:

        if "=" not in field:
            continue

        key, value = field.split("=")

        key = key.strip()
        value = value.strip()

        if key == "attempts":
            value = int(value)

        record[key] = value

    return record



def status_of(record):
    """Check whether a cybersecurity record should be flagged."""

    if "result" not in record:
        return "INVALID"

    if record["result"] == "failed":
        return "FLAGGED"
    else:
        return "OK"


raw_records = []

with open("Cyber_records.txt", "r") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)



total_records = 0
flagged_records = 0

for raw_record in raw_records:

    cleaned_record = parse_line(raw_record)

    status = status_of(cleaned_record)

    print("Record:", cleaned_record)
    print("Status:", status)
    print()

    total_records += 1

    if status == "FLAGGED":
        flagged_records += 1


print("SUMMARY")
print("Total records:", total_records)
print("Flagged records:", flagged_records)
