import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://way2automation.com")
driver.maximize_window()

driver.implicitly_wait(10)


driver.find_element(By.XPATH,"//i[@class='eicon-close']").click() # Remove ad

menu = driver.find_element(By.XPATH,"//li[@id='menu-item-27617']//span[@class='menu-text'][normalize-space()='Resources']")
action = ActionChains(driver)
action.move_to_element(menu).perform()
driver.find_element(By.XPATH,"//li[@id='menu-item-27619']//span[@class='menu-text'][normalize-space()='Practice Site 2']").click()
time.sleep(20)



