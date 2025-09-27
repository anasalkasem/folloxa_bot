from aiogram import Router, types
from aiogram.filters import Command
from .config import settings
from .keyboards import contact_kb

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    welcome_text = (
        "Welcome to **Folloxa**!\n"
        "Ask me anything about services, pricing tiers, refill, or delivery times.\n"
        "أهلاً بك! اكتب سؤالك وسأجيبك فوراً."
    )
    await message.answer(welcome_text, reply_markup=contact_kb())

@router.message()
async def handle_any_message(message: types.Message):
    user_text = message.text or ""
    
    print(f"📨 Received message: {user_text}")
    print(f"🔑 OpenAI client exists: {settings.openai_client is not None}")
    
    try:
        # استدعاء OpenAI مباشرة
        response = settings.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "أنت بوت دعم لموقع Folloxa (لوحة SMM). رد بنفس لغة المستخدم. اختصر الرد وكن مهنياً."
                },
                {"role": "user", "content": user_text}
            ],
            max_tokens=300,
            temperature=0.4
        )
        
        ai_reply = response.choices[0].message.content.strip()
        print(f"✅ OpenAI replied: {ai_reply[:50]}...")
        
        await message.answer(ai_reply, reply_markup=contact_kb())
        
    except Exception as e:
        print(f"❌ OpenAI Error: {str(e)}")
        print(f"❌ Error type: {type(e).__name__}")
        
        # رد مع تفاصيل الخطأ للتشخيص
        error_msg = f"خطأ OpenAI: {str(e)[:100]}"
        await message.answer(error_msg, reply_markup=contact_kb())
