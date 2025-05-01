# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
 

def get_chrome_browser(site):
    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    chrome_browser.get(site)
    return chrome_browser

browser = get_chrome_browser('https://www.google.com')
time.sleep(10)
