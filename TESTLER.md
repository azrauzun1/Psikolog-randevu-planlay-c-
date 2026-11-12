# Gerçek Python test sonuçları

**Son sürüm:** `uygulama.py`  
**Tarih:** 12.11.2026  
**Ortam:** Python 3.13.5; her senaryo bağımsız geçici klasörde çalıştırıldı.

Testlerde gerçek danışan bilgisi kullanılmadı. Kaydetme hatası testi yapay olarak `unittest.mock` ile oluşturuldu.

| # | Girdi / senaryo | Beklenen | Gözlenen |
|---|---|---|---|
| 1 | Normal randevu ve kaydetme | Kayıt dosyası oluşturulur | Başarılı |
| 2 | Çakışan randevuyu reddetme | Çakışan ikinci kayıt eklenmez | Başarılı |
| 3 | Ardışık randevuları kabul etme | Ardışık seans kabul edilir | Başarılı |
| 4 | Boş danışan kodu yeniden sorulur | Boş kod reddedilir; ikinci kod kabul edilir | Başarılı |
| 5 | Geçersiz tarih reddedilir | Geçersiz tarih reddedilir; geçerli tarih kabul edilir | Başarılı |
| 6 | Geçmiş tarih reddedilir | Geçmiş tarih reddedilir | Başarılı |
| 7 | Hatalı saat yeniden sorulur | Geçersiz saat reddedilir | Başarılı |
| 8 | Sıfır süre ve negatif süre reddedilir | 0 ve -5 reddedilir | Başarılı |
| 9 | Mesai bitişini aşan randevu reddedilir | 18:00 bitişini aşan seans reddedilir | Başarılı |
| 10 | Gizlilik raporunda kod çıkmaz | Gizli raporda danışan kodu yoktur | Başarılı |
| 11 | Program yeniden açılınca randevu yüklenir | İkinci çalıştırmada eski kayıt yüklenir | Başarılı |
| 12 | Bozuk kayıt dosyası güvenle durdurulur | Bozuk dosya bozulmadan kalır ve uygulama durur | Başarılı |
| 13 | Kaydetme hatasında eski TXT korunur (simülasyon) | Yapay kaydetme hatasında önceki dosya korunur | Başarılı |

## Örnek gerçek konsol çıktısı

```text
--- PSİKOLOG RANDEVU PLANLAYICISI ---
1) Randevu ekle
2) Randevuları görüntüle
3) TXT raporu kaydet
4) Gizlilik odaklı TXT raporu kaydet
5) Çıkış
Seçiminiz (1-5): Anonim danışan kodu (örn. D001): Randevu tarihi (GG.AA.YYYY): Başlangıç saati (SS:DD): Seans süresi (30/45/60 dakika): Rapor kaydedildi: randevu_raporu.txt
Randevu başarıyla eklendi.

--- PSİKOLOG RANDEVU PLANLAYICISI ---
1) Randevu ekle
2) Randevuları görüntüle
3) TXT raporu kaydet
4) Gizlilik odaklı TXT raporu kaydet
5) Çıkış
Seçiminiz (1-5): Program kapatıldı.
```

## Hata ayıklama notu

PROMPT 3 öncesinde kayıt dosyasından otomatik yeniden yükleme yapılmıyordu. Bu eksikliği gidermek üzere `randevulari_yukle()` fonksiyonu eklendi. PROMPT 5 kapsamında dosya kaydetme hatasında mevcut dosyanın korunması ve bellek kaydının geri alınması ele alındı. Son sürümde kaydetme hatası `os.replace` için kontrollü bir istisna üretilerek test edildi.

**Sınır:** Bu testler tüm cihazlarda veya gerçek disk arızalarında hatasız çalışacağını garanti etmez.
