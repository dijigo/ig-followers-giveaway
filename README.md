# Instagram Giveaway Script

Bu çekiliş kodu DijiGO Teknoloji tarafından yapılmıştır.
İletişim: bilgi@dijigo.net
Web Sitesi: [www.dijigo.net](http://www.dijigo.net)

## Amaç

Bu kod, belirli bir Instagram hesabının takipçileri arasından rastgele kazananlar ve yedek kazananlar seçmek için kullanılır.

## Kullanılan Kütüphaneler ve Amaçları

- `instaloader`: Instagram profil bilgilerini ve takipçilerini almak için kullanılır.
- `secrets`: Kriptografik olarak güvenli rastgele seçimler yapmak için kullanılır.
- `dotenv`: .env dosyasından ortam değişkenlerini yüklemek için kullanılır.
- `os`: Ortam değişkenlerine erişim sağlamak için kullanılır.
- `time`: Gecikme ve zamanlama işlemleri için kullanılır.
- `tqdm`: Takipçileri alırken ilerleme çubuğu göstermek için kullanılır.

## Kurulum

1. Gerekli Python kütüphanelerini yükleyin:
    ```sh
    pip install instaloader python-dotenv tqdm
    ```

2. Proje dizininde bir `.env` dosyası oluşturun ve Instagram kullanıcı adı ve şifrenizi ekleyin:
    ```
    INSTAGRAM_USERNAME=your_username
    INSTAGRAM_PASSWORD=your_password
    ```

3. Çekilişi başlatmak için aşağıdaki komutu çalıştırın:
    ```sh
    python your_script_name.py
    ```

## .gitignore Dosyası

Projenizi GitHub'a yüklerken `.env` dosyasını hariç tutmak için `.gitignore` dosyasını eklediğinizden emin olun:
```plaintext
# .env dosyasını hariç tut
.env

# Diğer tipik dosya ve dizinleri hariç tut
__pycache__/
*.py[cod]
*$py.class
venv/
.envrc
.idea/
.vscode/
*.log
*.sqlite3
.DS_Store
