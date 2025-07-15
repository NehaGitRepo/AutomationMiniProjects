from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
#
# def is_element_present(how,what):
#     try:
#         driver.find_element(by=how,value=what)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how,what):
    if len(driver.find_elements(by=how,value=what))==0:
        return False
    else:
        return True




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://gmail.com/")
driver.maximize_window()
driver.implicitly_wait(1)

print(is_element_present(By.ID,"identifierID"))
print(is_element_present(By.XPATH,"//*[@id='identifierId']"))