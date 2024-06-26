import secrets
import time

# Dosyadan takipçi listesini oku
with open('followers.txt', 'r') as f:
    followers_list = f.read().splitlines()

# Toplam takipçi sayısını yazdır
total_followers_count = len(followers_list)
print(f"Toplam takipçi sayısı: {total_followers_count}")

# Takipçi sayısını kontrol edin
if total_followers_count < 24:
    print("Takipçi sayısı 24'ten az olduğu için çekiliş yapılamıyor.")
else:
    # 36 kişiyi kriptografik olarak güvenli bir şekilde rastgele seçin (12 kazanan ve 24 yedek)
    selected = secrets.SystemRandom().sample(followers_list, 36)
    winners = selected[:12]
    backups = selected[12:]

    # Geri sayım ile kazananları yazdırma
    print("\n" + "*" * 50 + "\n")
    print("Çekilişi kazananlar:")

    for i, winner in enumerate(winners, 1):
        print(f"{i}. kazanan: {winner}")
        time.sleep(2)

    print("\n" + "*" * 50 + "\n")
    print("Yedek kazananlar:")

    for i, backup in enumerate(backups, 1):
        print(f"{i}. yedek kazanan: {backup}")
        time.sleep(2)

    print("\n" + "*" * 50 + "\n")
    print("Çekiliş bitmiştir. Kazananları ve yedek kazananları tebrik ederiz.")