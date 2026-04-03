import yt_dlp
import pandas as pd
import time


def verileri_cek_ve_sirala():
    # 1. Bir önceki adımda topladığımız linkleri oku
    dosya_adi = "climate_toplanan_videolar.txt"
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            linkler = [satir.strip() for satir in f.readlines() if satir.strip()]
    except FileNotFoundError:
        print(f"HATA: '{dosya_adi}' dosyası bulunamadı! Lütfen aynı klasörde olduğundan emin olun.")
        return

    print(f"Toplam {len(linkler)} video incelenecek. Veriler çekiliyor...")

    video_verileri = []

    # yt-dlp ayarları (Sadece bilgi çeker, videoyu KESİNLİKLE indirmez)
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i, link in enumerate(linkler):
            print(f"[{i + 1}/{len(linkler)}] Veri çekiliyor: {link}")
            try:
                # Video bilgilerini arka plandan al
                info = ydl.extract_info(link, download=False)

                # İhtiyacımız olanları listeye ekle
                video_verileri.append({
                    "Hesap Adı": info.get("uploader", "Bilinmiyor"),
                    "İzlenme Sayısı": info.get("view_count", 0),
                    "Beğeni Sayısı": info.get("like_count", 0),
                    "Video Linki": link
                })
            except Exception as e:
                print(f"   -> Hata oluştu, video gizli veya silinmiş olabilir. Atlanıyor...")

            # TikTok'u şüphelendirmemek için her videoda yarım saniye bekle
            time.sleep(0.5)

            # 2. Toplanan verileri Excel tablosuna (Pandas DataFrame) çevir
    df = pd.DataFrame(video_verileri)

    # 3. İZLENME SAYISINA GÖRE BÜYÜKTEN KÜÇÜĞE SIRALA
    df = df.sort_values(by="İzlenme Sayısı", ascending=False)

    # 4. Excel dosyası olarak kaydet
    excel_adi = "climate_sirali_liste.xlsx"
    df.to_excel(excel_adi, index=False)

    print(f"\n✅ İŞLEM TAMAM! Tüm veriler '{excel_adi}' dosyasına kaydedildi.")
    print("\n--- İLK 5 VİDEO ÖZETİ ---")
    print(df.head(5)[["Hesap Adı", "İzlenme Sayısı", "Beğeni Sayısı"]].to_string(index=False))


if __name__ == "__main__":
    verileri_cek_ve_sirala()