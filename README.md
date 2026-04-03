# TikTok Hashtag Scraper Bot

Bu proje, TikTok'un öneri algoritmasını denetlemek, belirli etiketler (#iklimkrizi vb.) altındaki popüler videoları analiz etmek için geliştirilmiş bir otomatize veri toplama aracıdır.

## Özellikler
* **Veri Kazıma:** Belirtilen bir TikTok etiket sayfasındaki (hashtag) video bağlantılarını otomatik olarak toplar (Playwright).
* **Meta Veri Çıkarımı:** Videoların izlenme, beğeni ve yükleyici hesabı gibi meta verilerini videoları indirmeden arka planda çeker (yt-dlp).
* **Yapılandırılmış Veri:** Elde edilen verileri algoritmik popülerliğe göre sıralayarak içerik analizi için Excel dosyasına dönüştürür (Pandas).

## Kurulum
Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Bu depoyu bilgisayarınıza indirin.
2. Gerekli kütüphaneleri (bağımlılıkları) kurmak için terminale şu komutu yazın:
```bash
pip install -r requirements.txt
```

## Kullanım
İlk olarak belirlenen etiket üzerinden linkleri toplamak için ana botu çalıştırın:
```bash
python main.py
```

Toplanan ham linkleri analiz edip sıralı bir Excel veri setine dönüştürmek için sıralama botunu çalıştırın:
```bash
python siralama_botu.py
```
