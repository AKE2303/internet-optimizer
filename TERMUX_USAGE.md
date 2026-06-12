# Internet Optimizer - Termux uchun

## Termuxda Ishlatish Bo'yicha To'liq Ko'rsatma

### 1️⃣ TERMUX O'RNATISH
- Google Play Store yoki F-Droid dan "Termux" qidiring va o'rnatib qo'ying

### 2️⃣ BIZ REPOSITORIYASI KLONLASH
```bash
apt update && apt upgrade
apt install python3 git
git clone https://github.com/AKE2303/internet-optimizer.git
cd internet-optimizer
```

### 3️⃣ SCRIPTNI ISHGA TUSHIRISH
```bash
python3 internet_optimizer.py
```

### 4️⃣ NATIJANI KO'RISH
- Ekranda barcha testlar ko'rsatiladi
- `optimization_report_SANA.json` faylida saqlandi

---

## 🔧 DNS OPTIMIZE QILISH QADAMLAR:

### Android Sozlamalarida:
```
1. Settings (Sozlamalar)
2. Network & Internet / Connected Devices
3. Advanced → Private DNS / DNS Settings
4. Google: 8.8.8.8 yoki Cloudflare: 1.1.1.1
5. Apni qayta ishga tushiring
```

### Termuxda Script orqali:
```bash
# Tez DNS test qilish
ping -c 4 8.8.8.8
ping -c 4 1.1.1.1
```

---

## 📊 SCRIPT NIMA QILADI?

| Funksiya | Tafsifi |
|----------|---------|
| `test_internet_speed()` | Ping va tezlik testi |
| `get_dns_servers()` | Hozirgi DNS ko'rish |
| `optimize_dns()` | DNS tavsiyalari |
| `test_connection_quality()` | Aloqa sifati |
| `clear_cache()` | Kesh tozalash |
| `network_statistics()` | Tarmoq ma'lumoti |

---

## 🚀 TURLI FOYDALANISH USULLARI:

### Faqat tezlik testi:
```bash
python3 internet_optimizer.py | grep "tezlik"
```

### Faqat DNS tekshirish:
```bash
python3 internet_optimizer.py | grep "DNS"
```

### Hamma narsani ishga tushirish:
```bash
python3 internet_optimizer.py
```

---

## ⚡ TEZLIK OSHIRISH MASLAHAT:

1. ✓ **WiFi Ulanib Ko'ring** - Mobil internet o'rniga WiFi
2. ✓ **Fonda Aplikatsiyalarni Yopib Tashlang** - RAM tozalash
3. ✓ **DNS O'zgartiring** - Cloudflare/Google DNS
4. ✓ **Keshni Tozalang** - `rm -rf ~/.cache/*`
5. ✓ **VPN Ishlatib Ko'ring** - Boshqa serverlar orqali ulanish
6. ✓ **Batareyani Tejash Rejimini O'chib Tashlang**
7. ✓ **Operator Bilan Aloqa Qiling** - Tarmoq muammosi bo'lsa

---

## 📱 TERMUX UCHUN QOSHIMCHA BUYRUQLAR:

```bash
# Tarmoq ma'lumoti
ifconfig

# Ping testi
ping -c 10 google.com

# Speedtest ishga tushirish (o'rnatib olish kerak)
pip install speedtest-cli
speedtest-cli

# DNS test
nslookup google.com

# MTU qiymati ko'rish
ip link show | grep mtu
```

---

## ❓ FAQ

**S:** Script nima vaqt ichida tugadi?
**J:** Odatda 30-60 soniyada

**S:** Termuxda ruxsat xatosi bo'lsa?
**J:** `chmod +x internet_optimizer.py` ishga tushiring

**S:** Script fon rejimida ishlatishim mumkin?
**J:** Ha! Termuxda app ishga tushib qolib, script fonda ishlaydi

**S:** Repeta ishga tushirsam nima bo'ladi?
**J:** Har safar yangi hisobot JSON faylida saqlanadi

---

**Yaratuvchi:** @Ravshan_Karimov_engineer
**Versiya:** 1.0
**Sana:** 2024
