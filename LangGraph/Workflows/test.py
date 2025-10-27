import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://chartink.com/screener/macd-crossover-bearish-bullish")
        print("Page loaded...............................")
        # await page.wait_for_selector("table")  # wait until table loads
        await page.wait_for_selector("table tr a")  # wait until table loads

        html = await page.content()
        await browser.close()

        # print(html)  # preview part of the rendered HTML
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # print(soup.select("tbody"))
        # print(soup.select("tbody tr")[0])
        rows = soup.select("tbody tr")
        names = []
        code = []
        price = []

        for row in rows:
            temp = row.select("td")
            # print(temp[5].text.strip())
            names.append(temp[1].text.strip())
            code.append(temp[2].text.strip())
            price.append(temp[5].text.strip())
            break
       
asyncio.run(main())




