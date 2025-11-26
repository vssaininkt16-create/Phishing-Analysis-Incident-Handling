"""Enrichment stubs for threat intel lookups.

These functions are intentionally simple placeholders. Integrate external
APIs (VirusTotal, WHOIS, PassiveDNS) by implementing the functions below
and providing API keys via environment variables or config.
"""
from typing import Dict


def whois_lookup(domain: str) -> Dict[str, str]:
    # Placeholder: return minimal structure
    return {"domain": domain, "registrar": None, "created": None}


def virustotal_lookup(indicator: str) -> Dict[str, str]:
    # Placeholder: return basic structure indicating no findings
    return {"indicator": indicator, "positives": 0, "total_scans": 0}
