#Printing all the languages available on wikipedia.com

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

#selecting the drop down element having languages
dropDown = driver.find_element(By.XPATH,"//*[@name='language']")
select = Select(dropDown)
select.select_by_value("hi")

#printing all the languages
DropDownOptions = driver.find_elements(By.TAG_NAME,"option")
for option in DropDownOptions:
    print("Text is ", option.text, "Language is: "+option.get_attribute("lang"))

#printing total number of languages
print("Total Drop Down values are: ", len(DropDownOptions))