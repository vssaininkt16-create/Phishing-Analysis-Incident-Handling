# Phishing Analysis & Incident Handling

## Overview
This project shows a real workflow for analyzing suspicious emails and responding to phishing incidents. It includes email header review, URL inspection, threat intelligence lookup, and incident documentation.

## Objectives
- Identify phishing emails
- Analyze email headers
- Inspect suspicious URLs
- Lookup threats on intelligence platforms
- Document incidents using NIST IR framework

## Tools Used
- Email Header Analyzer
- VirusTotal / Hybrid Analysis
- URLScan.io
- WHOIS Lookup

## NIST Incident Response Phases
1. Preparation
2. Detection & Analysis
3. Containment, Eradication & Recovery
4. Post-Incident Activity

## How to Use
1. Place suspicious emails in the `samples` folder
2. Analyze headers and URLs
3. Check threat intelligence reports
4. Document findings in `reports/investigation_report.md`

## Quickstart
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m phishing_analyzer.cli analyze sample_email.txt --output report.html
```

## Components
- `src/phishing_analyzer`: core parsing, indicator extraction, enrichment stubs, scoring, and reporting
- `tests/`: unit tests (run with `pytest`)
- GitHub Actions workflow for CI

If you want a web UI, run the FastAPI app in `src/phishing_analyzer/cli.py` with `--serve`.
