import os
import shutil
from PIL import Image

# --- AYARLAR ---
SOURCE_DIR = "wp-content"
TARGET_DIR = "wp-content-2"
MAX_SIZE_KB = 500  # 500 KB sınırı
TARGET_LONG_EDGE = 800  # Uzun kenar 800px
JPG_QUALITY = 75  # JPG kalitesi

def optimize_images():
    if not os.path.exists(SOURCE_DIR):
        print(f"Hata: {SOURCE_DIR} klasörü bulunamadı!")
        return

    processed_count = 0
    optimized_count = 0

    print("İşlem başlıyor, lütfen bekleyin...\n")

    for root, dirs, files in os.walk(SOURCE_DIR):
        # Hedef klasör yapısını oluştur
        relative_path = os.path.relpath(root, SOURCE_DIR)
        dest_path = os.path.join(TARGET_DIR, relative_path)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        for file in files:
            file_extension = file.lower().split('.')[-1]
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(dest_path, file)
            
            # Sadece yaygın görsel formatlarını işle
            if file_extension in ['jpg', 'jpeg', 'png', 'webp']:
                file_size_kb = os.path.getsize(source_file_path) / 1024
                
                # Kriter: 500 KB'dan büyükse işlem yap
                if file_size_kb > MAX_SIZE_KB:
                    try:
                        with Image.open(source_file_path) as img:
                            # Orijinal boyutları al
                            width, height = img.size
                            
                            # Uzun kenarı 800px yapacak oranı hesapla
                            if width > height:
                                if width > TARGET_LONG_EDGE:
                                    new_width = TARGET_LONG_EDGE
                                    new_height = int((TARGET_LONG_EDGE / width) * height)
                                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                            else:
                                if height > TARGET_LONG_EDGE:
                                    new_height = TARGET_LONG_EDGE
                                    new_width = int((TARGET_LONG_EDGE / height) * width)
                                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                            # Kaydet (JPG ise kaliteyi ayarla, değilse normal kaydet)
                            if file_extension in ['jpg', 'jpeg']:
                                img.save(target_file_path, "JPEG", quality=JPG_QUALITY, optimize=True)
                            else:
                                img.save(target_file_path, optimize=True)
                            
                        optimized_count += 1
                        print(f"Optimize Edildi: {file} ({int(file_size_kb)}KB -> {int(os.path.getsize(target_file_path)/1024)}KB)")
                    except Exception as e:
                        print(f"Hata ({file}): {e}")
                        shutil.copy2(source_file_path, target_file_path)
                else:
                    # 500 KB'dan küçükse doğrudan kopyala
                    shutil.copy2(source_file_path, target_file_path)
            else:
                # Görsel olmayan dosyaları (pdf, zip vb.) doğrudan kopyala
                shutil.copy2(source_file_path, target_file_path)
            
            processed_count += 1

    print(f"\n--- İşlem Tamamlandı ---")
    print(f"Toplam işlenen dosya: {processed_count}")
    print(f"Optimize edilen büyük görsel: {optimized_count}")
    print(f"Yeni dosyalar '{TARGET_DIR}' klasörüne kaydedildi.")

if __name__ == "__main__":
    optimize_images()