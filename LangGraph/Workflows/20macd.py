# import asyncio
# from playwright.async_api import async_playwright
# from bs4 import BeautifulSoup

# async def scrape_chartink_macd():
#     """
#     Scrapes stock names, codes, and prices from the ChartInk MACD crossover screener.
#     Returns a list of dicts: [{name, code, price}, ...]
#     """
    # async with async_playwright() as p:
    #     browser = await p.chromium.launch(headless=True)
    #     page = await browser.new_page()
        
    #     url = "https://chartink.com/screener/macd-crossover-bearish-bullish"
    #     await page.goto(url)
    #     print("✅ Page loaded... waiting for table...")
        
    #     # Wait until the results table appears
    #     await page.wait_for_selector("table tr a")
        
    #     # Get rendered HTML
    #     html = await page.content()
    #     await browser.close()

    #     # Parse with BeautifulSoup
    #     soup = BeautifulSoup(html, "html.parser")
    #     rows = soup.select("tbody tr")

    #     data = []
    #     for row in rows:
    #         cols = row.select("td")
    #         if len(cols) >= 6:
    #             data.append({
    #                 "name": cols[1].text.strip(),
    #                 "code": cols[2].text.strip(),
    #                 "price": cols[5].text.strip(),
    #             })
        
#         return data


# # Example usage
# if __name__ == "__main__":
#     results = asyncio.run(scrape_chartink_macd())
#     print(f"✅ Found {len(results)} stocks")
#     for stock in results[:10]:  # print first 10
#         print(stock)

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def bullish_macd_20_pick_sync():
    """
    Scrapes stock names, codes, and prices from the ChartInk MACD crossover screener.
    Returns a list of dicts: [{name, code, price}, ...]
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = "https://chartink.com/screener/macd-crossover-bearish-bullish"
        page.goto(url)
        print("✅ Page loaded... waiting for table...")

        # Wait until the results table appears
        page.wait_for_selector("table tr a")

        # Get rendered HTML
        html = page.content()
        browser.close()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select("tbody tr")

        data = []
        for row in rows:
            cols = row.select("td")
            if len(cols) >= 6:
                data.append({
                    "name": cols[1].text.strip(),
                    "code": cols[2].text.strip(),
                    "price": cols[5].text.strip(),
                })

        return data

# Example usage:
if __name__ == "__main__":
    results = bullish_macd_20_pick_sync()
    print(f"✅ Found {len(results)} stocks")
    for stock in results[:10]:
        print(stock)
