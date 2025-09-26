import os
from openai import OpenAI

class Settings:
    def __init__(self):
        # قراءة متغيرات البيئة بطرق متعددة
        self.bot_token = (os.getenv('BOT_TOKEN') or 
                         os.getenv('bot_token') or 
                         "8213247929:AAEe8Bpkfri3l9H4kG-NwP9sEb_JyXBGw_k")
        
        self.openai_api_key = (os.getenv('OPENAI_API_KEY') or 
                              os.getenv('openai_api_key') or 
                              "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")
        
        print(f"🔍 BOT_TOKEN found: {bool(self.bot_token)}")
        print(f"🔍 OPENAI_API_KEY found: {bool(self.openai_api_key)}")
        
        # إعدادات أخرى
        self.site_url = os.getenv('SITE_URL', 'https://folloxa.com' )
        self.contact_whatsapp = os.getenv('CONTACT_WHATSAPP', '0017163036301')
        self.contact_telegram = os.getenv('CONTACT_TELEGRAM', 'folloxa_admin')
        
        # إعداد OpenAI
        self.openai_client = OpenAI(api_key=self.openai_api_key)

settings = Settings()
