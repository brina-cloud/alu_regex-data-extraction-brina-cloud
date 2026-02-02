This project is data extraction regex project with sampleinput txt file, sampleoutput.json and samplecode.py python with source code for regex of data types: phone number, time, hashtags and email addresses. From the sample input text.

Purpose:
**

# ALU Regex Data Extraction 📦

**Purpose:**
A small utility for extracting commonly-used data types (emails, phone numbers, hashtags, and times) from raw text using regular expressions. This repository contains a sample input file, a Python script (`samplecode.py`) that performs extraction and simple privacy masking, and an output file that records results.

---

## Files

- `sampleinput.txt` — realistic raw input log used for testing and demonstration.
- `samplecode.py` — extraction script (reads `sampleinput.txt`, extracts patterns, masks emails, and writes `sampleoutput.txt`).
- `sampleoutput.txt` — generated output from `samplecode.py`.

---

## How it works 🔧

- The script reads the raw text file and applies regex patterns to find:
  - Email addresses
  - 10-digit phone numbers and various phone formats
  - Hashtags (e.g., `#ProductLaunch`)
  - Time formats (e.g., `14:30`, `2:30 PM`, ISO timestamps)
- Found values are validated with a simple `security()` check to filter known risky patterns.
- Emails are partially obfuscated with `hide_email()` before writing to the output for privacy.

---

## Usage

1. Ensure Python 3 is installed.
2. From the project directory run:

```bash
python samplecode.py
```

3. Check `sampleoutput.txt` for extracted results.

---

## Notes & Limitations ⚠️

- Regex patterns are intentionally simple: they may not catch every valid international format or edge case.
- The `security()` function contains rules to detect risky input patterns; review and expand these checks for production use.
- The script assumes well-formed input; malformed entries are included in `sampleinput.txt` for testing.

---

## Testing & Extending 💡

- Add cases to `sampleinput.txt` to verify regex coverage and edge cases (e.g., `user+tag@example.com`, international phone formats, malformed emails).
- Consider replacing any third-party `regex` usage with Python's stdlib `re` if portability is desired.

---

Contributions and improvements are welcome — open an issue or submit a pull request. ✅


