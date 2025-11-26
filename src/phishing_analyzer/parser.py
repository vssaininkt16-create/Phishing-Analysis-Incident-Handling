"""Simple email parser to split headers and body."""
from typing import Dict


def parse_email_text(raw: str) -> Dict[str, str]:
    """Parse a raw RFC-822-like email text into headers and body.

    This is intentionally simple and works with exported raw emails saved as text.
    """
    parts = raw.split("\n\n", 1)
    if len(parts) == 2:
        headers, body = parts
    else:
        headers = raw
        body = ""
    return {"headers": headers.strip(), "body": body.strip()}


def parse_email_file(path: str) -> Dict[str, str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    return parse_email_text(raw)
