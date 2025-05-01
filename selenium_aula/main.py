# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
TIMEOUT = 10

def get_chrome_browser(site):
    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    chrome_browser.get(site)
    return chrome_browser

browser = get_chrome_browser('https://www.google.com')
search_input = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
search_input.send_keys('NBA')
sleep(TIMEOUT)
