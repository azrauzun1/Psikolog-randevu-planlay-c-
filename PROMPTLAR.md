# Yapay zekâ ile çalışma günlüğü

**Ders:** GEP1316 Kodlama Okuryazarlığı – Ara Değerlendirme Ödevi 1  
**Öğrenci:** Beyza Azra Uzun  
**Araç:** ChatGPT (2026)  

Bu dosya beş gerçek takip promptunun tam metinlerini ve öğrencinin konuşmada onayladığı kararlarını içerir. Başlangıç yönergesi beş promptun içinde sayılmamıştır.

## PROMPT 1 – Randevu çakışması ve çalışma saatleri

**Gönderdiğim prompt (tam metin):**

> Psikolog Randevu Planlayıcısı uygulamamın ilk Python kodunu incele. Randevu çakışmalarını nasıl kontrol ettiğini basitçe açıkla. Bu sistemde eksik veya geliştirilebilecek bir özellik varsa bana iki seçenek sun. Kodda değişiklik yapmadan önce benim kararımı bekle.

**YZ yanıtının özeti:** YZ çalışma saatleri kontrolü (A) veya iptal özelliği (B) önerdi.

**Seçtiğim karar:** A – çalışma saatleri kontrolü. Seansın tamamının 09.00–18.00 arasında olması seçildi.

**Onayladığım öğrenci gerekçesi:** Yapay zekâ bana çalışma saatleri kontrolü ve randevu iptali olmak üzere iki geliştirme önerdi. Çalışma saatleri kontrolünü seçtim çünkü bir psikoloğun günlük programını düzenlerken seansların mesai saatleri içerisinde tamamlanmasının önemli olduğunu düşündüm. Bu özellik sayesinde çalışma saatleri dışında randevu oluşturulması önleniyor.

## PROMPT 2 – Hatalı girdiler ve geçmiş tarih

**Gönderdiğim prompt (tam metin):**

> Psikolog Randevu Planlayıcısı uygulamamın kullanıcı girdilerini incele. Özellikle boş danışan kodu, geçersiz tarih, hatalı saat ve sıfır veya negatif seans süresi girildiğinde programın nasıl davrandığını gerçek Python testleriyle kontrol et. Eksik ya da geliştirilebilecek bir nokta bulursan bana iki çözüm önerisi sun. Kodda değişiklik yapmadan önce kararımı bekle.

**YZ yanıtının özeti:** YZ geçmiş tarih kontrolü (A) veya açıklayıcı hata mesajları (B) önerdi.

**Seçtiğim karar:** A – sistem tarihinden eski tarihlere randevu eklenmesi önlendi.

**Onayladığım öğrenci gerekçesi:** Yapay zekâ ile yaptığımız testlerde programın geçmiş tarihlere de randevu oluşturabildiğini fark ettim. Bu eksikliği düzeltmeyi tercih ettim çünkü gerçek bir psikolog randevu sisteminde geçmiş tarihlere yeni randevu verilmesi mantıklı değildir. Programın bugünün tarihini otomatik kontrol etmesini istedim. Böylece geçmiş tarihler reddedilirken güncel ve gelecek tarihler kabul ediliyor.

## PROMPT 3 – TXT kaydı ve yeniden açma

**Gönderdiğim prompt (tam metin):**

> Psikolog Randevu Planlayıcısı uygulamamın dosya kaydetme özelliğini incele. Randevuların .txt dosyasına nasıl kaydedildiğini açıkla. Özellikle program kapatılıp yeniden açıldığında kayıtların korunup korunmadığını gerçek Python testleriyle kontrol et. Eksik veya geliştirilebilecek bir özellik bulursan bana iki çözüm önerisi sun. Kodda değişiklik yapmadan önce kararımı bekle.

**YZ yanıtının özeti:** YZ kayıtları otomatik geri yükleme (A) veya eski raporun üzerine yazılmasını önleme (B) önerdi.

**Seçtiğim karar:** A – açılışta TXT dosyasından randevuları okuma seçildi.

