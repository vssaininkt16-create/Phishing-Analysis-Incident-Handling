"""Simple scoring engine for indicators."""
from typing import Dict, List


def score_indicators(urls: List[str], domains: List[str], ips: List[str]) -> Dict[str, int]:
    score = 0
    reasons = []
    if urls:
        score += min(30, len(urls) * 5)
        reasons.append(f"{len(urls)} URLs")
    if domains:
        score += min(40, len(domains) * 6)
        reasons.append(f"{len(domains)} domains")
    if ips:
        score += min(30, len(ips) * 10)
        reasons.append(f"{len(ips)} IPs")

    # normalize to 0-100
    score = max(0, min(100, score))
    return {"score": score, "reasons": ", ".join(reasons)}
