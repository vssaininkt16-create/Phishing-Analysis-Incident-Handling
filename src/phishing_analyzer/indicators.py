"""Indicator extraction helpers."""
import re
from typing import List
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[\w\-\._~:/?#\[\]@!$&'()*+,;=%]+", re.IGNORECASE)
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def extract_urls(text: str) -> List[str]:
    return list({m.group(0) for m in URL_RE.finditer(text)})


def extract_domains_from_urls(urls: List[str]) -> List[str]:
    domains = set()
    for u in urls:
        try:
            p = urlparse(u)
            host = p.hostname
            if host:
                domains.add(host.lower())
        except Exception:
            continue
    return list(domains)


def extract_ips(text: str) -> List[str]:
    # Note: this is a loose IP matcher
    return list({m.group(0) for m in IP_RE.finditer(text)})
