#!/usr/bin/env python3
import argparse
import shlex
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="OS-28: File Search & Text-Grep Teaching Wrapper")
    parser.add_argument("path", nargs="?", default=".", help="Aranacak dizin yolu")
    parser.add_argument("file_pattern", nargs="?", default="*.py", help="Wildcard içeren dosya kalıbı (örn: *.py, test*)")
    parser.add_argument("search_term", nargs="?", default="def", help="Dosyalarda aranacak metin (grep için)")
    parser.add_argument("--execute", action="store_true", help="Oluşturulan komutları terminalde gerçekten çalıştırır")

    args = parser.parse_args()

    # Komutları f-string yerine argüman listesi olarak tanımlama
    find_args = ["find", args.path, "-name", args.file_pattern]
    grep_args = ["grep", "-rn", "--", args.search_term, args.path]

    print("=" * 70)
    print(" OS-28: File Search & Text-Grep Teaching Wrapper")
    print("=" * 70)

    print("\n[EĞİTSEL AÇIKLAMA] Girdilerinizden üretilen Linux Komutları:")
    print("-" * 70)
    print("1. Dosya Arama Komutu (Find):")
    print(f"   Argüman listesi : {find_args}")
    print(f"   Komut görünümü  : {shlex.join(find_args)}")
    print("   Açıklama:")
    print("      * find: Belirtilen dizin altında dosya ve klasör arar.")
    print(f"      * {args.path}: Aramanın başlatılacağı konum.")
    print(f"      * -name {args.file_pattern}: Wildcard (*) kullanarak dosya adını filtreler.")

    print("\n2. Metin Tarama Komutu (Grep):")
    print(f"   Argüman listesi : {grep_args}")
    print(f"   Komut görünümü  : {shlex.join(grep_args)}")
    print("   Açıklama:")
    print("      * grep -rn: Dizin içinde özyinelemeli (-r) arama yapar ve satır numarası (-n) gösterir.")
    print("      * --: Arama ifadesinin tire (-) ile başlaması durumunda seçenek olarak algılanmasını önler.")
    print(f"      * {args.search_term}: Aranan hedef kelime/metin.")
    print("-" * 70)

    if args.execute:
        print("\n[ÇALIŞTIRMA] Komutlar argüman listesiyle çalıştırılıyor...\n")
        try:
            base_path = Path(args.path).resolve()
            if not base_path.exists() or not base_path.is_dir():
                print(f"Hata: Geçerli bir dizin bulunamadı -> {args.path}")
                return

            target_dir = str(base_path)

            # Önce eşleşen dosyaları bul
            find_cmd = ["find", target_dir, "-type", "f", "-name", args.file_pattern]
            print(f"Çalışan find listesi : {find_cmd}")
            find_proc = subprocess.run(find_cmd, capture_output=True, text=True, check=False)
            matched_files = [line for line in find_proc.stdout.splitlines() if line.strip()]

            if not matched_files:
                print("Eşleşen dosya bulunamadı.")
                return

            # Bulunan dosyalarda grep'i argüman listesiyle (shell=False) çalıştır
            grep_cmd = ["grep", "-n", "--", args.search_term, *matched_files]
            print(f"Çalışan grep listesi : {grep_cmd}\n")
            grep_proc = subprocess.run(grep_cmd, capture_output=True, text=True, check=False)

            if grep_proc.stdout:
                print(grep_proc.stdout.rstrip())
            else:
                print("Eşleşen sonuç bulunamadı.")

            if grep_proc.stderr:
                print(f"Uyarı/Hata: {grep_proc.stderr.rstrip()}")

        except Exception as e:
            print(f"Çalıştırma hatası: {e}")
    else:
        print("\n[İpucu]: Komutları sistem üzerinde gerçekten çalıştırmak için sonuna '--execute' ekleyebilirsiniz.")
        print("Örnek: python3 os-28-search-grep-wrapper.py . '*.py' 'def' --execute")


if __name__ == "__main__":
    main()

    
           
