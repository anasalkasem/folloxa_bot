import os
from dotenv import load_dotenv

# تحميل القيم من ملف .env (للتطوير المحلي فقط)
# على Railway، المتغيرات ستكون متاحة مباشرة من النظام
load_dotenv()

class Settings:
    def __init__(self):
        # توكن البوت من تلغرام
        self.bot_token: str = os.getenv("BOT_TOKEN")
        # مفتاح OpenAI API
        self.openai_api_key: str = os.getenv("OPENAI_API_KEY")
        # رابط الموقع
        self.site_url: str = os.getenv("SITE_URL", "https://folloxa.com")
        # رقم الواتساب للتواصل
        self.contact_whatsapp: str = os.getenv("CONTACT_WHATSAPP", "0017163036301")
        # معرف التلغرام للتواصل
        self.contact_telegram: str = os.getenv("CONTACT_TELEGRAM", "folloxa_admin")

        # تحقق إذا القيم انقرأت بشكل صحيح
        if not self.bot_token:
            raise ValueError("❌ BOT_TOKEN غير موجود في متغيرات البيئة. تأكد من إعداده في Railway.")

        if not self.openai_api_key:
            raise ValueError("❌ OPENAI_API_KEY غير موجود في متغيرات البيئة. تأكد من إعداده في Railway.")

# كائن واحد جاهز للاستخدام
settings = Settings()