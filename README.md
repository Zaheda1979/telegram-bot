# Telegram Daily Bot (Motivation + Stock News) — Railway Deploy

## Files
- `config.py` — Stock list yahan hai (`STOCKS = [...]`), timings bhi.
- `motivation.py` — 9:00 AM IST daily motivation message.
- `news.py` — 11:00 AM IST daily stock news (positive/negative split, no buy/sell advice).
- `main.py` — Scheduler, ye hi Railway pe chalega.
- `test_message.py` — Ek test message bhejne ke liye.

## Steps

1. **GitHub pe upload karo**
   - Ek naya repo banao, ye saari files usme daalo.

2. **Railway pe deploy karo**
   - railway.app pe login karo → New Project → Deploy from GitHub repo → apna repo select karo.

3. **Environment Variables set karo** (Railway dashboard → Variables tab)
   - `TELEGRAM_BOT_TOKEN` — BotFather se mila token
   - `TELEGRAM_CHAT_ID` — apna chat ID
   - `ANTHROPIC_API_KEY` — apni Anthropic API key ([console.anthropic.com](https://console.anthropic.com) se banao)

4. **Test karo**
   - Railway dashboard mein terminal/shell se: `python test_message.py`
   - Telegram check karo, message aana chahiye.

5. **Deploy start karo**
   - Railway automatically `Procfile` follow karega aur `main.py` worker start ho jayega.
   - Ye process hamesha chalta rahega aur roz 9 AM + 11 AM IST pe message bhejega.

## Stocks change karna
`config.py` mein `STOCKS` list edit karo, save karo, Railway pe redeploy ho jayega automatically (agar GitHub se connected hai).

## Security
- Token kabhi bhi code mein hardcode mat karo, sirf Environment Variables mein rakho.
- Token leak ho jaye to BotFather pe `/revoke` karke naya token lo, aur Railway variable update karo.
