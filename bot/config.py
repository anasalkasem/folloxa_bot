import os
from openai import OpenAI

class Settings:
    def __init__(self):
        # قراءة متغيرات البيئة بشكل آمن
        self.bot_token = os.getenv('BOT_TOKEN')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        
        # التحقق من وجود المتغيرات المطلوبة
        if not self.bot_token:
            raise ValueError("❌ BOT_TOKEN is required! Please set it in Railway Variables.")
        
        if not self.openai_api_key:
            raise ValueError("❌ OPENAI_API_KEY is required! Please set it in Railway Variables.")
        
        # طباعة للتشخيص (بدون كشف المفاتيح)
        print(f"🔍 BOT_TOKEN found: {bool(self.bot_token)}")
        print(f"🔍 OPENAI_API_KEY found: {bool(self.openai_api_key)}")
        print(f"🔑 BOT_TOKEN starts with: {self.bot_token[:10]}...")
        print(f"🔑 OPENAI_API_KEY starts with: {self.openai_api_key[:10]}...")
        
        # إعدادات أخرى
        self.site_url = os.getenv('SITE_URL', 'https://folloxa.com' )
        self.contact_whatsapp = os.getenv('CONTACT_WHATSAPP', '0017163036301')
        self.contact_telegram = os.getenv('CONTACT_TELEGRAM', 'folloxa_admin')
        
        # إعداد OpenAI بشكل آمن
        try:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
            
            # اختبار الاتصال
            models = self.openai_client.models.list()
            print(f"✅ OpenAI client initialized successfully - {len(models.data)} models available")
            
        except Exception as e:
            print(f"❌ Failed to initialize OpenAI client: {str(e)}")
            raise ValueError(f"OpenAI initialization failed: {str(e)}")

# إنشاء كائن الإعدادات
settings = Settings()
