import asyncio
from aiogram import Bot, Dispatcher
from .config import settings
from .handlers import router

# استدعاء التوكن من ملف config
BOT_TOKEN = settings.bot_token

# إنشاء البوت والديسباتشر
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# تسجيل الـ handlers
dp.include_router(router)

# تشغيل البوت
async def main():
    print("🚀 Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())