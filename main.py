from playwright.sync_api import sync_playwright
import time


def tiktok_veri_cek():
    with sync_playwright() as p:
        print("Tarayıcı kamuflajlı olarak başlatılıyor...")

        # 1. BOT GİZLEME TAKTİĞİ: Otomasyon yazılımı olduğumuzu belli eden özellikleri kapatıyoruz
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        # 2. KİMLİK TAKLİDİ: Kendimizi sıradan bir Windows bilgisayardaki Chrome gibi tanıtıyoruz
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )

        page = context.new_page()

        print("TikTok #climate sayfasına gidiliyor...")
        page.goto("https://www.tiktok.com/tag/climate")

        print("-------------------------------------------------")
        print("DİKKAT: Sayfa açıldı. 15 Saniye süreniz var.")
        print("Eğer yine 'Bir şeyler ters gitti' derse, ekrandaki 'Yenile' butonuna manuel basın!")
        print("-------------------------------------------------")
        time.sleep(15)  # Sayfanın oturması ve gerekirse senin müdahalen için süre

        print("Sayfa aşağı kaydırılıyor...")
        for i in range(5):  # 5 kez aşağı kaydırır
            page.mouse.wheel(0, 1500)
            time.sleep(3)

        print("Video linkleri toplanıyor...")
        video_linkleri = set()

        link_elementleri = page.locator("a").all()
        for element in link_elementleri:
            href = element.get_attribute("href")
            if href and "/video/" in href:
                video_linkleri.add(href)

        print(f"\n✅ Toplam {len(video_linkleri)} benzersiz video linki bulundu!")

        with open("climate_toplanan_videolar.txt", "w", encoding="utf-8") as f:
            for link in video_linkleri:
                f.write(link + "\n")

        print("Tüm linkler 'climate_toplanan_videolar.txt' dosyasına kaydedildi.")

        browser.close()


if __name__ == "__main__":
    tiktok_veri_cek()