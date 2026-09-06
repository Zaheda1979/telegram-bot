# Telegram Daily Bot (Motivation + Stock News) — FREE Version, No API Key Needed

## Files
- `config.py` — Stock list yahan hai (`STOCKS = [...]`), timings bhi.
- `motivation.py` — 9:00 AM IST daily motivation message (fixed rotating messages, no AI).
- `news.py` — 11:00 AM IST daily stock news headlines + links (raw, no AI summary).
- `main.py` — Scheduler, ye hi Railway pe chalega.
- `test_message.py` — Ek test message bhejne ke liye.

## Steps

1. **GitHub pe upload karo** — done already.
2. **Railway pe deploy karo** — done already.
3. **Environment Variables set karo** (Railway dashboard → Variables tab)
   - `TELEGRAM_BOT_TOKEN` — BotFather se mila token
   - `TELEGRAM_CHAT_ID` — apna chat ID
   - (ANTHROPIC_API_KEY ki zaroorat nahi is free version mein)
4. **Test karo**
   - Railway dashboard mein terminal/shell se: `python test_message.py`
5. **Deploy start karo**
   - Railway automatically `Procfile` follow karega aur `main.py` worker start ho jayega.

## Stocks change karna
`config.py` mein `STOCKS` list edit karo.

## Motivation messages change karna
`motivation.py` mein `MESSAGES` list mein naye messages add/edit kar sakte ho.
