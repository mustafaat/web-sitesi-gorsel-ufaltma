# web-sitesi-gorsel-ufaltma
500 kb.'dan büyük görsel dosyaları bulur, uzun kenarları 800 piksele düşürür, son olarak jpg kalitesini %75 yaparak yeni klasöre kayıt eder. 500 kb.'den küçük dosyaları da hedef klasöre kopyalar.

---
[ Wordpress'i yerelde çalıştırmak isterseniz yapmanız gereken LocalWP ([localwp.com](localwp.com)) kurmak we sitenizin yedeğini istediğiniz eklenti ile yerele aktarmaktır. ]

# Görsel Optimizasyon ve Boyutlandırma Aracı (gorsel-opt.py)

Bu Python scripti, bir kaynak dizindeki görselleri tarar, belirli bir boyut sınırının (örn. 500 KB) üzerindeki dosyaları otomatik olarak yeniden boyutlandırır ve optimize ederek yeni bir dizine aktarır. Görsel olmayan veya zaten küçük olan dosyaları ise yapıya sadık kalarak doğrudan kopyalar.

## 🚀 Özellikler

* **Boyut Odaklı Optimizasyon:** Sadece belirlediğiniz eşik değerinden (`MAX_SIZE_KB`) büyük dosyaları işleyerek gereksiz işlem yükünü önler.
* **En-Boy Oranını Koruma:** Görsellerin uzun kenarını baz alarak (`TARGET_LONG_EDGE`) oranları bozmadan küçültür.
* **Dizin Yapısını Koruma:** Kaynak klasördeki (`wp-content`) tüm alt klasör mimarisini hedef klasörde (`wp-content-2`) aynen oluşturur.
* **Akıllı Filtreleme:** `.jpg`, `.jpeg`, `.png` ve `.webp` formatlarını destekler; PDF, ZIP gibi dosyalara dokunmadan kopyalar.
* **Yüksek Kaliteli Sıkıştırma:** `LANCZOS` yeniden örnekleme algoritması ve ayarlanabilir JPG kalite parametresi ile dengeli sonuçlar sunar.

## 🛠️ Teknolojiler ve Bağımlılıklar

* **Python 3.x**
* **Pillow (PIL):** Görsel işleme ve manipülasyon için.
* **Shutil & OS:** Dosya sistemi ve kopyalama işlemleri için.

## 📦 Kurulum

1. **Gerekli kütüphaneyi yükleyin:**
```bash
pip install Pillow

```


2. **Projeyi hazırlayın:**
`gorsel-opt.py` dosyasını, işlem yapmak istediğiniz ana dizine yerleştirin.

## ⚙️ Yapılandırma

Kodun içindeki `--- AYARLAR ---` bölümünden ihtiyacınıza göre düzenleme yapabilirsiniz:

| Değişken | Varsayılan | Açıklama |
| --- | --- | --- |
| `SOURCE_DIR` | `"wp-content"` | Kaynak dosyaların bulunduğu klasör. |
| `TARGET_DIR` | `"wp-content-2"` | İşlenmiş dosyaların kaydedileceği yeni klasör. |
| `MAX_SIZE_KB` | `500` | İşlem yapılması için gereken minimum dosya boyutu. |
| `TARGET_LONG_EDGE` | `800` | Görselin uzun kenarının maksimum piksel değeri. |
| `JPG_QUALITY` | `75` | Çıktı kalitesi (1-100 arası). |

## 📖 Kullanım

Scripti çalıştırmak için:

```bash
python gorsel-opt.py

```

**İşlem Akışı:**

1. Script `SOURCE_DIR` içindeki her dosyayı kontrol eder.
2. Görsel 500 KB'dan büyükse; yeniden boyutlandırılır, sıkıştırılır ve kaydedilir.
3. Görsel zaten küçükse veya görsel değilse; orijinal haliyle hedef klasöre kopyalanır.
4. İşlem sonunda kaç dosyanın optimize edildiğine dair bir özet rapor sunulur.

---

### ⚠️ Önemli Not

Bu araç, orijinal dosyalarınızı korumak için tasarlanmıştır ve çıktıları her zaman **yeni bir klasöre** kaydeder. Yine de büyük çaplı işlemlerden önce yedek almanız önerilir.

---

Bu araçla web sitenizin yükleme hızını ciddi oranda artırabilirsin. Başka bir fonksiyon eklememi veya farklı bir dosyanı analiz etmemi ister misin?
