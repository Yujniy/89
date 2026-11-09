"""Отправляет виджет Winter Cup через Bot API 10.4 (sendWidget).

Использование:
    BOT_TOKEN=... CHAT_ID=... python send_widget.py

В продакшене виджеты пока доставляются только в личные чаты с ботом,
поэтому CHAT_ID — это user_id участника, а не id канала/группы.
"""
import json
import os
import sys
import urllib.request
import zlib
from pathlib import Path

token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
if not token or not chat_id:
    sys.exit("Нужны переменные окружения BOT_TOKEN и CHAT_ID")

html = Path(__file__).with_name("winter_cup.html").read_text(encoding="utf-8")
raw = html.encode("utf-8")
if len(raw) > 32768 or len(zlib.compress(raw, 9)) > 4096:
    sys.exit("html превышает лимиты виджета (32768 B / 4096 B zlib)")

payload = {
    "chat_id": chat_id,
    "html": html,
    "height": 220,
    "caption": "❄️ <b>Winter Cup</b> — турнир FC Mobile в декабре.\nСвайпни виджет вбок, чтобы узнать больше.",
    "parse_mode": "HTML",
}

req = urllib.request.Request(
    f"https://api.telegram.org/bot{token}/sendWidget",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.load(resp)

print(json.dumps(result, ensure_ascii=False, indent=2))
