from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from openai import OpenAI
from .config import settings
from .keyboards import contact_kb

router = Router()

# Initialize OpenAI client once
oa = OpenAI(api_key=settings.openai_api_key)

SYSTEM_PROMPT = (
    "أنت بوت دعم لموقع Folloxa (لوحة SMM). "
    "مهمتك أن ترد دائمًا بنفس لغة الزائر. "
    "إذا كتب بالعربية ترد بالعربية، إذا كتب بالإنجليزية ترد بالإنجليزية، "
    "إذا كتب بالإسبانية ترد بالإسبانية… إلخ. "
    "اختصر الرد وخلّيه واضح ومهني. "
    "إذا كان السؤال خارج نطاق خدمات السوشيال ميديا أو يحتاج موظف، "
    "وجّه المستخدم للتواصل مع الدعم البشري عبر الأزرار."
)

async def ai_reply(user_text: str) -> str:
    try:
        resp = oa.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.4,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return "حدث خطأ مؤقت. تواصل مع الدعم من الأزرار أعلاه."

@router.message(Command("start"))
async def cmd_start(msg: Message):
    text = (
        "Welcome to **Folloxa**!\n"
        "Ask me anything about services, pricing tiers, refill, or delivery times.\n"
        "أهلاً بك! اكتب سؤالك وسأجيبك فوراً."
    )
    await msg.answer(text, reply_markup=contact_kb())

@router.message(Command("help"))
async def cmd_help(msg: Message):
    text = (
        "Send your question about our SMM services and I'll reply in your language.\n"
        "للتواصل مع فريق الدعم مباشرة استخدم الأزرار أدناه."
    )
    await msg.answer(text, reply_markup=contact_kb())

@router.message(F.text)
async def on_text(msg: Message):
    reply = await ai_reply(msg.text or "")
    await msg.answer(reply, reply_markup=contact_kb())
