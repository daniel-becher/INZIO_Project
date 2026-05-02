# Google Search Scraper & API 🚀

Moderní webový scraper postavený na **FastAPI** a **Selenium**, který automatizuje sběr výsledků z vyhledávače Google. Projekt je plně kontejnerizován a optimalizován pro nasazení v cloudu (např. Railway).

## ✨ Klíčové vlastnosti
- **Asynchronní API:** Postaveno na FastAPI pro vysoký výkon a rychlou odezvu.
- **Advanced Scraping:** Využívá Selenium s pokročilým maskováním botů (stealth mode, custom User-Agents, CDP příkazy).
- **Cloud Ready:** Automatická detekce prostředí (Windows vs. Linux/Railway) a konfigurace cest k prohlížeči Chromium.
- **Strojově čitelný výstup:** Výsledky jsou generovány do strukturovaného formátu JSON.
- **Unit Testing:** Pokrytí testy pomocí `pytest` pro zajištění stability scraping logiky a souborových operací.

## 🛠️ Technologie
- **Python 3.10+**
- **FastAPI** (Web framework)
- **Selenium WebDriver** (Automatizace prohlížeče)
- **Chromium / ChromeDriver** (Prohlížeč pro serverové prostředí)
- **Pytest** (Testování)
- **Jinja2** (HTML šablony)

## 🚀 Rychlý start

### Lokální spuštění (Windows/macOS)
1. **Klonování repozitáře:**
   ```bash
   git clone [https://github.com/daniel-becher/inizio.git](https://github.com/daniel-becher/inizio.git)
   cd inizio

2. **Instalace závislostí:**
   ```bash
   pip install -r requirements.txt

3. **Spuštění aplikace:**
   ```bash
   python google_test.py

4. **Spuštění testů:**
   ```bash
   pytest unit_tests.py