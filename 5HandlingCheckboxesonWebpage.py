#Printing all the languages available on wikipedia.com

from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
checkbox = driver.find_element(By.CLASS_NAME,"Automation")
if checkbox.is_enabled():
    print("checkbox is enabled")
    checkbox.click()

if checkbox.is_selected():
    print("checkbox is selected")
time.sleep(2)
driver.quit()