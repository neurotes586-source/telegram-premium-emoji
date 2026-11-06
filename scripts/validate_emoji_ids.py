#!/usr/bin/env python3
"""Проверка живости custom_emoji_id через getCustomEmojiStickers (Bot API 6.2+, read-only, ничего не отправляет).

Использование:
    python3 validate_emoji_ids.py --token 123456:ABC-DEF references/manual-icons.json
    python3 validate_emoji_ids.py --token TOKEN catalog1.json catalog2.json
    python3 validate_emoji_ids.py --token TOKEN packs-dump.json --drop-dead clean.json

Принимает json-файлы двух форматов:
  [{"name":..., "emoji":..., "custom_emoji_id"|"id":...}, ...]
  {"ИмяПака": {"emojis": [{"id": ...}, ...], ...}}
Бьёт на чанки по 200 (лимит метода), печатает живые/мёртвые, по ключу --drop-dead
пишет копию без мёртвых id (исходник не трогает).
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

API = "https://api.telegram.org/bot{token}/getCustomEmojiStickers"


def collect(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        if "custom_emoji_id" in data or "id" in data:
            data = [data]
        else:
            flat = []
            for v in data.values():
                if isinstance(v, dict) and "emojis" in v:
                    flat += v["emojis"]
                elif isinstance(v, list):
                    flat += v
            data = flat
    ids, meta = [], {}
    for e in data:
        cid = str(e.get("custom_emoji_id") or e.get("id") or "")
        if cid.isdigit():
            ids.append(cid)
            meta[cid] = e
    return ids, meta


def alive(token, ids):
    ok = set()
    for i in range(0, len(ids), 200):
        chunk = ids[i:i + 200]
        body = urllib.parse.urlencode({"custom_emoji_ids": json.dumps(chunk)}).encode()
        req = urllib.request.Request(API.format(token=token), data=body)
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.load(r)
        if not res.get("ok"):
            sys.exit(f"API вернул ошибку: {res}")
        ok |= {s["custom_emoji_id"] for s in res.get("result", [])}
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", required=True, help="токен любого бота, Premium не нужен")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--drop-dead", metavar="OUT", help="записать объединённый json без мёртвых id")
    a = ap.parse_args()

    all_ids, all_meta, per_file = [], {}, {}
    for f in a.files:
        ids, meta = collect(f)
        per_file[f] = ids
        all_meta.update(meta)
        all_ids += ids
    print(f"всего id: {len(all_ids)}")

    ok = alive(a.token, all_ids)
    dead = [i for i in all_ids if i not in ok]
    print(f"живых: {len(ok)}, мёртвых: {len(dead)}")
    for i in dead:
        m = all_meta.get(i, {})
        print(f"  ✗ {i}  {m.get('emoji','')} {m.get('name', m.get('pack',''))}")

    if a.drop_dead:
        clean = [all_meta[i] for i in all_ids if i in ok]
        json.dump(clean, open(a.drop_dead, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"чистый каталог ({len(clean)} записей) -> {a.drop_dead}")


if __name__ == "__main__":
    main()
