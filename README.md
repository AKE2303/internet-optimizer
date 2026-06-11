# 📱 Internet Optimizer - Python Script

Telefon interni tezlashtiruvchi va optimize qiluvchi Python scripti.

## ✨ Xususiyatlari

- 📊 **Internet tezligini o'lchash** - Ping testi va tezlik kontrili
- 🌐 **DNS serverlarini tekshirish** - Hozirgi DNS ko'rish
- ⚙️ **DNS optimizatsiya** - Tez DNS serverlarni tavsiya (Google, Cloudflare)
- 🔗 **Aloqa sifatini tekshirish** - Turli serverlar bilan ulanish
- 🗑️ **Kesh tozalash** - Cache fayllarini o'chirish
- 📈 **Tarmoq statistikasi** - Faol ulanishlarni ko'rish
- 💡 **Tavsiyalar** - Internet tezligini oshirish bo'yicha maslahatlar
- 📄 **Hisobot saqlash** - Natijalarni JSON formatida saqlash

## 🚀 Termuxda Ishlatish

### 1. O'rnatish
```bash
# Termuxni ochib, Python ni o'rnatish
apt update
apt install python3 git

# Repositoriyani klonlash
git clone https://github.com/YOUR_USERNAME/internet-optimizer.git
cd internet-optimizer
```

### 2. Ishga Tushirish
```bash
python3 internet_optimizer.py
```

### 3. Natijalar
- Ekranda barcha testlar natijasi ko'rsatiladi
- JSON faylida hisobot saqlanadi (masalan: `optimization_report_2024-01-15_10-30-45.json`)

## 💻 Windows/Linux da

```bash
python3 internet_optimizer.py
```

## 📋 Talab Qiladigan Paketlar

```
requests
```

O'rnatish:
```bash
pip install -r requirements.txt
```

## 🔧 DNS Optimize Qilish

### Android (Termux):
1. Settings → Network → DNS
2. Google DNS: `8.8.8.8`, `8.8.4.4`
3. Cloudflare DNS: `1.1.1.1`, `1.0.0.1`
4. Apni qayta ishga tushiring

### Internet Tezligini Oshirish Yo'llari:
- ✓ WiFi signali kuchli joyda bo'ling
- ✓ Fonda turgan ilovalarni yopib tashlang
- ✓ Brauzer keshini tozalang
- ✓ VPN dan foydalaning
- ✓ Mobil Internet operatoriga murojaat qiling

## 📝 Hisobot Faylining Misoli

```json
{
  "timestamp": "2024-01-15_10-30-45",
  "is_termux": true,
  "results": {
    "speed_test": "Completed",
    "dns": "Checked",
    "dns_optimize": "Recommended",
    "connection_quality": "Tested",
    "cache_cleared": true,
    "statistics": "Collected"
  }
}
```

## 🐛 Muammolar

Agar xatolik bo'lsa:
1. Python3 o'rnatilganligini tekshiring: `python3 --version`
2. Ruxsatlarni tekshiring: `chmod +x internet_optimizer.py`
3. Termuxda: `termux-fix-shebang internet_optimizer.py`

## 📞 Bog'lanish

GitHub: [https://github.com/AKE2303]
Telegram: @turdiyevazam

## 📄 Litsenziya

MIT License

---

**Yaratildi:** Python 3.6+
**Oxirgi Yangilanish:** 2024
