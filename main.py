
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    message = f'''
📊 {data.get("symbol", "Instrument")} Signal

🔹 Type: {data.get("side", "N/A")}
🔹 Price: {data.get("price", "N/A")}
🔹 RSI: {data.get("rsi", "N/A")}
🔹 MACD: {data.get("macd", "N/A")}
🔹 Trend: {data.get("trend", "N/A")}

🎯 TP: {data.get("tp", "N/A")}
🛑 SL: {data.get("sl", "N/A")}

🕒 {data.get("timestamp", "")}
'''

    send_message(message)
    return {"status": "ok"}, 200

def send_message(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    pass
    
