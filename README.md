# Legal-writings (Pisma Prawnicze)

System do tworzenia profesjonalnych pism urzędowych dla organów administracji publicznej.

## Architektura projektu

| Katalog | Opis |
|---------|-----|
| `input/` | Pliki źródłowe (pisma urzędów, odpowiedzi) |
| `context/` | Przekonwertowane pliki Markdown |
| `output/` | Szkice pism do wysłania |

| Plik | Opis |
|------|-----|
| `extract_context.py` | Konwertuje PDF/DOCX do Markdown |
| `markdown_to_pdf.py` | Konwertuje Markdown do PDF |
| `.config` | Konfiguracja (miejscowość, autor, podpis) |
| `.opencode/skills/analiza_dokumentow/SKILL.md` | Instrukcje dla LLM |

---

## Jak rozpocząć rozmowę z modelem?

### Komenda otwarcia projektu:

```bash
opencode --skill .opencode/skills/analiza_dokumentow/SKILL.md "Przeczytaj pliki w folderze context/ i pomóż mi napisać odpowiedź na pismo urzędu"
```

### Ścieżka do skillu:
```
.opencode/skills/analiza_dokumentow/SKILL.md
```

---

## Jak korzystać ze środowiska wirtualnego?

### Aktywacja:
```bash
source .venv/bin/activate
```

### Dezaktywacja:
```bash
deactivate
```

---

## Jak wygenerować PDF z istniejącego pliku Markdown?

### Sposób 1 – aktywacja środowiska:
```bash
source .venv/bin/activate
.venv/bin/python markdown_to_pdf.py output/nazwa_pliku.md
```

### Sposób 2 – bez aktywacji:
```bash
.venv/bin/python markdown_to_pdf.py output/nazwa_pliku.md
```

### Sposób 3 – najnowszy plik w output/:
```bash
.venv/bin/python markdown_to_pdf.py
```

---

## Konwencja nazewnictwa plików

`YYYY.MM.DD HH_MM_SS - tytul.md`

- **Strefa czasowa**: `TZ='Europe/Warsaw'`
- Format: `2026.04.22 14_30_45 - ponowione_zapytanie.md`
- **ZAWSZE twórz nowy plik – NIE nadpisuj istniejących**

---

## Jak otworzyć wygenerowany PDF?

```bash
open output/nazwa_pliku.pdf
```

---

## Jak wygenerować PDF z najnowszego pliku Markdown?

```bash
.venv/bin/python markdown_to_pdf.py
```

System automatycznie znajdzie najnowszy plik `.md` w katalogu `output/` i wygeneruje PDF.

---

## Workflow

1. Umieść pliki w `input/`
2. `.venv/bin/python extract_context.py` → konwersja do `context/`
3. Poproś LLM o stworzenie odpowiedzi (użyj instrukcji ze SKILL.md)
4. `.venv/bin/python markdown_to_pdf.py` → PDF do wysłania

---

## Konfiguracja

Edytuj `.config`:
```
miejscowosc=Warszawa
autor=Twoje Imię i Nazwisko
wyrazy_zaufania=Z poważaniem
```