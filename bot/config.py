import os
from openai import OpenAI

class Settings:
    def __init__(self ):
        # قراءة متغيرات البيئة مع قيم افتراضية للاختبار
        self.bot_token = os.getenv('BOT_TOKEN')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        
        # طباعة للتشخيص
        print(f"🔍 BOT_TOKEN exists: {bool(self.bot_token)}")
        print(f"🔍 OPENAI_API_KEY exists: {bool(self.openai_api_key)}")
        
        # إذا لم توجد المتغيرات، استخدم قيم مؤقتة
        if not self.bot_token:
            print("⚠️ BOT_TOKEN not found, please check Railway variables")
            # ضع توكن البوت الحقيقي هنا مؤقتاً
            self.bot_token ="8213247929:AAEe8Bpkfri3l9H4kG-NwP9sEb_JyXBGw_k"            
        if not self.openai_api_key:
            print("⚠️ OPENAI_API_KEY not found, please check Railway variables")
            # ضع مفتاح OpenAI الحقيقي هنا مؤقتاً
            self.openai_api_key ="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"
        
        # إعدادات أخرى
        self.site_url = os.getenv('SITE_URL', 'https://folloxa.com' )
        self.contact_whatsapp = os.getenv('CONTACT_WHATSAPP', '0017163036301')
        self.contact_telegram = os.getenv('CONTACT_TELEGRAM', 'folloxa_admin')
        
        # إعداد OpenAI
        self.openai_client = OpenAI(api_key=self.openai_api_key)

# إنشاء كائن الإعدادات
settings = Settings()
