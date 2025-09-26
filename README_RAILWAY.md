# Folloxa Bot - Railway Deployment Ready

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Aiogram](https://img.shields.io/badge/Aiogram-3.4.1-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)
![Railway](https://img.shields.io/badge/Deploy-Railway-purple.svg)

**بوت تلغرام ذكي متعدد اللغات - جاهز للنشر على Railway**

</div>

## 🚀 النشر السريع على Railway

### الطريقة الأولى: النشر المباشر

1. **Fork هذا المستودع** إلى حسابك على GitHub
2. اذهب إلى [Railway.app](https://railway.app)
3. اضغط **"New Project"** → **"Deploy from GitHub repo"**
4. اختر مستودع **folloxa-bot**
5. أضف متغيرات البيئة (انظر أدناه)
6. اضغط **"Deploy"**

### الطريقة الثانية: استخدام Railway CLI

```bash
# تثبيت Railway CLI
npm install -g @railway/cli

# تسجيل الدخول
railway login

# نشر المشروع
railway up
```

## ⚙️ متغيرات البيئة المطلوبة

في لوحة تحكم Railway، أضف المتغيرات التالية:

| المتغير | القيمة | مطلوب |
|---------|--------|--------|
| `BOT_TOKEN` | توكن البوت من @BotFather | ✅ |
| `OPENAI_API_KEY` | مفتاح OpenAI API | ✅ |
| `SITE_URL` | `https://folloxa.com` | ❌ |
| `CONTACT_WHATSAPP` | `0017163036301` | ❌ |
| `CONTACT_TELEGRAM` | `folloxa_admin` | ❌ |

### كيفية الحصول على المفاتيح:

1. **BOT_TOKEN**: 
   - أرسل `/newbot` إلى [@BotFather](https://t.me/BotFather)
   - اتبع التعليمات واحصل على التوكن

2. **OPENAI_API_KEY**:
   - اذهب إلى [OpenAI Platform](https://platform.openai.com/api-keys)
   - أنشئ مفتاح API جديد

## 📁 ملفات التكوين المضافة

هذا المشروع جاهز للنشر على Railway مع الملفات التالية:

- ✅ `Procfile` - أمر التشغيل
- ✅ `railway.json` - إعدادات Railway
- ✅ `nixpacks.toml` - إعدادات البناء
- ✅ `runtime.txt` - إصدار Python
- ✅ `.gitignore` - حماية الملفات الحساسة

## 🔍 التحقق من النشر

بعد النشر، تحقق من:

1. **السجلات**: يجب أن ترى "🚀 Bot is starting..."
2. **اختبار البوت**: أرسل `/start` للبوت
3. **الردود**: جرب إرسال رسالة بأي لغة

## 🛠️ التطوير المحلي (اختياري)

```bash
# استنساخ المشروع
git clone https://github.com/username/folloxa-bot.git
cd folloxa-bot

# إعداد البيئة
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# نسخ الإعدادات
cp .env.example .env
# حرر .env وأضف قيمك

# تشغيل البوت
python -m bot.main
```

## 🐛 استكشاف الأخطاء

### البوت لا يعمل؟

1. **تحقق من السجلات** في Railway Dashboard
2. **تأكد من المتغيرات** في تبويب Variables
3. **راجع التوكن** - تأكد من صحته

### أخطاء شائعة:

- `BOT_TOKEN غير موجود` → أضف التوكن في متغيرات البيئة
- `OPENAI_API_KEY غير موجود` → أضف مفتاح OpenAI
- `Unauthorized` → تحقق من صحة التوكن

## 💰 التكاليف

### Railway
- **Hobby Plan**: $5/شهر
- **Pro Plan**: $20/شهر

### OpenAI
- **GPT-4o-mini**: ~$0.15 لكل مليون توكن
- **مراقبة الاستخدام**: في لوحة تحكم OpenAI

## 📊 الميزات

- 🌍 **متعدد اللغات**: يرد بنفس لغة المستخدم
- 🤖 **ذكاء اصطناعي**: GPT-4o-mini للردود الذكية
- 📱 **أزرار تفاعلية**: روابط سريعة للتواصل
- ⚡ **استجابة فورية**: ردود سريعة ومهنية
- 🔄 **إعادة تشغيل تلقائي**: في حالة الأخطاء

## 🔗 الروابط المفيدة

- [Railway Documentation](https://docs.railway.app)
- [Aiogram Documentation](https://aiogram.dev)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📞 الدعم

إذا واجهت مشاكل:

1. راجع [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md) للدليل المفصل
2. تحقق من [TROUBLESHOOTING.md](TROUBLESHOOTING.md) للحلول
3. راجع سجلات Railway للأخطاء

---

<div align="center">

**🎉 البوت جاهز للعمل على Railway!**

[🌐 Folloxa](https://folloxa.com) • [💬 Telegram](https://t.me/folloxa_admin) • [📱 WhatsApp](https://wa.me/0017163036301)

</div>
