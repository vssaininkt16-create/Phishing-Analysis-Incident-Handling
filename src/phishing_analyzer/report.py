"""Generate simple HTML/JSON reports from analysis results."""
from typing import Dict
import json


HTML_TEMPLATE = """
<html>
<head><meta charset="utf-8"><title>Phishing Analysis Report</title></head>
<body>
<h1>Phishing Analysis Report</h1>
<pre>{content}</pre>
</body>
</html>
"""


def make_json_report(result: Dict) -> str:
    return json.dumps(result, indent=2)


def make_html_report(result: Dict) -> str:
    return HTML_TEMPLATE.format(content=make_json_report(result))
