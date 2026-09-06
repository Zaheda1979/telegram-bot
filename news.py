import feedparser
from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, STOCKS

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def fetch_headlines(stock: str, limit: int = 5):
    query = f"{stock} stock India".replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({"title": entry.title, "link": entry.link})
    return items


def summarize_stock(stock: str, headlines: list) -> str:
    if not headlines:
        return f"{stock}: No significant fresh news."

    headline_text = "\n".join(f"- {h['title']} ({h['link']})" for h in headlines)
    prompt = f"""Yeh raw headlines hain {stock} stock ke baare mein:

{headline_text}

Simple English mein summarize karo. Positive aur negative news alag-alag section mein dikhao.
Har news ke saath likely impact bhi batao (1 line). Source link zaroor include karo.
Agar kuch important nahi mila to likho: 'No significant fresh news'.
Buy ya sell advice bilkul mat do, sirf news summary do.
Sirf summary likho, koi extra intro nahi."""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    return f"*{stock}*\n{response.content[0].text.strip()}"


def generate_news_report() -> str:
    sections = []
    for stock in STOCKS:
        headlines = fetch_headlines(stock)
        sections.append(summarize_stock(stock, headlines))
    return "\n\n".join(sections)


def run():
    from telegram_utils import send_message
    report = generate_news_report()
    send_message(report)


if __name__ == "__main__":
    run()
