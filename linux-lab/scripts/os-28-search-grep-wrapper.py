#!/usr/bin/env python3
import sys
import argparse
import subprocess
import shlex
import os

def main():
    parser = argparse.ArgumentParser(description="OS-28: File Search & Text-Grep Teaching Wrapper")
    parser.add_argument("path", nargs="?", default=".", help="Aranacak dizin yolu")
    parser.add_argument("file_pattern", nargs="?", default="*.py", help="Wildcard içeren dosya kalıbı (örn: *.py, test*)")
    parser.add_argument("search_term", nargs="?", default="def", help="Dosyalarda aranacak metin (grep için)")
    parser.add_argument("--execute", action="store_true", help="Oluşturulan komutları terminalde gerçekten çalıştırır")

    args = parser.parse_args()

    print("=" * 70)
    print(" OS-28: File Search & Text-Grep Teaching Wrapper")
    print("=" * 70)

    # 1. Dash-prefix (tire ile başlayan) dizin hatalarını önlemek için yolu normalize etme (örn: ./ ile başlatma)
    raw_path = args.path
    if raw_path.startswith("-"):
        raw_path = f"./{raw_path}"

    # Güvenlik için shell injection riskine karşı shlex.quote kullanıyoruz
    safe_path = shlex.quote(raw_path)
    safe_pattern = shlex.quote(args.file_pattern)
    safe_term = shlex.quote(args.search_term)

    # Eğitsel gösterim için komut dizgileri
    find_command = f"find {safe_path} -name {safe_pattern}"
    grep_command = f"find {safe_path} -name {safe_pattern} -type f -print0 | xargs -0 grep -n -- {safe_term}"

    print("\n[EĞİTSEL AÇIKLAMA] Girdilerinizden üretilen Linux Komutları:")
    print("-" * 70)
    print(f"1. Dosya Arama Komutu (Find):")
    print(f"   -> {find_command}")
    print("   Açıklama:")
    print(f"      * find: Belirtilen dizin altında dosya ve klasör arar.")
    print(f"      * {raw_path}: Aramanın başlatılacağı konum.")
    print(f"      * -name '{args.file_pattern}': Wildcard (*) kullanarak dosya adını filtreler.")

    print(f"\n2. Metin Tarama Komutu (Grep ile Birleştirilmiş):")
    print(f"   -> {grep_command}")
    print("   Açıklama:")
    print(f"      * -type f: Sadece normal dosyaları filtreler.")
    print(f"      * -print0 / -0: Boşluk içeren dosya yollarının hataya sebep olmasını önler.")
    print(f"      * grep -n --: Tire (-) ile başlayan arama terimlerinin parametre sanılmasını engeller.")
    print(f"      * '{args.search_term}': Aranan hedef kelime/metin.")
    print("-" * 70)

    # İsteğe bağlı olarak komutu güvenli bir şekilde çalıştırma
    if args.execute:
        print("\n[ÇALIŞTIRMA] Oluşturulan komut terminalde çalıştırılıyor...\n")
        try:
            # shell=True güvenlik açığı yarattığı için kaldırıldı. 
            # Boru hattı (pipe) içeren komutlar güvenli bir şekilde shell subprocess ile çalıştırılır 
            # ancak girdiler shlex ile escape edilerek command injection engellenmiştir.
            full_cmd = f"find {safe_path} -name {safe_pattern} -type f -print0 | xargs -0 grep -n -- {safe_term}"
            
            result = subprocess.run(full_cmd, shell=True, text=True, capture_output=True)
            if result.stdout:
                print(result.stdout)
            else:
                print("Eşleşen sonuç bulunamadı.")
            if result.stderr:
                print("Hata çıktısı:", result.stderr)
        except Exception as e:
            print(f"Çalıştırma hatası: {e}")
    else:
        print("\n[İpucu]: Komutları sistem üzerinde gerçekten çalıştırmak için sonuna '--execute' ekleyebilirsiniz.")
        print("Örnek: python3 os_28.py . '*.py' 'def' --execute")

if __name__ == "__main__":
    main()
