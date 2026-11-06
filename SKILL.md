---
name: telegram-premium-emoji
description: Use when building or editing Telegram bot UI that needs premium custom emoji instead of ordinary emoji - message text, inline buttons, reply keyboards, menus, status lines, broadcast copy. Covers the `<tg-emoji>` HTML tag and the `icon_custom_emoji_id` field, with a curated catalog of 102 ready-to-use premium emoji IDs, a 1923-entry dump of public packs and the iOS icon set in references/, plus a liveness validator in scripts/. Trigger on premium emoji, custom emoji, tg-emoji, icon_custom_emoji_id, премиум эмодзи, эмодзи в кнопках бота.
---

# Telegram Premium Emoji in Bots

Premium custom emoji let a bot render polished, branded icons in messages and buttons. The bot itself
does not need Telegram Premium - any bot can send them. A user whose client cannot render a custom
emoji sees the fallback unicode character in message text, so never let the icon carry meaning alone:
keep the label readable with the icon removed.

## Requirements

- **Bot API 6.2+** for `<tg-emoji>` inside message text (custom emoji entities).
- **Bot API 7.0+** for `icon_custom_emoji_id` on `InlineKeyboardButton` / `KeyboardButton`. Use a
  library version that exposes those fields (recent aiogram 3.x); older libraries silently drop them.
- **HTML parse mode** on every send/edit call that uses `<tg-emoji>` (`parse_mode=ParseMode.HTML` for
  aiogram). Without it the tag is rendered as literal text.
- **Fallback character always present** between the tags - it is what non-supporting clients show.

## Quick reference

Three places premium emoji can appear:

1. **Inside message text** -> `<tg-emoji emoji-id="ID">fallback</tg-emoji>` with `parse_mode=HTML`
2. **Inline keyboard buttons** -> `icon_custom_emoji_id="ID"` field on `InlineKeyboardButton`
3. **Reply keyboard buttons** -> `icon_custom_emoji_id` field on `KeyboardButton`

## Premium emoji catalog

Format: `fallback - name - emoji_id`. Machine-readable versions with `pack` / `category` fields live in
`references/manual-icons.json` (core) and `references/manual-icons-part2.json` (extended).

### Core UI icons (49)

```
⚙️ Настройки                  5870982283724328568
👤  Профиль                    5870994129244131212
👥  Люди                       5870772616305839506
👤  Человек+галочка            5891207662678317861
👤  Человек+крестик            5893192487324880883
📁  Файл                       5870528606328852614
🙂  Смайл улыбка               5870764288364252592
📊  Рост (график вверх)        5870930636742595124
📊  Статистика график          5870921681735781843
🏘  Дом                        5873147866364514353
🔒  Замок закрытый             6037249452824072506
🔓  Замок открытый             6037496202990194718
📣  Рупор                      6039422865189638057
✅  Галочка                    5870633910337015697
❌  Крестик                    5870657884844462243
🖋  Карандаш                   5870676941614354370
🗑  Мусорный бак               5870875489362513438
⬇️ Вниз                       5893057118545646106
📎  Скрепка                    6039451237743595514
🔗  Ссылка                     5769289093221454192
i  Инфо                       6028435952299413210
🤖  Бот                        6030400221232501136
👁  Глаз                       6037397706505195857
👁  Скрыто                     6037243349675544634
⬆️ Отправить                  5963103826075456248
⬇️ Скачать                    6039802767931871481
🔔  Уведомление                6039486778597970865
🎁  Подарок                    6032644646587338669
⏰  Часы                       5983150113483134607
🎉  Ура                        6041731551845159060
🔗  Шрифт                      5870801517140775623
✍️ Писать                     5870753782874246579
🖼  Медиа/фото                 6035128606563241721
📍  Геометка                   6042011682497106307
👛  Кошелек                    5769126056262898415
📦  Коробка                    5884479287171485878
👾  Криптобот                  5260752406890711732
📅  Календарь                  5890937706803894250
🏷  Бирка                      5886285355279193209
🕓  Время прошло               5775896410780079073
📦  Приложения                 5778672437122045013
🖌  Кисточка                   6050679691004612757
🔡  Добавить текст             5771851822897566479
↔️ Разрешение/формат          5778479949572738874
🪙  Деньги                     5904462880941545555
🪙  Отправить деньги           5890848474563352982
🏧  Принять деньги             5879814368572478751
🔨  Код </>                    5940433880585605708
🔄  Загрузка                   5345906554510012647
```

