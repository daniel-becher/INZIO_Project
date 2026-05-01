from fastapi import Form, FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = FastAPI()
template = Jinja2Templates (directory="templates")

def google_scrape(query: str):
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    # Tohle přidá maskování:
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    results = []

    try:
        url = f"https://www.google.com/search?q={query}&hl=cs"
        driver.get(url)

        try:
            cookie_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "L2AGLb"))
            )
            cookie_button.click()
        except:
            pass
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.LC20lb")))

        elements = driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb")
        for i, el in enumerate(elements):
            try:
                parnet = el.find_element(By.XPATH, "./..")
                results.append({
                    "order": i+1,
                    "title": el.text,
                    "link": parnet.get_attribute("href")
                })
            except:
                continue
    except Exception as e:
        print(f"Error during scraping: {e}")
    finally:
        driver.quit()
    return results

@app.get("/", response_class=HTMLResponse)
async def read(request: Request): 
    return template.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/search")
async def post(key_word: str = Form(...)):
    data = google_scrape(key_word)

    file_path = "results_google.json"
    with open (file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return FileResponse(path=file_path, filename="results_google.json", media_type="application/json")

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)