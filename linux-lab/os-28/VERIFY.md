# OS-28 Doğrulama (VERIFY)

## Kod Uyumu Notu
- Betik (`linux-lab/scripts/os-28-search-grep-wrapper.py`) komutları `f-string` ile birleştirmek yerine argüman listeleri ve `subprocess.run` kullanır; kodda `shlex.quote` veya `-print0` kullanılmamıştır.

## Test Komutları ve Çıktıları

### 1. Sadece komut ve açıklama gösterimi (`--execute` olmadan)
```bash
python3 linux-lab/scripts/os-28-search-grep-wrapper.py . '*.py' 'def'