**Onayladığım öğrenci gerekçesi:** Yapay zekâ ile yaptığımız incelemede programın randevuları TXT dosyasına kaydetmesine rağmen yeniden açıldığında eski kayıtları yüklemediğini gördüm. Bu sorunu çözmek için otomatik geri yükleme özelliğini seçtim. Çünkü bir psikoloğun her gün aynı randevu bilgilerini yeniden girmesi zaman kaybına neden olur. Ayrıca eski kayıtların korunması, yeni randevuların mevcut seanslarla çakışmasını önlemek açısından da önemlidir.

## PROMPT 4 – Danışan gizliliği

**Gönderdiğim prompt (tam metin):**

> Psikolog Randevu Planlayıcısı uygulamamı danışan gizliliği açısından incele. Programın hangi bilgileri topladığını ve TXT dosyasına neleri kaydettiğini açıkla. Gerçek danışan bilgileri kullanmadan, anonim kodlarla çalışmanın avantajlarını değerlendir. Gizliliği artırmak için iki farklı geliştirme önerisi sun. Kodda değişiklik yapmadan önce kararımı bekle.

**YZ yanıtının özeti:** YZ gizlilik raporu (A) veya program açılış şifresi (B) önerdi.

**Seçtiğim karar:** A – danışan kodu içermeyen ikinci TXT raporu eklendi.

**Onayladığım öğrenci gerekçesi:** Yapay zekâ ile yaptığımız incelemede programın danışanların gerçek isimlerini kullanmamasına rağmen randevu kodlarını TXT dosyasına kaydettiğini gördüm. Gizliliği artırmak için danışan kodlarının görünmediği ayrı bir rapor oluşturmayı seçtim. Çünkü psikoloji alanında danışan bilgilerinin korunmasının önemli olduğunu düşünüyorum. Böylece normal kayıtları değiştirmeden yalnızca tarih, saat ve seans süresini gösteren ikinci bir rapor oluşturabiliyoruz.

## PROMPT 5 – Teknik gereksinimler ve güvenli kayıt

**Gönderdiğim prompt (tam metin):**

> Psikolog Randevu Planlayıcısı uygulamamın mevcut Python kodunu hocamın GEP1316 Ara Değerlendirme Ödevi 1 yönergesine göre incele. En az üç kullanıcı girdisi, iki karar yapısı, bir döngü, üç fonksiyon, liste veya sözlük kullanımı, TXT dosyasına kayıt ve hatalı girdi kontrolü gereksinimlerini tek tek değerlendir. Kodun anlaşılmasını veya güvenilirliğini artırabilecek iki geliştirme önerisi sun. Henüz değişiklik yapma, önce kararımı bekle.

**YZ yanıtının özeti:** YZ güvenli dosya kaydı (A) veya tarihe göre filtreleme (B) önerdi.

**Seçtiğim karar:** A – geçici dosyaya yazma, başarılı olunca değiştirme ve başarısız kayıt halinde bellekten geri alma seçildi.

**Onayladığım öğrenci gerekçesi:** Yapay zekâ ile kodu incelediğimizde dosyaya kaydetme başarısız olsa bile randevunun programın belleğinde kalabildiğini öğrendim. Bu nedenle dosya kaydetme güvenliğini artırmayı seçtim. Çünkü psikoloğun bir randevunun kaydedildiğini düşünmesi ancak bilgilerin gerçekte dosyaya yazılmamış olması karışıklığa neden olabilir. Yapılan düzenlemeyle kayıt başarısız olduğunda kullanıcıya uyarı verilmesini ve eski kayıtların korunmasını sağladık.

## Eleştirel değerlendirme ve test

PROMPT 2 incelemesinde geçmiş tarihe randevu ekleme kontrolünün eksik olduğu, PROMPT 3 incelemesinde eski TXT dosyasının yeniden açılışta yüklenmediği ve PROMPT 5 incelemesinde kaydetme başarısızlığından sonra bellek kaydının korunabildiği belirlendi. Bunlar geliştirme sürecinde ele alınan gerçek eksiklerdir; yapay zekânın ürettiği kodun otomatik olarak doğru kabul edilmediğini gösterir.

Son sürüm bağımsız olarak 13 otomatik Python testinden geçti. Test dosyasındaki çıktılar çalıştırma ile elde edilmiştir. Kaydetme hatası unittest.mock kullanılarak simüle edilmiştir; gerçek disk arızası değildir.

## Kaynakça

OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com
