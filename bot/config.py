import os
from openai import OpenAI

class Settings:
    def __init__(self):
        # قراءة متغيرات البيئة بطرق متعددة
        self.bot_token = (
            os.getenv('BOT_TOKEN') or 
            os.getenv('bot_token') or 
            "8213247929:AAEe8Bpkfri3l9H4kG-NwP9sEb_JyXBGw_k"
        )
        
        self.openai_api_key = (
            os.getenv('OPENAI_API_KEY') or 
            os.getenv('openai_api_key') or 
            "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"
        )
        
        # طباعة للتشخيص
        print(f"🔍 BOT_TOKEN found: {bool(self.bot_token)}")
        print(f"🔍 OPENAI_API_KEY found: {bool(self.openai_api_key)}")
        
        # إعدادات أخرى
        self.site_url = os.getenv('SITE_URL', 'https://folloxa.com' )
        self.contact_whatsapp = os.getenv('CONTACT_WHATSAPP', '0017163036301')
        self.contact_telegram = os.getenv('CONTACT_TELEGRAM', 'folloxa_admin')
        
        # إعداد OpenAI
        try:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
            print("✅ OpenAI client initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize OpenAI client: {str(e)}")
            self.openai_client = None

# إنشاء كائن الإعدادات
settings = Settings()