### Extended set (53)

```
⬅️ Назад                      5877536313623711363
➡️ Вперёд                     5877468380125990242
⬆️ Вверх                      6005807101056651268
⬇️ Вниз                       5886451926995833684
🔍  Поиск                      5258274739041883702
⭐️ Звезда, рейтинг            5874948844935974490
👑  Корона, VIP                5807868868886009920
⚡️ Молния, скорость           5843553939672274145
🔥  Огонь, популярное          6008118472066732010
⚠️ Предупреждение             5881702736843511327
⛔  Запрет, блокировка         5339233635620899144
❓  Вопрос, поддержка          5873121512445187130
❤️ Сердце                     5992453811510186287
❤️‍🔥Сердце в огне              5449394813709327952
💯  Сто, топ                   5222241728659988366
👀  Наблюдение                 5260341314095947411
🫡  Приветствие, в строй       5323772371830588991
💎  Алмаз, токены              5807465992363710697
🛒  Корзина, магазин           5258024802010026053
💳  Банковская карта           5967548335542767952
📉  График вниз                5246762912428603768
💵  Доллар                     5409048419211682843
💸  Евро                       5233326571099534068
💸  Рубль                      5231449120635370684
🛍  Процент                    5229064374403998351
▶️ Воспроизвести              5264919878082509254
⏸  Пауза                      5359543311897998264
🎵  Музыка                     5891249688933305846
📷  Камера                     5778335621491723621
💬  Чат                        5793933761594789855
✉️ Письмо                     5985817223749439505
🔕  Звук выключен              5909123362839335003
💡  Идея                       5258216851472654189
🔑  Ключ, доступ               6005570495603282482
📌  Булавка, закрепить         5397782960512444700
🛡  Щит, защита                5926783847453692661
💾  Сохранить                  5884448719889240368
🗒  Заметка                    5877597667231534929
🔄  Обновить                   5258420634785947640
➕  Добавить                   5775937998948404844
➖  Убрать                     5229113891081956317
🛠  Инструменты                5988023995125993550
🧠  Мозг, AI                   5314413943035278948
🚀  Запуск                     5445284980978621387
🌍  Глобус, язык               5399898266265475100
⏳  Ожидание                   5451732530048802485
🎯  Цель                       5350460637182993292
🤝  Рукопожатие                5357080225463149588
🖥  Экран, ПК                  5282843764451195532
📱  Телефон                    5985833664884250583
🎨  Палитра, тема              5814690801665446789
🧪  Эксперимент                5897607722295103204
🚩  Флаг                       5454310635707853545
```

## Examples

### 1. Premium emoji in message text (aiogram 3)

```python
from aiogram.enums import ParseMode

await callback.message.edit_text(
    '<b><tg-emoji emoji-id="6039422865189638057">📣</tg-emoji> '
    'Отправь сообщение, которое хотите разослать всем пользователям.</b>',
    parse_mode=ParseMode.HTML,
    reply_markup=get_broadcast_keyboard()
)
```

Rules: HTML mode is mandatory; the fallback emoji must be present; the tag nests inside `<b>`, `<i>`,
`<a>`, `<code>`.

