# Folloxa – Multilingual Telegram Support Bot

This bot auto-detects the user's language and replies in the same language using OpenAI.
Built with **aiogram v3**.

## Features
- Replies in the **same language** of the user (Arabic, English, Spanish, etc.).
- Quick contact buttons (WhatsApp / Telegram).
- Short, professional responses; gracefully hands off to human support if needed.
- Simple `.env` configuration.

## Quick Start

1) **Create a bot** with @BotFather and get the `BOT_TOKEN`.
2) **Get an OpenAI API key**.
3) **Rename** `.env.example` to `.env` and fill your values:

```
BOT_TOKEN=123456:abc...
OPENAI_API_KEY=sk-...
SITE_URL=https://folloxa.com
CONTACT_WHATSAPP=0017163036301
CONTACT_TELEGRAM=folloxa_admin
```

4) Create a Python virtual environment and install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

5) Run the bot:

```bash
python -m bot.main
```

> Tip: If your server blocks long polling, consider setting a webhook. For most setups, long polling is fine.

## Commands
- `/start` – greet the user & show contact buttons
- `/help` – how to use the bot
- Just **send any question**; the bot will auto-reply in the same language.

## Files
- `bot/main.py` – entry point
- `bot/config.py` – loads environment variables
- `bot/keyboards.py` – inline keyboards (contact buttons)
- `bot/handlers.py` – commands & AI replies
- `requirements.txt` – pinned deps
- `.env.example` – configuration template

