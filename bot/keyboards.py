from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .config import settings

def contact_kb() -> InlineKeyboardMarkup:
    wa_url = f"https://wa.me/{settings.contact_whatsapp}"
    tg_url = f"https://t.me/{settings.contact_telegram}"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 WhatsApp", url=wa_url)],
        [InlineKeyboardButton(text="📨 Telegram", url=tg_url)],
        [InlineKeyboardButton(text="🌐 Visit website", url=settings.site_url)],
    ])
