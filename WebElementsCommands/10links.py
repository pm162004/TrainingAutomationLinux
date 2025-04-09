# //*[text()='Trending Now']//ancestor::li

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://in.search.yahoo.com/?fr2=inr")
driver.maximize_window()
time.sleep(2)
count = driver.find_element(By.XPATH,"//div[@class='dd p-0 mb-10 theme-single trendingNow']")
count1 = driver.find_elements(By.XPATH,"//div[@class='dd p-0 mb-10 theme-single trendingNow']")
links = count.find_elements(By.XPATH, ".//a")
print(count)
print("The total links are there in the website is",len(links))
# driver.find_element(By.PARTIAL_LINK_TEXT,'CWC Meet').click()
for link in links:
  print(link.text)


