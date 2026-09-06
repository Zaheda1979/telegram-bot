import os

# --- Secrets: set these as Environment Variables on Railway, never hardcode ---
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# --- Edit this list anytime to change which stocks get covered ---
STOCKS = ["SBIN", "ITC", "INDIGO", "CIPLA"]

# --- Schedule times (24hr, Asia/Kolkata timezone) ---
MOTIVATION_TIME = {"hour": 9, "minute": 0}
NEWS_TIME = {"hour": 11, "minute": 0}
TIMEZONE = "Asia/Kolkata"
