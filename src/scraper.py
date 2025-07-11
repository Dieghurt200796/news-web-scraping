import logging
import logging.config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.setup import driver

def open_site():
    driver.get("https://www.bbc.com/")

def get_headlines():
    headline_selector='h2[data-testid="card-headline"]'
    try:
        wait = WebDriverWait(driver, 20)
        headlines = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, headline_selector)))
    except Exception as e:
        logging.warning(f"Could not find headlines.\nError: {e}")
        return []

    headlines = [headline.get_attribute('textContent') for headline in headlines]
    return set(headlines)

def main():
    logging.config.fileConfig('logging.conf')
    try:
        open_site()
        headlines = get_headlines()
        if headlines:
            print("--- SCRAPED HEADLINES ---")
            for i, title in enumerate(headlines, 1):
                print(f"{i}: {title}")
            print("-------------------------")
        else:
            logging.info("No headlines were found.")

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()