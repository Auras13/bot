
# Telegram Trading Bot

Trimite semnale de tranzacționare în Telegram pe baza webhook-urilor.

## Variabile de mediu:
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
- PORT (default 5000)

## Pornire locală:
```
pip install -r requirements.txt
python main.py
```

## Webhook payload exemplu (pentru TradingView):
```
{
  "symbol": "EUR/USD",
  "side": "BUY",
  "price": "1.1762",
  "rsi": "29.8",
  "macd": "bullish crossover",
  "trend": "Above MA50",
  "tp": "1.1850",
  "sl": "1.1690",
  "timestamp": "2025-07-14 22:00 GMT"
}
```
