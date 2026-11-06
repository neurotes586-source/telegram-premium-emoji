# telegram-premium-emoji

Agent skill + data packs for **Telegram Premium custom emoji** in bots: `<tg-emoji>` in message text and
`icon_custom_emoji_id` on inline / reply keyboard buttons (Bot API 7.0+). The bot itself does **not**
need Telegram Premium, and users whose clients cannot draw a custom emoji see the plain fallback emoji -
so every icon here ships with one.

| Path | What it is | Entries |
|---|---|---|
| `SKILL.md` | the skill: rules, catalog, examples, pitfalls, verification | - |
| `references/manual-icons.json` | curated core UI icons (part 1) | 49 |
| `references/manual-icons-part2.json` | curated extended set: navigation, search, status, finance, media | 53 |
| `references/packs-dump.json` | flat dump of 6 public packs | 1923 |
| `scripts/validate_emoji_ids.py` | read-only liveness check via `getCustomEmojiStickers` | - |

## Install as an agent skill

Clone into wherever your harness loads `SKILL.md` from, e.g. for Claude Code:

```bash
git clone https://github.com/neurotes586-source/telegram-premium-emoji.git \
  ~/.claude/skills/telegram-premium-emoji
```

For other agents: copy the folder and point the loader at `SKILL.md`.

## Quick start (aiogram 3)

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Подписаться",
        url=CHANNEL_LINK,
        icon_custom_emoji_id="6039422865189638057",
    )],
    [InlineKeyboardButton(
        text="Проверить подписку",
        callback_data="check_subscribe",
        icon_custom_emoji_id="5870633910337015697",
    )],
])
```

In message text use HTML mode with a mandatory fallback:

```python
await msg.answer('<tg-emoji emoji-id="5870633910337015697">\u2705</tg-emoji> Готово',
                 parse_mode='HTML')
```

Full rules, more examples and pitfalls: [`SKILL.md`](SKILL.md).

## Validate before shipping

```bash
python3 scripts/validate_emoji_ids.py --token $BOT_TOKEN references/manual-icons.json
```

Read-only (`getCustomEmojiStickers`), chunks of 200 IDs, `--drop-dead clean.json` writes a copy without
dead IDs. Emoji can be revoked by their owners, so re-run it before releases.

## Extending the catalog

1. Resolve a pack: `getStickerSet(name)` for `https://t.me/addemoji/<name>` - stickers carry `custom_emoji_id`.
2. Append entries with fields `name`, `emoji`, `custom_emoji_id`, `pack`, `category`; dedupe by ID.
3. Validate the batch (see above). Live search: [ehub.tg](https://ehub.tg) (15 000+ emoji, 217 packs, HTTP API + MCP).

## Sources & credits

- [abbosahmad/telegram-premium-emojis](https://github.com/abbosahmad/telegram-premium-emojis) - packs behind `packs-dump.json`
  (TgAndroidIcons, tgmacicons, vector_icons_by_fStikBot, NewsEmoji, RoboEmoji, RestrictedEmoji).
- [Zulut30/premium-telegram-emoji](https://github.com/Zulut30/premium-telegram-emoji) - community pack dumps, source of `tgiosicons.json`.
- [TGlimmer/tg-emoji-hub](https://github.com/TGlimmer/tg-emoji-hub) / [ehub.tg](https://ehub.tg) - live emoji search.
- Core curated lists - collected for production bot UI.

## Notes

- Not affiliated with Telegram.
- Catalog names are in Russian (the lists were assembled for Russian-language bot UIs); the `emoji` fallback
  field is what matters for grep-by-emoji workflows.
- Licenses of the source repos were not checked; emoji IDs are factual identifiers from public packs.

## License

MIT
