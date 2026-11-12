"""Psikolog seans ve randevu planlayıcısı (öğrenci projesi).

Gerçek danışan bilgileri yerine anonim kodlar kullanılmalıdır.
"""
from datetime import date, datetime, timedelta
from pathlib import Path
import os
import re
import tempfile

RANDEVULAR = []
DOSYA_YOLU = Path(__file__).with_name('randevu_raporu.txt')
GIZLI_RAPOR_YOLU = Path(__file__).with_name('gizlilik_odakli_rapor.txt')
CALISMA_BASLANGICI = '09:00'
CALISMA_BITISI = '18:00'


def tarih_al(metin):
    """GG.AA.YYYY biçiminde geçerli tarih ister."""
    while True:
        deger = input(metin).strip()
        try:
            tarih = datetime.strptime(deger, '%d.%m.%Y').date()
            if tarih.strftime('%d.%m.%Y') != deger:
                raise ValueError
            # DUZELTME (PROMPT 2): Geçmiş günlere yeni randevu verilmesini önle.
            # Bugünün tarihi sistemden alınır; 2030 senaryosu için sabit yıl kullanılmaz.
            if tarih < date.today():
                print('Geçmiş bir tarihe randevu oluşturulamaz. Bugün veya daha ileri bir tarih girin.')
                continue
            return tarih
        except ValueError:
            print('Hatalı tarih. Örnek: 15.11.2030')


def saat_al(metin):
    """SS:DD biçiminde geçerli saat ister."""
    while True:
        deger = input(metin).strip()
        try:
            saat = datetime.strptime(deger, '%H:%M').time()
            if saat.strftime('%H:%M') != deger:
                raise ValueError
            return saat
        except ValueError:
            print('Hatalı saat. Örnek: 14:30')


def sure_al():
    """Seans süresini 30, 45 veya 60 dakika ile sınırlar."""
    while True:
        deger = input('Seans süresi (30/45/60 dakika): ').strip()
        if deger in ('30', '45', '60'):
            return int(deger)
        print('Lütfen 30, 45 veya 60 girin.')


def kod_al():
    """Danışanın gerçek adını değil, anonim kodunu alır."""
    while True:
        kod = input('Anonim danışan kodu (örn. D001): ').strip().upper()
        if 2 <= len(kod) <= 12 and kod.isalnum():
            return kod
        print('Kod 2-12 karakter olmalı ve yalnızca harf/rakam içermeli.')


def cakisma_var_mi(baslangic, bitis):
    """Aynı gün kısmen veya tamamen çakışan seansları bulur."""
    for randevu in RANDEVULAR:
        if baslangic < randevu['bitis'] and bitis > randevu['baslangic']:
            return True
    return False


def calisma_saatine_uygun_mu(baslangic, bitis):
    """Seansın tamamının 09:00-18:00 arasında olup olmadığını kontrol eder."""
    acilis = datetime.combine(baslangic.date(), datetime.strptime(CALISMA_BASLANGICI, '%H:%M').time())
    kapanis = datetime.combine(baslangic.date(), datetime.strptime(CALISMA_BITISI, '%H:%M').time())
    return acilis <= baslangic and bitis <= kapanis


def randevu_ekle():
    """Dört kullanıcı girdisini kontrol ederek randevu oluşturur."""
    kod = kod_al()
    tarih = tarih_al('Randevu tarihi (GG.AA.YYYY): ')
    saat = saat_al('Başlangıç saati (SS:DD): ')
    sure = sure_al()
    baslangic = datetime.combine(tarih, saat)
    bitis = baslangic + timedelta(minutes=sure)

    # DUZELTME: Yalnızca başlangıç saatini değil, seansın bitişini de kontrol et.
    # Örneğin 17:45'te başlayan 30 dakikalık seans 18:00'i aşacağı için reddedilir.
    if not calisma_saatine_uygun_mu(baslangic, bitis):
        print('Randevu eklenemedi: Seans 09:00-18:00 çalışma saatleri içinde tamamlanmalıdır.')
    elif cakisma_var_mi(baslangic, bitis):
        print('Randevu eklenemedi: Bu saat aralığında başka bir seans var.')
    else:
        yeni_randevu = {'kod': kod, 'baslangic': baslangic, 'bitis': bitis, 'sure': sure}
        RANDEVULAR.append(yeni_randevu)
        # DUZELTME (PROMPT 5): Disk kaydı başarısız olursa bellek kaydını geri al.
        # Böylece kullanıcıya yanlışlıkla 'başarıyla eklendi' denmez.
        if rapor_kaydet():
            print('Randevu başarıyla eklendi.')
        else:
            RANDEVULAR.remove(yeni_randevu)
            print('Randevu eklenemedi; kayıt güvenle geri alındı.')


def rapor_metni(gizlilik_odakli=False):
    """Randevuları sıralar; gizlilik raporunda danışan kodlarını göstermez."""
    satirlar = ['PSİKOLOG RANDEVU PLANI', '=' * 48]
    if not RANDEVULAR:
        satirlar.append('Henüz randevu bulunmuyor.')
    else:
        for sira, randevu in enumerate(sorted(RANDEVULAR, key=lambda r: r['baslangic']), 1):
            bas = randevu['baslangic']
            bit = randevu['bitis']
            satir = f"{sira:>2}. {bas:%d.%m.%Y}  {bas:%H:%M}-{bit:%H:%M}"
            # PROMPT 4: Paylaşılabilir raporda danışan kodu gösterilmez.
            # Kalıcı kayıt dosyasında kod kalır; aksi halde açılışta geri yükleme bozulur.
            if not gizlilik_odakli:
                satir += f"  Kod: {randevu['kod']}"
            satir += f"  Süre: {randevu['sure']} dk"
            satirlar.append(satir)
    return '\n'.join(satirlar)


