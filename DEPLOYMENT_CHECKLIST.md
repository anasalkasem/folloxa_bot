# قائمة التحقق من النشر - Railway

## ✅ قبل النشر

### 1. الملفات المطلوبة
- [x] `Procfile` - أمر التشغيل
- [x] `railway.json` - إعدادات Railway
- [x] `nixpacks.toml` - إعدادات البناء
- [x] `runtime.txt` - إصدار Python
- [x] `requirements.txt` - المتطلبات
- [x] `.gitignore` - حماية الملفات
- [x] `.env.example` - مثال الإعدادات

### 2. بنية المشروع
- [x] `bot/__init__.py` - حزمة Python
- [x] `bot/main.py` - نقطة البداية
- [x] `bot/config.py` - الإعدادات
- [x] `bot/handlers.py` - معالجات الرسائل
- [x] `bot/keyboards.py` - الأزرار

### 3. الكود
- [x] جميع الاستيرادات تعمل
- [x] لا توجد أخطاء نحوية
- [x] متغيرات البيئة محمية

## 🚀 خطوات النشر

### 1. رفع إلى GitHub
```bash
git init
git add .
git commit -m "Ready for Railway deployment"
git branch -M main
git remote add origin https://github.com/username/folloxa-bot.git
git push -u origin main
```

### 2. النشر على Railway
1. اذهب إلى [railway.app](https://railway.app)
2. **New Project** → **Deploy from GitHub repo**
3. اختر المستودع
4. أضف متغيرات البيئة:
   - `BOT_TOKEN`
   - `OPENAI_API_KEY`
   - `SITE_URL` (اختياري)
   - `CONTACT_WHATSAPP` (اختياري)
   - `CONTACT_TELEGRAM` (اختياري)

### 3. التحقق من النشر
- [ ] السجلات تظهر "🚀 Bot is starting..."
- [ ] لا توجد أخطاء في السجلات
- [ ] البوت يرد على `/start`
- [ ] الأزرار تعمل بشكل صحيح

## 🔧 متغيرات البيئة

### مطلوبة
| المتغير | المصدر | مثال |
|---------|--------|-------|
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) | `123456:ABC-DEF...` |
| `OPENAI_API_KEY` | [OpenAI Platform](https://platform.openai.com/api-keys) | `sk-proj-...` |

### اختيارية
| المتغير | القيمة الافتراضية |
|---------|------------------|
| `SITE_URL` | `https://folloxa.com` |
| `CONTACT_WHATSAPP` | `0017163036301` |
| `CONTACT_TELEGRAM` | `folloxa_admin` |

## 🐛 استكشاف الأخطاء

### أخطاء شائعة
1. **"BOT_TOKEN غير موجود"**
   - تأكد من إضافة التوكن في متغيرات البيئة
   - تحقق من صحة التوكن

2. **"OPENAI_API_KEY غير موجود"**
   - أضف مفتاح OpenAI في متغيرات البيئة
   - تأكد من وجود رصيد في الحساب

3. **"Module not found"**
   - تحقق من ملف `requirements.txt`
   - راجع سجلات البناء

### فحص السجلات
في Railway Dashboard:
1. اذهب إلى **Deployments**
2. اضغط على آخر نشر
3. راجع **Build Logs** و **Deploy Logs**

## 📊 بعد النشر

### المراقبة
- [ ] راقب استهلاك الموارد
- [ ] تحقق من سجلات الأخطاء
- [ ] راقب تكاليف OpenAI

### الصيانة
- [ ] حدّث المتطلبات بانتظام
- [ ] راقب أداء البوت
- [ ] احتفظ بنسخة احتياطية من الإعدادات

## 🎉 النجاح!

إذا رأيت:
- ✅ "🚀 Bot is starting..." في السجلات
- ✅ البوت يرد على الرسائل
- ✅ الأزرار تعمل

**تهانينا! البوت يعمل بنجاح على Railway! 🎉**

---

للمساعدة الإضافية، راجع:
- [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md) - دليل مفصل
- [README_RAILWAY.md](README_RAILWAY.md) - معلومات المشروع
