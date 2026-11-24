# OS-28 Doğrulama (VERIFY)

## Kod Uyumu Notu
- Betik (`linux-lab/scripts/os-28-search-grep-wrapper.py`) komutları `f-string` ile birleştirmek yerine argüman listeleri ve `subprocess.run` (`shell=False`) ile çalıştırır; komutlar ekranda `shlex.quote` ile gösterilir ve `find` komutu `-print0` ile çalışır (çıktı NUL karakterine göre ayrılır).

## Test Hazırlığı
```bash
mkdir -p "/tmp/os28-test/my dir"
printf 'def a():\n    pass\n' > "/tmp/os28-test/my dir/a b.py"
printf "def z(): pass\nit's here\n-x test(\n" > /tmp/os28-test/z.py
```

## Test Komutları ve Çıktıları

### 1. Sadece komut ve açıklama gösterimi (`--execute` olmadan)
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py /tmp/os28-test '*.py' 'def'
```
Beklenen: `find` ve `grep` komutları argüman listesi ve `shlex.quote` görünümüyle açıklanır, komut çalıştırılmaz.

Çıktı:
```text
(terminal çıktısı buraya yapıştırılacak)
```

### 2. Komutları çalıştırma ve boşluklu klasör/dosya adı (`--execute`)
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py /tmp/os28-test '*.py' 'def' --execute
```
Beklenen: `my dir/a b.py` ve `z.py` bulunur, her ikisinde `def` satırı yazdırılır.

Çıktı:
```text
(terminal çıktısı buraya yapıştırılacak)
```

### 3. Tire (`-`) ile başlayan ve özel karakter içeren arama metni
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py /tmp/os28-test '*.py' '-x test(' --execute
```
Beklenen: `--` ayıracı ve `-F` sayesinde metin seçenek ya da düzenli ifade sanılmaz, `z.py` içindeki `-x test(` satırı bulunur.

Çıktı:
```text
(terminal çıktısı buraya yapıştırılacak)
```

### 4. Tek tırnak içeren arama metni
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py /tmp/os28-test '*.py' "it's" --execute
```
Beklenen: komut bozulmaz, `z.py` içindeki `it's here` satırı bulunur.

Çıktı:
```text
(terminal çıktısı buraya yapıştırılacak)
```

### 5. Geçersiz dizin
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py /yok/dizin '*.py' 'def' --execute
```
Beklenen: komut çalıştırılmadan önce "Geçerli bir dizin bulunamadı" hatası verilir.

Çıktı:
```text
(terminal çıktısı buraya yapıştırılacak)
```