def rapor_kaydet():
    """Raporu önce geçici dosyaya yazar; başarılı olunca asıl dosyayla değiştirir."""
    gecici_dosya = None
    try:
        # DUZELTME (PROMPT 5): Doğrudan asıl dosyaya yazmak yerine aynı
        # klasörde geçici dosya kullanılır. Hata olursa eski kayıt korunur.
        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', dir=DOSYA_YOLU.parent,
            prefix='.randevu_', suffix='.tmp', delete=False
        ) as dosya:
            gecici_dosya = Path(dosya.name)
            dosya.write(rapor_metni() + '\n')
            dosya.flush()
            os.fsync(dosya.fileno())
        os.replace(gecici_dosya, DOSYA_YOLU)
        print(f'Rapor kaydedildi: {DOSYA_YOLU.name}')
        return True
    except OSError as hata:
        print(f'Rapor kaydedilemedi: {hata}')
        return False
    finally:
        if gecici_dosya is not None:
            try:
                gecici_dosya.unlink(missing_ok=True)
            except OSError:
                pass


def gizlilik_raporu_kaydet():
    """Danışan kodlarını içermeyen ayrı bir paylaşım raporu oluşturur."""
    try:
        GIZLI_RAPOR_YOLU.write_text(rapor_metni(gizlilik_odakli=True) + '\n', encoding='utf-8')
        print(f'Gizlilik odaklı rapor kaydedildi: {GIZLI_RAPOR_YOLU.name}')
    except OSError as hata:
        print(f'Gizlilik odaklı rapor kaydedilemedi: {hata}')


def randevulari_yukle():
    """Önceki TXT raporunu okuyup randevu listesini yeniden oluşturur."""
    if not DOSYA_YOLU.exists():
        return
    try:
        satirlar = DOSYA_YOLU.read_text(encoding='utf-8').splitlines()
    except OSError as hata:
        print(f'Eski randevular okunamadı: {hata}')
        return

    # Rapor formatındaki bilgileri yakalar; kullanıcı adına/sağlık verisine ihtiyaç yok.
    kalip = re.compile(
        r'^\s*\d+\.\s+(\d{2}\.\d{2}\.\d{4})\s+'
        r'(\d{2}:\d{2})-(\d{2}:\d{2})\s+'
        r'Kod:\s*([A-Z0-9]{2,12})\s+Süre:\s*(30|45|60)\s+dk$'
    )
    gecersiz = 0
    bulunan = 0
    for satir in satirlar[2:]:
        if satir == 'Henüz randevu bulunmuyor.' or not satir.strip():
            continue
        eslesme = kalip.fullmatch(satir)
        if not eslesme:
            gecersiz += 1
            continue
        gun, bas_saat, bit_saat, kod, sure_metin = eslesme.groups()
        try:
            bas = datetime.strptime(gun + ' ' + bas_saat, '%d.%m.%Y %H:%M')
            bit = datetime.strptime(gun + ' ' + bit_saat, '%d.%m.%Y %H:%M')
            sure = int(sure_metin)
            if bit - bas != timedelta(minutes=sure) or not calisma_saatine_uygun_mu(bas, bit):
                raise ValueError('Tutarsız randevu')
            if cakisma_var_mi(bas, bit):
                raise ValueError('Çakışan kayıt')
        except ValueError:
            gecersiz += 1
            continue
        RANDEVULAR.append({'kod': kod, 'baslangic': bas, 'bitis': bit, 'sure': sure})
        bulunan += 1
    if gecersiz:
        # Eksik/hatalı dosyayı kaydederek silmemek için yeni kayıt eklemeyi durdur.
        print(f'Uyarı: {gecersiz} satır okunamadı. Veri kaybını önlemek için dosyayı kontrol edin.')
        raise SystemExit('Rapor formatı hatalı; uygulama güvenli biçimde durduruldu.')
    print(f'Önceki randevular yüklendi: {bulunan} kayıt.')


def ana_menu():
    """Kullanıcı çıkış seçeneğini seçene dek menüyü gösterir."""
    while True:
        print('\n--- PSİKOLOG RANDEVU PLANLAYICISI ---')
        print('1) Randevu ekle')
        print('2) Randevuları görüntüle')
        print('3) TXT raporu kaydet')
        print('4) Gizlilik odaklı TXT raporu kaydet')
        print('5) Çıkış')
        secim = input('Seçiminiz (1-5): ').strip()
        if secim == '1':
            randevu_ekle()
        elif secim == '2':
            print('\n' + rapor_metni())
        elif secim == '3':
            rapor_kaydet()
        elif secim == '4':
            gizlilik_raporu_kaydet()
        elif secim == '5':
            print('Program kapatıldı.')
            break
        else:
            print('Geçersiz seçim. Lütfen 1, 2, 3, 4 veya 5 girin.')


if __name__ == '__main__':
    randevulari_yukle()
    ana_menu()
