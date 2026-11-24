# OS-28: File Search & Text-Grep Teaching Wrapper

## Amaç
Bu görev kapsamında, verilen dizin (`path`), wildcard dosya kalıbı (`file_pattern`) ve aranacak metne (`search_term`) göre `find` ve `grep` komutlarını argüman listesi olarak oluşturan, seçenekleri açıklayan ve istendiğinde (`--execute`) çalıştırıp neyin çalıştığını gösteren bir öğretici sarmalayıcı (`linux-lab/scripts/os-28-search-grep-wrapper.py`) geliştirildi.

## Nasıl Çalışır?
- Komutlar `f-string` yerine argüman listeleri (`find_args`, `grep_args`, `find_cmd`, `grep_cmd`) şeklinde hazırlanır.
- Ekranda eğitimsel modda komutların ne işe yaradığı (`find`, `-name` wildcard filtresi, `grep -rn`, `--` ayıracı ve arama ifadesi) açıklanır.
- `--execute` bayrağı verildiğinde hedef dizin doğrulanır, eşleşen dosyalar `find` ile listelenir ve bulunan dosyalarda `grep -n --` argüman listesiyle (`subprocess.run`) arama yapılır; çalışan komut listeleri ve sonuçlar ekrana yazdırılır.

## Test ve Video
- Doğrulama adımları ve komut çıktıları `linux-lab/os-28/VERIFY.md` dosyasında yer alır.
- Çalışma videosu / ekran kaydı: 
