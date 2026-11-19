import os
import time
from dotenv import load_dotenv

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

load_dotenv('.env')

driver_options = ChromeOptions()
driver_options.add_argument("--window-size=1792,1120")
driver_options.add_argument("--incognito")

driver_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver_options.add_experimental_option('useAutomationExtension', False)

driver = Chrome(driver_options)

stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.get('https://newlxp.ru/sign-in')

login_selector = '[data-testid=loginEmailInput]'
password_selector = '[data-testid=loginPasswordInput]'
button_selector = '[data-testid=loginSubmitButton]'
disciplines_selector = '/disciplines'

wait = WebDriverWait(driver, timeout=20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))

login_element = driver.find_element(By.CSS_SELECTOR, login_selector)
password_element = driver.find_element(By.CSS_SELECTOR, password_selector)
button_element = driver.find_element(By.CSS_SELECTOR, button_selector)

login_element.send_keys('trofimovay@spb.ithub.ru')
password_element.send_keys(os.getenv('PASSWORD') or "")
time.sleep(2)
button_element.click()

wait.until(EC.presence_of_element_located((By.XPATH, '//aside/div[4]/div[2]//p')))

notifications_elements = driver.find_elements(By.XPATH, '//aside/div[4]/div[2]/div')

for notification in notifications_elements:
    print(notification.get_attribute('outerHTML'))

driver.quit()