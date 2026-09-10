import feedparser
from html import escape
from config import STOCKS


def fetch_headlines(stock: str, limit: int = 3):
    query = f"{stock} stock India".replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({"title": entry.title, "link": entry.link})
    return items


def format_stock(stock: str, headlines: list) -> str:
    if not headlines:
        return f"<b>{escape(stock)}</b>\nNo significant fresh news."

    lines = [f"<b>{escape(stock)}</b>"]
    for h in headlines:
        title = escape(h["title"])
        link = escape(h["link"], quote=True)
        lines.append(f'• {title} — <a href="{link}">Read more</a>')
    return "\n".join(lines)


def generate_news_report() -> str:
    sections = []
    for stock in STOCKS:
        try:
            headlines = fetch_headlines(stock)
        except Exception:
            headlines = []
        sections.append(format_stock(stock, headlines))
    note = "\n\n(Ye sirf headlines hain, koi buy/sell advice nahi.)"
    return "\n\n".join(sections) + note


def run():
    from telegram_utils import send_message

    try:
        report = generate_news_report()
        send_message(report)
    except Exception as e:
        send_message(f"News report failed: {e}")

    try:
        from ath_alert import check_ath_alerts
        ath_alerts = check_ath_alerts(STOCKS)
        for alert in ath_alerts:
            send_message(alert)
    except Exception as e:
        send_message(f"ATH alert failed: {e}")


if __name__ == "__main__":
    run()
