from phishing_analyzer.indicators import extract_urls, extract_domains_from_urls, extract_ips


def test_extract_urls_and_domains():
    text = "Hello visit https://example.com/path and http://malicious.test/?q=1"
    urls = extract_urls(text)
    assert "https://example.com/path" in urls
    domains = extract_domains_from_urls(urls)
    assert "example.com" in domains


def test_extract_ips():
    text = "Connect to 192.168.1.5 or 8.8.8.8"
    ips = extract_ips(text)
    assert "192.168.1.5" in ips
    assert "8.8.8.8" in ips
