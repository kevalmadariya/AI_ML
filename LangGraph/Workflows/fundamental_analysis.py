import yfinance as yf

def fundanmental_analysis():
    fundamentals = []
    for s in ['TIRUPATIFL','SPORTKING']:
        stock = yf.Ticker(s)
        info = stock.info

        current_price = info.get('currentPrice') or info.get('regularMarketPrice')
        pb_ratio = info.get('priceToBook')
        debt_to_equity = info.get('debtToEquity')
        eps = info.get('trailingEps')
        roe = info.get('returnOnEquity')

        if debt_to_equity is not None and debt_to_equity > 1:
            debt_to_equity = debt_to_equity / 100

        conditions = {
            # "PE < Industry PE": pe_ratio is not None and industry_pe is not None and pe_ratio < industry_pe,
            "Debt/Equity < 0.5": debt_to_equity is not None and debt_to_equity < 0.5,
            "PB < 10": pb_ratio is not None and pb_ratio < 10,
            "EPS > 0.1×Price": eps is not None and current_price is not None and eps > 0.1 * current_price,
            "ROE > 12%": roe is not None and roe > 0.12
        }

        met = sum(conditions.values())
        signal = True if met >= 3 else False
        fundamentals.append(signal)

    return True