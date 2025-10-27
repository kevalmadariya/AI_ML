import requests

def scrape_chartink_all_pages(scan_clause, max_pages=10):
    url = "https://chartink.com/screener/process"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://chartink.com/screener/macd-crossover-bearish-bullish",
        "X-Requested-With": "XMLHttpRequest",
    }

    all_stocks = []
    for page in range(1, max_pages + 1):
        payload = {"scan_clause": scan_clause, "page": page}
        resp = requests.post(url, data=payload, headers=headers)
        data = resp.json()
        stocks = data.get("data", [])
        if not stocks:
            break  # no more pages
        all_stocks.extend(stocks)
        print(f"✅ Page {page} -> {len(stocks)} stocks")

    return [
        {
            "name": s["name"],
            "code": s["nsecode"],
            "price": s["close"],
        }
        for s in all_stocks
    ]


# Example: MACD crossover screener
scan_clause = """
( {cash} ( [0] 5 day ema(close) > [0] 12 day ema(close)
and [1] 5 day ema(close) <= [1] 12 day ema(close) ) )
"""

if __name__ == "__main__":
    results = scrape_chartink_all_pages(scan_clause, max_pages=2)
    print(f"Total stocks: {len(results)}")
    for s in results[:10]:
        print(s)
