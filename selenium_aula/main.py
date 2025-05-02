# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

TIMEOUT = 10

def get_chrome_browser(site):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    chrome_service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Remove a detecção de automação
    chrome_browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    })

    chrome_browser.get(site)
    return chrome_browser

browser = get_chrome_browser('https://www.google.com')

# Espera o elemento de pesquisa aparecer na página
search_input = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

search_input.send_keys('Hello World')
search_input.send_keys(Keys.ENTER)

# Espera os resultados aparecerem
results = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((By.ID, 'search'))
)

links = results.find_elements(By.TAG_NAME, 'a')
links[0].click()
sleep(TIMEOUT)
