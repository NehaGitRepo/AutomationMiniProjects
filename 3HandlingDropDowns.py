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

#Printing all the links in webpage
links = driver.find_elements(By.TAG_NAME,"a")
print("Total number of links are: ", len(links))
for link in links:
    print("Text is: ",link.text, " | URL is: ", link.get_attribute("href"))
#printing only 4th link text
print("4th link in page is:" ,driver.find_elements(By.TAG_NAME,"a").__getitem__(4).text)

#printing links from a particular section of page
print("-----------------Printing links in a block-----------------------------")
block =driver.find_element(By.XPATH,"//nav[@aria-label='Other projects']")
links=block.find_elements(By.TAG_NAME,"a")
print("Total number of links in block are: ", len(links))

print("----first link is---: ",driver.find_elements(By.TAG_NAME,"a").__getitem__(1).text)

for link in links:
    print("Text is: ",link.text, " | URL is: ", link.get_attribute("href"))


print("1st link in block is:" ,block.find_elements(By.TAG_NAME,"a").__getitem__(0).text)
