```
# Çekiliş Uygulaması

Bu Python betiği, bir takipçi listesinden rastgele kazananlar seçmek için kullanılır.

## Kullanım

1. `followers.txt` adlı bir dosya oluşturun ve her satırda bir takipçi kullanıcı adı olacak şekilde takipçi listesini bu dosyaya ekleyin.
2. Betiği çalıştırın.
3. Betik, takipçi listesinden 12 kazanan ve 24 yedek seçecektir.

## Gereksinimler

* Python 3.6 veya üstü
* `secrets` paketi

## Kurulum

1. `secrets` paketini yükleyin:
```bash
pip install secrets
```

## Çalıştırma

1. Terminale veya komut istemine aşağıdaki komutu girin:
```bash
python main.py
```

## Notlar

* Betik, takipçileri kriptografik olarak güvenli bir şekilde rastgele seçer.
* `secrets` paketi, rastgele sayılar üretmek için işletim sistemi tarafından sağlanan rastgele sayı üreticisini kullanır.
* `followers.txt` dosyası aynı dizinde olmalıdır.
* Kazananlar ve yedekler, her birinin 2 saniye bekleme süresiyle ayrı ayrı yazdırılır.

## Lisans

Bu betik, MIT lisansı altında yayınlanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
```
