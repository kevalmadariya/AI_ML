import re
import requests

import re
import requests
import html

def get_scan_clause(screener_url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    html_text = requests.get(screener_url, headers=headers).text

    # Try several patterns that ChartInk uses
    patterns = [
        r'"scan_clause":"(.*?)"',            # old pattern
        r"'scan_clause':'(.*?)'",            # single-quote variant
        r'scan_clause\s*[:=]\s*"(.*?)"',     # JS assignment pattern
    ]
    
    for pattern in patterns:
        match = re.search(pattern, html_text)
        if match:
            clause = match.group(1)
            clause = html.unescape(clause.encode().decode("unicode_escape"))
            return clause

    # As a fallback, try to extract from window.init_data
    match = re.search(r'window\.init_data\s*=\s*({.*?});', html_text, re.S)
    if match:
        block = match.group(1)
        clause_match = re.search(r'"scan_clause":"(.*?)"', block)
        if clause_match:
            clause = clause_match.group(1)
            clause = html.unescape(clause.encode().decode("unicode_escape"))
            return clause

    # If nothing matched, dump small preview for debugging
    print("⚠️ Could not find scan_clause. HTML preview:\n", html_text[:500])
    raise ValueError("scan_clause not found in page HTML!")

# Example usage
url = "https://chartink.com/screener/macd-crossover-bearish-bullish"
scan_clause = get_scan_clause(url)
print("Extracted scan clause:\n", scan_clause[:200], "...")

import requests

def scrape_chartink_all_pages(screener_url, max_pages=10):
    scan_clause = get_scan_clause(screener_url)
    print("Using scan_clause:", scan_clause[:150], "...")

    url = "https://chartink.com/screener/process"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": screener_url,
        "X-Requested-With": "XMLHttpRequest",
    }

    all_stocks = []
    for page in range(1, max_pages + 1):
        payload = {"scan_clause": scan_clause, "page": page}
        resp = requests.post(url, data=payload, headers=headers)
        data = resp.json()
        stocks = data.get("data", [])
        if not stocks:
            break
        all_stocks.extend(stocks)
        print(f"✅ Page {page}: {len(stocks)} stocks")

    # Transform into simple list
    return [
        {"name": s["name"], "code": s["nsecode"], "price": s["close"]}
        for s in all_stocks
    ]


if __name__ == "__main__":
    screener = "https://chartink.com/screener/macd-crossover-bearish-bullish"
    results = scrape_chartink_all_pages(screener, max_pages=20)
    print(f"\nTotal stocks found: {len(results)}")
    for s in results[:10]:
        print(s)
