"""CLI entrypoint for the phishing analyzer."""
import argparse
import json
import sys
from pathlib import Path

from .parser import parse_email_file
from .indicators import extract_urls, extract_domains_from_urls, extract_ips
from .enrich import whois_lookup, virustotal_lookup
from .score import score_indicators
from .report import make_html_report, make_json_report


def analyze_path(path: str):
    data = parse_email_file(path)
    text = data.get("headers", "") + "\n\n" + data.get("body", "")
    urls = extract_urls(text)
    domains = extract_domains_from_urls(urls)
    ips = extract_ips(text)

    # enrichment (stubs)
    domains_enriched = {d: whois_lookup(d) for d in domains}
    indicators_vt = {i: virustotal_lookup(i) for i in urls + ips}

    score = score_indicators(urls, domains, ips)

    result = {
        "source": str(path),
        "indicators": {"urls": urls, "domains": domains, "ips": ips},
        "domains_enriched": domains_enriched,
        "intel": indicators_vt,
        "score": score,
    }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(prog="phishing-analyzer")
    sub = parser.add_subparsers(dest="cmd")
    p_analyze = sub.add_parser("analyze", help="Analyze a raw email file")
    p_analyze.add_argument("input", help="Path to raw email text file")
    p_analyze.add_argument("--output", help="Write report file (html or json)")
    p_analyze.add_argument("--serve", action="store_true", help="Run web server (FastAPI)")

    args = parser.parse_args(argv)
    if args.cmd == "analyze":
        result = analyze_path(args.input)
        if args.output:
            out = Path(args.output)
            if out.suffix == ".html":
                out.write_text(make_html_report(result), encoding="utf-8")
            else:
                out.write_text(make_json_report(result), encoding="utf-8")
            print(f"Wrote report to {out}")
        else:
            print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
