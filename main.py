"""
Bu çekiliş kodu DijiGO Teknoloji tarafından yapılmıştır.
İletişim: bilgi@dijigo.net
Web Sitesi: www.dijigo.net

Amaç: Bu kod, belirli bir Instagram hesabının takipçileri arasından rastgele kazananlar ve yedek kazananlar seçmek için kullanılır.

Kullanılan Kütüphaneler ve Amaçları:
- instaloader: Instagram profil bilgilerini ve takipçilerini almak için kullanılır.
- secrets: Kriptografik olarak güvenli rastgele seçimler yapmak için kullanılır.
- dotenv: .env dosyasından ortam değişkenlerini yüklemek için kullanılır.
- os: Ortam değişkenlerine erişim sağlamak için kullanılır.
- time: Gecikme ve zamanlama işlemleri için kullanılır.
- tqdm: Takipçileri alırken ilerleme çubuğu göstermek için kullanılır.
"""

import instaloader
import secrets
from dotenv import load_dotenv
import os
import time
from tqdm import tqdm

# .env dosyasını yükleyin
load_dotenv()

# Kullanıcı adı ve şifreyi .env dosyasından alın
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

# Instaloader objesi oluşturun
L = instaloader.Instaloader()

# Kullanıcı adı ve şifre ile giriş yapın
L.login(username, password)

# Hedef kullanıcı adı
target_username = 'dijigonet'

# Hedef profil bilgilerini alın
profile = instaloader.Profile.from_username(L.context, target_username)

# Takipçi sayısını hızlı bir şekilde alın ve yazdırın
total_followers_count = profile.followers
print(f"Toplam takipçi sayısı: {total_followers_count}")

# Takipçileri alın ve isimlerini yazdırın
followers = profile.get_followers()
followers_list = []

print("Takipçiler alınıyor...")
for follower in tqdm(followers, desc="Takipçiler alınıyor", unit="takipçi"):
    followers_list.append(follower.username)

# Takipçi sayısını kontrol edin
if total_followers_count < 24:
    print("Takipçi sayısı 24'ten az olduğu için çekiliş yapılamıyor.")
else:
    # 24 kişiyi kriptografik olarak güvenli bir şekilde rastgele seçin (12 kazanan ve 12 yedek)
    selected = secrets.SystemRandom().sample(followers_list, 24)
    winners = selected[:12]
    backups = selected[12:]

    # Geri sayım ile kazananları yazdırma
    print("\n" + "*" * 50 + "\n")
    print("Çekilişi kazananlar:")

    for i, winner in enumerate(winners, 1):
        print(f"{i}. kazanan: {winner}")
        time.sleep(2)
        #tqdm.write(f"Progres: {i}/24")

    print("\n" + "*" * 50 + "\n")
    print("Yedek kazananlar:")

    for i, backup in enumerate(backups, 1):
        print(f"{i}. yedek kazanan: {backup}")
        time.sleep(2)
        #tqdm.write(f"Progres: {12 + i}/24")

    print("\n" + "*" * 50 + "\n")
    print("Çekiliş bitmiştir. Kazananları ve yedek kazananları tebrik ederiz.")
