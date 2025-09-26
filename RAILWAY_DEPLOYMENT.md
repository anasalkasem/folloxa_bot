# دليل نشر Folloxa Bot على Railway

## نظرة عامة

هذا الدليل يوضح كيفية نشر **Folloxa Bot** على منصة **Railway** خطوة بخطوة.

## المتطلبات المسبقة

1. **حساب Railway**: سجل في [railway.app](https://railway.app)
2. **حساب GitHub**: لرفع الكود
3. **توكن البوت**: احصل عليه من [@BotFather](https://t.me/BotFather)
4. **مفتاح OpenAI**: احصل عليه من [OpenAI Platform](https://platform.openai.com/api-keys)

## خطوات النشر

### الخطوة 1: رفع الكود إلى GitHub

1. **إنشاء مستودع جديد** على GitHub
2. **رفع ملفات المشروع**:
```bash
git init
git add .
git commit -m "Initial commit: Folloxa Bot for Railway"
git branch -M main
git remote add origin https://github.com/username/folloxa-bot.git
git push -u origin main
```

### الخطوة 2: إنشاء مشروع على Railway

1. اذهب إلى [railway.app](https://railway.app)
2. اضغط على **"New Project"**
3. اختر **"Deploy from GitHub repo"**
4. اختر مستودع **folloxa-bot**
5. اضغط على **"Deploy Now"**

### الخطوة 3: إعداد متغيرات البيئة

في لوحة تحكم Railway:

1. اذهب إلى تبويب **"Variables"**
2. أضف المتغيرات التالية:

| المتغير | القيمة | الوصف |
|---------|--------|-------|
| `BOT_TOKEN` | `123456:ABC-DEF...` | توكن البوت من BotFather |
| `OPENAI_API_KEY` | `sk-proj-...` | مفتاح OpenAI API |
| `SITE_URL` | `https://folloxa.com` | رابط الموقع (اختياري) |
| `CONTACT_WHATSAPP` | `0017163036301` | رقم الواتساب (اختياري) |
| `CONTACT_TELEGRAM` | `folloxa_admin` | معرف التلغرام (اختياري) |

### الخطوة 4: التحقق من النشر

1. **مراقبة السجلات**: اذهب إلى تبويب **"Deployments"** لمراقبة عملية النشر
2. **فحص السجلات**: تأكد من ظهور رسالة "🚀 Bot is starting..."
3. **اختبار البوت**: أرسل `/start` للبوت على تلغرام

## ملفات التكوين المضافة

### 1. `Procfile`
```
web: python -m bot.main
```

### 2. `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python -m bot.main",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 3. `nixpacks.toml`
```toml
[phases.setup]
nixPkgs = ["python311"]

[phases.install]
cmds = [
    "pip install --upgrade pip",
    "pip install -r requirements.txt"
]

[start]
cmd = "python -m bot.main"
```

### 4. `runtime.txt`
```
python-3.11
```

## استكشاف الأخطاء

### مشكلة: البوت لا يستجيب

**الحلول**:
1. تحقق من صحة `BOT_TOKEN` في متغيرات البيئة
2. تأكد من أن البوت مفعل مع @BotFather
3. راجع السجلات في Railway للأخطاء

### مشكلة: خطأ OpenAI API

**الحلول**:
1. تحقق من صحة `OPENAI_API_KEY`
2. تأكد من وجود رصيد في حساب OpenAI
3. تحقق من حدود الاستخدام

### مشكلة: فشل في النشر

**الحلول**:
1. تحقق من ملف `requirements.txt`
2. راجع سجلات البناء في Railway
3. تأكد من صحة ملفات التكوين

## مراقبة الأداء

### السجلات
- **الوصول**: Railway Dashboard → Deployments → View Logs
- **المراقبة**: راقب رسائل الخطأ والتحذيرات

### الموارد
- **الذاكرة**: Railway يوفر 512MB افتراضياً
- **المعالج**: مشترك مع حدود استخدام عادلة
- **الشبكة**: بدون حدود للبيانات الواردة/الصادرة

## التحديثات

لتحديث البوت:

1. **ادفع التغييرات** إلى GitHub:
```bash
git add .
git commit -m "Update bot features"
git push
```

2. **النشر التلقائي**: Railway سيعيد النشر تلقائياً

## الأمان

### حماية المفاتيح
- ✅ **لا تضع** المفاتيح في الكود
- ✅ **استخدم** متغيرات البيئة في Railway
- ✅ **أضف** `.env` إلى `.gitignore`

### أفضل الممارسات
- 🔄 **دوّر المفاتيح** بانتظام
- 📊 **راقب الاستخدام** والتكاليف
- 🔒 **قيّد الأذونات** حسب الحاجة

## التكاليف

### Railway Pricing
- **Hobby Plan**: $5/شهر - مناسب للاستخدام الشخصي
- **Pro Plan**: $20/شهر - للاستخدام التجاري

### OpenAI Pricing
- **GPT-4o-mini**: ~$0.15 لكل مليون توكن
- **مراقبة التكاليف**: راجع لوحة تحكم OpenAI

## الدعم

### مصادر المساعدة
- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Railway Discord**: [discord.gg/railway](https://discord.gg/railway)
- **OpenAI Support**: [help.openai.com](https://help.openai.com)

### المشاكل الشائعة
راجع ملف `TROUBLESHOOTING.md` للحلول التفصيلية.

---

🎉 **تهانينا!** البوت الآن يعمل على Railway ومتاح 24/7!
