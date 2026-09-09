import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

MAX_LEN = 3900


def _send_one(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "disable_web_page_preview": False,
    }
    resp = requests.post(url, data=payload, timeout=20)
    resp.raise_for_status()
    return resp.json()


def send_message(text: str):
    if not text:
        return None

    chunks = []
    remaining = text

    while len(remaining) > MAX_LEN:
        cut = remaining.rfind("\n", 0, MAX_LEN)
        if cut == -1:
            cut = MAX_LEN
        chunks.append(remaining[:cut])
        remaining = remaining[cut:].lstrip("\n")

    if remaining:
        chunks.append(remaining)

    result = None
    for chunk in chunks:
        result = _send_one(chunk)
    return result
