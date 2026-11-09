"""Проверяет лимиты Bot API для html виджета: ≤32768 байт UTF-8 и ≤4096 байт после zlib(9)."""
import sys
import zlib
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("winter_cup.html"))
raw = path.read_bytes()
packed = len(zlib.compress(raw, 9))
print(f"{path.name}: raw={len(raw)} B (limit 32768), zlib9={packed} B (limit 4096)")
ok = len(raw) <= 32768 and packed <= 4096
print("OK" if ok else "TOO BIG")
sys.exit(0 if ok else 1)