### 2. Inline keyboard with premium icons

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Подписаться",
        url=CHANNEL_LINK,
        icon_custom_emoji_id="6039422865189638057"
    )],
    [InlineKeyboardButton(
        text="Проверить подписку",
        callback_data="check_subscribe",
        icon_custom_emoji_id="5870633910337015697"
    )],
])
```

Do not put a plain unicode emoji inside `text=` when using `icon_custom_emoji_id` - the label renders
twice as decorated text plus icon. Keep the label clean; the icon draws separately to its left.

### 3. Reply keyboard with premium icons (raw Bot API)

```python
keyboard = {
    "keyboard": [
        [{"text": "⚙️ Настройки", "icon_custom_emoji_id": "5870982283724328568"}],
        [{"text": "📅 История",  "icon_custom_emoji_id": "5890937706803894250"}],
    ],
    "resize_keyboard": True,
}
```

## Catalog resources

- `references/manual-icons.json` — core curated list (49 entries: `name`, `emoji`, `custom_emoji_id`).
- `references/manual-icons-part2.json` — extended curated set (53 entries, adds `pack` and `category`).
- `references/packs-dump.json` — flat dump of 1923 emoji from 6 public packs (TgAndroidIcons, tgmacicons, vector_icons_by_fStikBot, NewsEmoji, RoboEmoji, official animated RestrictedEmoji): `id`, `emoji`, `pack`, `category`, `html_tag`.
- `scripts/validate_emoji_ids.py` — read-only liveness check for any ID list (see Verification).

When an icon is missing from the curated lists, grep `references/packs-dump.json` for the fallback emoji
and pick the first hit that fits the semantics; prefer the curated lists when both have a match.

## Extending the catalog

1. Take a pack link `https://t.me/addemoji/<name>` and resolve it with `getStickerSet(name)` - every
   sticker carries `custom_emoji_id`.
2. Merge new entries with the same fields (`name`, `emoji`, `custom_emoji_id`, `pack`, `category`),
   deduplicate by ID.
3. Validate the batch with `scripts/validate_emoji_ids.py` before committing (see Verification).
4. Live search over 15 000+ emoji / 217 packs: [ehub.tg](https://ehub.tg) - web UI, HTTP API and MCP server.

## Finding more emoji IDs

1. Send the desired premium emoji from a Premium account into any chat.
2. Read `MessageEntity.custom_emoji_id` - forward the message to a helper bot, or use a userbot
   (`MessageEntity.custom_emoji_id` on the incoming message).
3. Validate the ID before shipping (see Verification).

## Pitfalls

- **Forgot `parse_mode=HTML`** -> `<tg-emoji>` shows up as literal text.
- **Empty or missing fallback** -> nothing renders for clients that cannot draw the custom emoji.
- **Unicode emoji inside button `text=` plus `icon_custom_emoji_id`** -> doubled icon.
- **Library without Bot API 7.0 fields** -> `icon_custom_emoji_id` is dropped without an error; the
  button just has no icon.
- **Invented IDs** -> the message send fails or the emoji resolves to nothing. Use IDs from this
  catalog or from a `getCustomEmojiStickers` check.
- **IDs lifted from random channels** -> custom emoji can be revoked or renamed; re-validate after
  copy-paste from third parties.

## Verification

1. `getCustomEmojiStickers(custom_emoji_ids=[...])` (Bot API 6.2+, up to 200 ids per call, read-only,
   sends nothing) - returns the stickers that exist; ids missing from the response are invalid.
   `scripts/validate_emoji_ids.py` wraps it in a batch mode:

   ```bash
   python3 scripts/validate_emoji_ids.py --token $BOT_TOKEN references/manual-icons.json references/manual-icons-part2.json
   ```

2. Send the message/keyboard and confirm rendering with a **Premium** account and a **non-Premium**
   account.
3. Confirm the fallback character reads correctly on the non-Premium client.
4. Grep the bot source for `tg-emoji` and assert every send/edit path passes HTML parse mode.

Anything not used by a Premium account can also be checked per-set via `getStickerSet`.

## Sources

- [abbosahmad/telegram-premium-emojis](https://github.com/abbosahmad/telegram-premium-emojis) - source
  of the `packs-dump.json` pack collection.
- [Zulut30/premium-telegram-emoji](https://github.com/Zulut30/premium-telegram-emoji) - community pack
  dumps (source of `tgiosicons.json`).
- [TGlimmer/tg-emoji-hub](https://github.com/TGlimmer/tg-emoji-hub) / [ehub.tg](https://ehub.tg) - live
  emoji search.

## License

MIT - see [LICENSE](LICENSE). Emoji IDs belong to their packs' owners and may be revoked by them.
