import yfinance as yf
import pandas as pd

NIFTY50 = [
    "ADANIENT.NS", "ADANIPORTS.NS", "APOLLOHOSP.NS", "ASIANPAINT.NS", "AXISBANK.NS",
    "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BEL.NS", "BHARTIARTL.NS",
    "CIPLA.NS", "COALINDIA.NS", "DRREDDY.NS", "EICHERMOT.NS", "ETERNAL.NS",
    "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS",
    "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS", "INDUSINDBK.NS", "INFY.NS",
    "ITC.NS", "JIOFIN.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS",
    "M&M.NS", "MARUTI.NS", "NESTLEIND.NS", "NTPC.NS", "ONGC.NS",
    "POWERGRID.NS", "RELIANCE.NS", "SBILIFE.NS", "SBIN.NS", "SHRIRAMFIN.NS",
    "SUNPHARMA.NS", "TATACONSUM.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TCS.NS",
    "TECHM.NS", "TITAN.NS", "TRENT.NS", "ULTRACEMCO.NS", "WIPRO.NS",
]

SP500_SAMPLE = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "BRK-B", "AVGO", "JPM",
    "LLY", "V", "UNH", "XOM", "MA", "COST", "HD", "PG", "JNJ", "WMT",
    "ABBV", "NFLX", "CRM", "BAC", "ORCL", "MRK", "CVX", "KO", "AMD", "PEP",
    "ADBE", "TMO", "LIN", "CSCO", "MCD", "ACN", "ABT", "PM", "DHR", "INTU",
    "TXN", "VZ", "IBM", "QCOM", "GE", "CAT", "NOW", "AMGN", "NEE", "DIS",
]


def _breadth(tickers):
    above50 = below50 = above200 = below200 = 0
    data = yf.download(tickers, period="1y", interval="1d",
                       group_by="ticker", auto_adjust=True,
                       progress=False, threads=True)

    for t in tickers:
        try:
            closes = data[t]["Close"].dropna()
            if len(closes) < 200:
                continue
            price = closes.iloc[-1]
            ma50 = closes.tail(50).mean()
            ma200 = closes.tail(200).mean()

            if price > ma50:
                above50 += 1
            else:
                below50 += 1

            if price > ma200:
                above200 += 1
            else:
                below200 += 1
        except Exception:
            continue

    return above50, below50, above200, below200


def _verdict(above50, total):
    if total == 0:
        return "N/A"
    pct = above50 / total * 100
    if pct >= 65:
        return "Bullish"
    if pct <= 35:
        return "Bearish"
    return "Neutral"


def generate_breadth_report() -> str:
    lines = ["WEEKLY MARKET HEALTH", ""]

    try:
        a50, b50, a200, b200 = _breadth(NIFTY50)
        lines.append("NIFTY 50 (India)")
        lines.append(f"50 DMA: {a50} above / {b50} below")
        lines.append(f"200 DMA: {a200} above / {b200} below")
        lines.append(f"Trend: {_verdict(a50, a50 + b50)}")
    except Exception as e:
        lines.append(f"NIFTY 50 data failed: {e}")

    lines.append("")

    try:
        a50, b50, a200, b200 = _breadth(SP500_SAMPLE)
        lines.append("S&P 500 (US, top 50)")
        lines.append(f"50 DMA: {a50} above / {b50} below")
        lines.append(f"200 DMA: {a200} above / {b200} below")
        lines.append(f"Trend: {_verdict(a50, a50 + b50)}")
    except Exception as e:
        lines.append(f"S&P 500 data failed: {e}")

    lines.append("")
    lines.append("(Zyada stocks MA ke upar = market strong, neeche = weak)")
    return "\n".join(lines)


def run():
    from telegram_utils import send_message
    try:
        send_message(generate_breadth_report())
    except Exception as e:
        send_message(f"Market breadth failed: {e}")


if __name__ == "__main__":
    run()
