from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .config import settings

def contact_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💬 WhatsApp", 
                url=f"https://wa.me/{settings.contact_whatsapp}"
             )
        ],
        [
            InlineKeyboardButton(
                text="📱 Telegram", 
                url=f"https://t.me/{settings.contact_telegram}"
             )
        ],
        [
            InlineKeyboardButton(
                text="🌐 Visit website", 
                url=settings.site_url
            )
        ]
    ])
    return keyboard
