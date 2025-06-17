from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
import logging

def get_pdf_links():
    base_url = "https://mnre.gov.in"
    url = "https://mnre.gov.in/en/monthly-updates/"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        pdf_links = []

        # Wait a bit for JS to load (optional: add WebDriverWait for robust wait)
        driver.implicitly_wait(5)

        anchors = driver.find_elements("xpath", "//a[contains(@href, '.pdf')]")
        for a in anchors:
            href = a.get_attribute("href")
            if href:
                full_url = urljoin(base_url, href)
                if full_url not in pdf_links:
                    pdf_links.append(full_url)

        print(f"Found {len(pdf_links)} PDFs")
        return pdf_links

    except Exception as e:
        print(f"Error: {str(e)}")
        return []
    finally:
        driver.quit()
