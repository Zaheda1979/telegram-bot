import yfinance as yf

def check_ath_alerts(stocks):
    """
    Checks each stock for a new All-Time High (ATH) with volume confirmation.
    Returns a list of alert message strings (empty list if none).
    """
    alerts = []

    for symbol in stocks:
        try:
            ticker = yf.Ticker(f"{symbol}.NS")  # .NS = NSE India
            hist = ticker.history(period="5y")

            if hist.empty or len(hist) < 30:
                continue

            current_price = hist["Close"].iloc[-1]
            current_volume = hist["Volume"].iloc[-1]

            # Previous ATH = highest close before today
            previous_ath = hist["High"].iloc[:-1].max()
            avg_volume_20d = hist["Volume"].iloc[-21:-1].mean()

            if current_price > previous_ath:
                pct_change = ((current_price - previous_ath) / previous_ath) * 100
                volume_ratio = current_volume / avg_volume_20d if avg_volume_20d > 0 else 0

                if volume_ratio >= 1.5:
                    volume_note = f"Volume: {current_volume:,.0f} shares ({volume_ratio:.1f}x avg) ✅ Strong breakout"
                else:
                    volume_note = f"Volume: {current_volume:,.0f} shares ({volume_ratio:.1f}x avg) ⚠️ Weak volume, confirm before entry"

                msg = (
                    f"🚀 {symbol} ne naya ALL-TIME HIGH banaya!\n"
                    f"Current price: ₹{current_price:,.2f}\n"
                    f"Previous ATH: ₹{previous_ath:,.2f}\n"
                    f"+{pct_change:.1f}% naya high\n"
                    f"{volume_note}"
                )
                alerts.append(msg)

        except Exception as e:
            print(f"ATH check failed for {symbol}: {e}")

    return alerts
