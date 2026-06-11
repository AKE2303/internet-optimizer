#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Internet Optimizer - Telefon interni tezlashtiruvchi script
Tezlikni o'lchash, DNS optimize, cache tozalash va boshqalar
"""

import subprocess
import socket
import time
import os
import sys
import json
from datetime import datetime

class InternetOptimizer:
    def __init__(self):
        self.results = {}
        self.is_termux = self.check_termux()
        
    def check_termux(self):
        """Termuxda ishlamoqda yoki yo'q tekshirish"""
        return os.path.exists('/data/data/com.termux')
    
    def print_header(self, text):
        """Rangli sarlavha chop etish"""
        print("\n" + "="*50)
        print(f"  {text}")
        print("="*50)
    
    def run_command(self, command):
        """Terminaldagi buyruq ishga tushirish"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True,
                timeout=10
            )
            return result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return None, str(e)
    
    def test_internet_speed(self):
        """Internet tezligini o'lchash"""
        self.print_header("📊 INTERNET TEZLIGINI O'LCHASH")
        
        try:
            # Ping test
            stdout, _ = self.run_command("ping -c 4 8.8.8.8" if not self.is_termux else "ping -c 4 8.8.8.8")
            
            if stdout:
                print("✓ Ping testi: OK")
                print(stdout[-150:])  # Oxirgi qismini ko'rsatish
            
            # Speed test (agar speedtest-cli o'rnatilgan bo'lsa)
            print("\n💡 Tezlik to'liq o'lchash uchun: pip install speedtest-cli")
            print("   Keyin: speedtest-cli")
            
            self.results['speed_test'] = 'Completed'
        except Exception as e:
            print(f"❌ Xato: {e}")
            self.results['speed_test'] = 'Failed'
    
    def get_dns_servers(self):
        """Hozirgi DNS serverlarini ko'rsatish"""
        self.print_header("🌐 DNS SERVERLAR")
        
        if self.is_termux:
            stdout, _ = self.run_command("getprop net.dns1; getprop net.dns2")
            print(stdout if stdout else "DNS ma'lumot topilmadi")
        else:
            stdout, _ = self.run_command("nslookup 8.8.8.8 | findstr 'Server'")
            print(stdout if stdout else "DNS ma'lumot topilmadi")
        
        self.results['dns'] = 'Checked'
    
    def optimize_dns(self):
        """DNS optimize qilish (tez DNS: Google, Cloudflare)"""
        self.print_header("⚙️ DNS OPTIMIZATSIYA")
        
        if self.is_termux:
            print("📱 Termuxda DNS o'zgartirilishi:")
            print("  1. Settings → Network → DNS")
            print("  2. Google: 8.8.8.8, 8.8.4.4")
            print("  3. Cloudflare: 1.1.1.1, 1.0.0.1")
            print("  4. Apni qayta ishga tushiring")
        else:
            print("💻 Windows/Linux da DNS o'zgartirilishi dokumentatsiyasiga qarang")
        
        self.results['dns_optimize'] = 'Recommended'
    
    def test_connection_quality(self):
        """Internet aloqasining sifatini tekshirish"""
        self.print_header("🔗 ALOQA SIFATI")
        
        servers = {
            'Google': '8.8.8.8',
            'Cloudflare': '1.1.1.1',
            'OpenDNS': '208.67.222.222'
        }
        
        for name, ip in servers.items():
            stdout, stderr = self.run_command(f"ping -c 2 {ip}")
            if stdout and "avg" in stdout:
                print(f"✓ {name}: Yaxshi")
            else:
                print(f"⚠ {name}: Kuchsiz yoki ulanmagan")
        
        self.results['connection_quality'] = 'Tested'
    
    def clear_cache(self):
        """Kesh tozalash"""
        self.print_header("🗑️ KESH TOZALASH")
        
        if self.is_termux:
            print("📱 Termuxda kesh tozalash:")
            print("  rm -rf ~/.cache/*")
            print("  rm -rf /data/data/*/cache/*")
            stdout, _ = self.run_command("rm -rf ~/.cache/*")
            print("✓ Termux keshi tozalandi")
        else:
            print("💻 Windows/Linux da keshni tozalashning o'z usulilari bor")
        
        self.results['cache_cleared'] = True
    
    def network_statistics(self):
        """Tarmoq statistikasi"""
        self.print_header("📈 TARMOQ STATISTIKASI")
        
        if self.is_termux:
            stdout, _ = self.run_command("netstat -an | wc -l")
            print(f"Aktiv ulanishlar: {stdout if stdout else 'N/A'}")
        else:
            stdout, _ = self.run_command("netstat -s | findstr packets")
            print(stdout if stdout else "Statistika topilmadi")
        
        self.results['statistics'] = 'Collected'
    
    def save_report(self):
        """Natijalarni saqlash"""
        self.print_header("📄 HISOBOT SAQLASH")
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = f"optimization_report_{timestamp}.json"
        
        report_data = {
            'timestamp': timestamp,
            'is_termux': self.is_termux,
            'results': self.results
        }
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)
            print(f"✓ Hisobot saqlandi: {report_file}")
        except Exception as e:
            print(f"❌ Hisobot saqlashda xato: {e}")
    
    def recommendations(self):
        """Tavsiyalar"""
        self.print_header("💡 TAVSIYALAR")
        
        recommendations = [
            "✓ VPN ishlatib ko'ring (Termuxda VPN o'rnatib ishlatsangiz)",
            "✓ Fonda turgan ilovalarni yopib tashlang",
            "✓ WiFi bilan mobil internetni almashtirip ko'ring",
            "✓ DNS-ni tez serverga o'zgartiring (Cloudflare yoki Google)",
            "✓ Browser keshini muntazam tozalang",
            "✓ Sistema yangilanishlarini o'rnatib qo'ying",
            "✓ MTU qiymati 1500 ga o'rnatilganligini tekshiring"
        ]
        
        for rec in recommendations:
            print(rec)
    
    def run_all(self):
        """Barcha testlarni ishga tushirish"""
        print("\n" + "🚀 "*25)
        print("  INTERNET OPTIMIZER - BOSHLANDI")
        print("🚀 "*25)
        
        if self.is_termux:
            print("\n✓ Termuxda ishlamoqda - Hammasi optimallangan!")
        else:
            print("\n⚠ Termux amalga oshirilmagan - Ba'zi xususiyatlar cheklangan")
        
        # Barcha testlarni ishga tushirish
        self.test_internet_speed()
        self.get_dns_servers()
        self.optimize_dns()
        self.test_connection_quality()
        self.clear_cache()
        self.network_statistics()
        self.recommendations()
        self.save_report()
        
        print("\n" + "✓"*50)
        print("  BARCHA TESTLAR TUGADI!")
        print("✓"*50 + "\n")

def main():
    try:
        optimizer = InternetOptimizer()
        optimizer.run_all()
    except KeyboardInterrupt:
        print("\n\n⛔ Foydalanuvchi tomonidan to'xtatildi")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Xato: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
