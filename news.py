import feedparser
from config import STOCKS


def fetch_headlines(stock: str, limit: int = 4):
    query = f"{stock} stock India".replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({"title": entry.title, "link": entry.link})
    return items


def format_stock(stock: str, headlines: list) -> str:
    if not headlines:
        return f"*{stock}*\nNo significant fresh news."

    lines = [f"*{stock}*"]
    for h in headlines:
        lines.append(f"- {h['title']}\n  {h['link']}")
    return "\n".join(lines)


def generate_news_report() -> str:
    sections = []
    for stock in STOCKS:
        headlines = fetch_headlines(stock)
        sections.append(format_stock(stock, headlines))
    note = "\n\n(Ye sirf headlines hain, koi buy/sell advice nahi. Poori khabar link pe padho.)"
    return "\n\n".join(sections) + note


def run():
    from ath_alert import check_ath_alerts
    from telegram_utils import send_message
    report = generate_news_report()
    send_message(report)

    ath_alerts = check_ath_alerts(STOCKS)
    for alert in ath_alerts:
        send_message(alert)

if __name__ == "__main__":
    run()
